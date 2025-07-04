import os
import pathlib
from dotenv import load_dotenv
from typing import List # Importa o tipo para listas

# Carrega as variáveis de ambiente do arquivo .env para o sistema
load_dotenv()

# --- Paths ---
# Cria um caminho absoluto para a raiz do projeto, garantindo que funcione em qualquer OS
BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR: pathlib.Path = BASE_DIR / "data"

# --- Configurações do Pipeline de Dados ---
# Busca a data de início do .env, com um valor padrão ("default") se não for encontrada
START_DATE: str = os.getenv("START_DATE", "2015-01-01")

# Busca o nome do banco de dados do .env, com um valor padrão
DB_NAME: str = os.getenv("DATABASE_NAME", "mercados.duckdb")

# Constrói o caminho completo para o banco de dados
DB_PATH: pathlib.Path = DATA_DIR / DB_NAME

# Lista de ativos que queremos baixar.
TICKERS: List[str] = ["^BVSP", "USDBRL=X", "^GSPC", "CL=F", "PETR4.SA"]

# --- Configurações da Aplicação ---
# Permite configurar o nível de detalhe do log via .env
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
