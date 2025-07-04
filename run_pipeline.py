import argparse
import datetime
from src.data.pipeline import main
from src import config

if __name__ == "__main__":
    
    # 1. Cria o "parser" que lerá os argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Pipeline de dados para o Tech Challenge.")
    
    # 2. Adiciona o argumento --start-date
    parser.add_argument(
        '--start-date', 
        type=str, 
        default=config.START_DATE, # Usa o valor do config como padrão
        help=f"Data de início para a busca no formato AAAA-MM-DD. Padrão: {config.START_DATE}"
    )
    
    # Adiciona o argumento --end-date, usando a data de hoje como padrão
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    parser.add_argument(
        '--end-date', 
        type=str, 
        default=today_str,
        help=f"Data de fim para a busca no formato AAAA-MM-DD. Padrão: hoje ({today_str})"
    )
    
    # 3. Lê os argumentos que foram passados no terminal
    args = parser.parse_args()

    print(">>> Iniciando o pipeline a partir do lançador...")
    
    # 4. Chama a função main, passando os argumentos lidos
    main(start_date=args.start_date, end_date=args.end_date)
    
    print(">>> Pipeline finalizado.")