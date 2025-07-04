import logging
import pandas as pd
import yfinance as yf
import duckdb
import pathlib


# Importa as configurações que definimos no nosso módulo config
import src.config as config

# Configuração básica do logging para vermos o progresso no terminal
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def fetch_data(tickers: list[str], start_date: str, end_date: str) -> pd.DataFrame:
    """
    Busca dados históricos (OHLCV) para uma lista de tickers.
    """
    logging.info(f"Iniciando busca de dados OHLCV para os tickers: {tickers}...")
    try:
        data = yf.download(tickers, start=start_date, end=end_date, progress=False)
        
        if data is None or data.empty:
            logging.warning(f"Nenhum dado retornado do yfinance para: {tickers}")
            return pd.DataFrame()

        # Se tivermos múltiplas colunas (MultiIndex), vamos achatá-las
        if isinstance(data.columns, pd.MultiIndex):
            # Une os dois níveis de nome de coluna, ex: ('Close', '^BVSP') -> 'close_^bvsp'
            data.columns = [f"{col[0].lower()}_{col[1]}" for col in data.columns]
        else:
            # Se for um único ticker, as colunas já são simples
            data.columns = [f"{col.lower()}" for col in data.columns]
            
        # Remove colunas que não usaremos (Adj Close e Volume)
        cols_to_drop = [col for col in data.columns if 'adj' in col or 'volume' in col]
        data = data.drop(columns=cols_to_drop)
            
        logging.info("Busca de dados concluída com sucesso.")
        return data
        
    except Exception as e:
        logging.error(f"Erro ao buscar dados: {e}")
        return pd.DataFrame()

def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Preenche valores NaN com forward-fill e backward-fill."""
    return df.ffill().bfill()

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza nomes de colunas iterativamente, substituindo tickers por nomes amigáveis.
    """
    # É uma boa prática trabalhar com uma cópia para evitar avisos do Pandas
    df_renamed = df.copy()
    
    # Pega a lista de nomes de colunas atuais para podermos modificá-la
    new_columns = df_renamed.columns.tolist()

    # Itera sobre cada item do nosso mapa de 'de-para' vindo do config
    for ticker, friendly_name in config.TICKER_MAP.items():
        # Para cada coluna na nossa lista, substitui o texto do ticker pelo nome amigável
        # Ex: 'close_^gspc' se torna 'close_sp500'
        new_columns = [col.replace(ticker, friendly_name) for col in new_columns]
    
    # Atribui a lista de nomes de colunas, agora modificada, de volta ao DataFrame
    df_renamed.columns = new_columns
    
    # A limpeza final garante que tudo esteja em minúsculas e sem caracteres especiais
    df_renamed.columns = df_renamed.columns.str.lower().str.replace('[^a-zA-Z0-9_]', '_', regex=True)

    return df_renamed

def process_dates(df: pd.DataFrame, date_column: str = 'Date') -> pd.DataFrame:
    """Converte e enriquece a coluna de datas."""
    df = df.reset_index().rename(columns={date_column: 'data'})
    df['data'] = pd.to_datetime(df['data'])
    
    # Adiciona semana do mês (1 a 5)
    df['semana_do_mes'] = ((df['data'].dt.day - 1) // 7) + 1
    
    # Formata data como string (opcional)
    df['data'] = df['data'].dt.strftime('%Y-%m-%d')
    return df

def validate_data(df: pd.DataFrame) -> None:
    """Valida se não há valores nulos."""
    assert not df.isnull().any().any(), "Dados contêm valores nulos após a limpeza."

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Orquestra a limpeza e transformação dos dados."""
    logging.info("Iniciando limpeza e padronização dos dados...")
    
    df_cleaned = fill_missing_values(df)
    df_cleaned = process_dates(df_cleaned)
    df_cleaned = standardize_columns(df_cleaned)
    
    validate_data(df_cleaned)
    logging.info(f"Colunas finais: {df_cleaned.columns.tolist()}")
    logging.info("Limpeza concluída.")
    
    return df_cleaned

def save_to_db(df: pd.DataFrame, table_name: str, db_path: pathlib.Path):
    """
    Salva o DataFrame limpo em uma tabela de um banco de dados DuckDB.
    """
    logging.info(f"Salvando dados na tabela '{table_name}' em: {db_path}")
    try:
        con = duckdb.connect(database=str(db_path), read_only=False)
        # A instrução CREATE OR REPLACE TABLE garante que podemos rodar o pipeline
        # várias vezes, sempre substituindo os dados pelos mais recentes.
        con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
        con.close()
        logging.info("Dados salvos com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao salvar dados no banco de dados: {e}")


def main(start_date: str, end_date: str):
    """
    Função principal que orquestra todo o pipeline de ETL (Extract, Transform, Load).
    Recebe as datas de início e fim como parâmetros.
    """
    logging.info("--- INICIANDO PIPELINE DE DADOS ---")
    
    # Usa os parâmetros recebidos pela função, em vez de valores fixos
    raw_data = fetch_data(
        tickers=config.TICKERS,
        start_date=start_date,
        end_date=end_date
    )
    
    if not raw_data.empty:
        cleaned_data = clean_data(raw_data)
        save_to_db(df=cleaned_data, table_name="precos_diarios", db_path=config.DB_PATH)
    else:
        logging.warning("Nenhum dado foi baixado. Pipeline encerrado.")
    
    logging.info("--- PIPELINE DE DADOS FINALIZADO ---")
