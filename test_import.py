import os
import sys

# 1. Imprimir o Diretório de Trabalho Atual (Current Working Directory - CWD)
# Isso nos diz DE ONDE o Python está sendo executado. É a informação mais crítica.
current_working_directory = os.getcwd()
print(f"--- Diretório de Trabalho Atual (CWD): ---")
print(current_working_directory)
print("-" * 20)

# 2. Listar TODOS os arquivos e pastas no CWD
# Vamos ver se o 'config.py' está realmente visível a partir daqui.
print(f"\n--- Arquivos e Pastas no CWD: ---")
try:
    file_list = os.listdir(current_working_directory)
    for item in file_list:
        print(item)
except Exception as e:
    print(f"Não foi possível listar os arquivos: {e}")
print("-" * 20)

# 3. Imprimir o sys.path novamente para confirmar
print("\n--- Python Path (sys.path): ---")
for path in sys.path:
    print(path)
print("-" * 20)

# 4. Tentar o import novamente dentro de um bloco try-except para um feedback claro
print("\n--- Tentando a importação ---")
try:
    import src.config as config
    print("\n✅ SUCESSO! O módulo 'config' foi importado.")
    print(f"Ticker de exemplo do config: {config.TICKERS[0]}")
except ModuleNotFoundError:
    print("\n❌ FALHA! ModuleNotFoundError ainda ocorre.")
except Exception as e:
    print(f"\n❌ FALHA! Erro inesperado: {e}")