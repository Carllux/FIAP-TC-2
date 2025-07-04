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
    Busca dados históricos para uma lista de tickers usando a API do Yahoo Finance.
    """
    logging.info(f"Iniciando busca de dados para os tickers: {tickers}...")
    try:
        data = yf.download(tickers, start=start_date, end=end_date, progress=False)
        
        if data is None or data.empty:
            logging.warning(f"Nenhum dado retornado do yfinance para os tickers: {tickers}")
            return pd.DataFrame()

        # Seleciona apenas a(s) coluna(s) 'Close'
        if isinstance(data.columns, pd.MultiIndex):
            data = data['Close']
        elif 'Close' in data.columns:
            data = data[['Close']] # Colchetes duplos aqui já garantem um DataFrame
        else:
            logging.warning("Coluna 'Close' não encontrada nos dados baixados.")
            return pd.DataFrame()

        # --- ADIÇÃO PARA GARANTIR O TIPO DE RETORNO ---
        # Se após a seleção o resultado for uma Series (caso de um único ticker),
        # converte para DataFrame.
        if isinstance(data, pd.Series):
            data = data.to_frame(name=tickers[0] if len(tickers) == 1 else 'Close')
        # --------------------------------------------------

        logging.info("Busca de dados concluída com sucesso.")
        return data
        
    except Exception as e:
        logging.error(f"Erro ao buscar dados: {e}")
        return pd.DataFrame()

def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Preenche valores NaN com forward-fill e backward-fill."""
    return df.ffill().bfill()

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza nomes das colunas para lowercase e renomeia tickers."""
    novos_nomes = {
        '^BVSP': 'ibovespa',
        'USDBRL=X': 'dolar',
        '^GSPC': 'sp500',
        'CL=F': 'petroleo_brent',
        'PETR4.SA': 'petrobras'
    }
    df = df.rename(columns=novos_nomes)
    return df.rename(columns=str.lower)

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
