import os
import pathlib
from dotenv import load_dotenv
from typing import Dict, List # Importa o tipo para listas

# Carrega as variáveis de ambiente do arquivo .env para o sistema
load_dotenv()

# --- Paths ---
# Cria um caminho absoluto para a raiz do projeto, garantindo que funcione em qualquer OS
BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR: pathlib.Path = BASE_DIR / "data"

# --- Configurações do Pipeline de Dados ---
START_DATE: str = os.getenv("START_DATE", "2005-01-01")

# --- ADIÇÃO DO MAPEAMENTO DE NOMES ---
TICKER_MAP: Dict[str, str] = {
    '^BVSP': 'ibovespa',
    'VALE3.SA': 'vale',
    'PETR3.SA': 'petrobras_pn',
    'PETR4.SA': 'petrobras',
    'ITUB4.SA': 'itau_unibanco',
    'BBDC4.SA': 'bradesco_pn',
    'B3SA3.SA': 'b3',
    'ABEV3.SA': 'ambev',
    'BBAS3.SA': 'banco_do_brasil',
    'WEGE3.SA': 'weg',
    'RENT3.SA': 'localiza',
    'SUZB3.SA': 'suzano',
    'ELET3.SA': 'eletrobras',
    'ELET6.SA': 'eletrobras_pfb',
    'GGBR4.SA': 'gerdau_pn',
    'JBSS3.SA': 'jbs',
    'RAIL3.SA': 'rumo',
    'HAPV3.SA': 'hapvida',
    'LREN3.SA': 'lojas_renner',
    'RADL3.SA': 'raia_drogasil',
    'CSAN3.SA': 'cosan',
    'VIVT3.SA': 'telefonica_brasil',
    'BPAC11.SA': 'btg_pactual',
    'EQTL3.SA': 'equatorial',
    'BRFS3.SA': 'brf',
    'UGPA3.SA': 'ultrapar',
    'CCRO3.SA': 'ccr',
    'KLBN11.SA': 'klabin',
    'SBSP3.SA': 'sabesp',
    'TOTS3.SA': 'totvs',
    'MGLU3.SA': 'magazine_luiza',
    'ENGI11.SA': 'energisa',
    'EMBR3.SA': 'embraer',
    'AZUL4.SA': 'azul',
    'CYRE3.SA': 'cyrela',
    'NTCO3.SA': 'natura',
    'QUAL3.SA': 'qualicorp',
    'GOAU4.SA': 'metalurgica_gerdau',
    'CMIG4.SA': 'cemig',
    'BBDC3.SA': 'bradesco',
    'ITSA4.SA': 'itausa',
    'SANB11.SA': 'santander_br',
    'TAEE11.SA': 'taesa',
    'BRAP4.SA': 'bradespar',
    'USIM5.SA': 'usiminas',
    'CSNA3.SA': 'csn',
    'MRFG3.SA': 'marfrig',
    'GOLL4.SA': 'gol',
    'PCAR3.SA': 'pão_de_açúcar',
    'MRVE3.SA': 'mrv',
    'ECOR3.SA': 'ecorodovias',
    'YDUQ3.SA': 'yduqs',
    'COGN3.SA': 'cogna',
    'CVCB3.SA': 'cvc',
    'IRBR3.SA': 'irb_brasil',
    'HYPE3.SA': 'hypera',
    'DXCO3.SA': 'dexco',
    'BEEF3.SA': 'minerva',
    'BRKM5.SA': 'braskem',
    'CRFB3.SA': 'carrefour_br',
    'PRIO3.SA': 'petro_rio',
    'RRRP3.SA': '3r_petroleum',
    'ALPA4.SA': 'alpacruz',
    'CPLE6.SA': 'copel',
    'CPFE3.SA': 'cpfl_energia',
    'ENEV3.SA': 'eneva',
    'EGIE3.SA': 'engie_brasil',
    'FLRY3.SA': 'fleury',
    'GNDI3.SA': 'intermedica',
    'LWSA3.SA': 'locaweb',
    'SOMA3.SA': 'grupo_soma',
    'VAMO3.SA': 'vamos',
    'USDBRL=X': 'dolar',
    '^GSPC': 'sp500',
    'CL=F': 'petroleo_brent',
    'USDBRL=X': 'dolar'
}
# ------------------------------------

# Busca o nome do banco de dados do .env, com um valor padrão
DB_NAME: str = os.getenv("DATABASE_NAME", "mercados.duckdb")

# Constrói o caminho completo para o banco de dados
DB_PATH: pathlib.Path = DATA_DIR / DB_NAME

# Lista de ativos que queremos baixar.
TICKERS: List[str] = ["^BVSP", "USDBRL=X", "^GSPC", "CL=F", "PETR4.SA"]


# --- Configurações da Aplicação ---
# Permite configurar o nível de detalhe do log via .env
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
