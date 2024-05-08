import os

def separar_registros_cron(arquivo_log):

    registros_cron = []

    try:
        with open(arquivo_log, 'r') as file:

            for linha in file:

                if 'CRON' in linha:

                    # Extrair data e hora
                    data_hora = ' '.join(linha.split()[:3])

                    # Extrair nome de usuário
                    inicio_usuario = linha.find('(') + 1
                    fim_usuario = linha.find(')')
                    nome_usuario = linha[inicio_usuario:fim_usuario]

                    # Extrair comando da tarefa
                    inicio_comando = linha.find('CMD (') + len('CMD (')
                    fim_comando = linha.rfind(')')
                    comando_tarefa = linha[inicio_comando:fim_comando]

                    # Criar dicionário com informações do registro de cron
                    registro_cron = {
                        'data_hora': data_hora,
                        'nome_usuario': nome_usuario,
                        'comando_tarefa': comando_tarefa
                    }

                    registros_cron.append(registro_cron)

    except FileNotFoundError:

        print(f"Arquivo '{arquivo_log}' não encontrado.")

    except Exception as e:

        print(f"Erro ao processar o arquivo '{arquivo_log}': {e}")

    return registros_cron

def main():

    print("""
    Programa para separar os registros de cron de um arquivo de log.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        Lista de dicionários com as informações dos registros de cron.
    """)

    arquivo_log = input("Informe o caminho do arquivo: ")

    if not os.path.exists(arquivo_log):
            print(f"Arquivo '{arquivo_log}' não encontrado.")
            return

    registros_cron = separar_registros_cron(arquivo_log)

    if registros_cron:

        for i, registro in enumerate(registros_cron, 1):

            print(f"Registro {i}:")
            
            for chave, valor in registro.items():
                print(f"{chave}: {valor}")
            print()


if __name__ == "__main__":
    main()