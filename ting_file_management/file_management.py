import sys


def txt_importer(path_file):
    # Caso o arquivo não tenha extensão txt
    if not path_file.endswith('txt'):
        # retorna erro de formato
        return sys.stderr.write('Formato inválido\n')
    try:
        # Abrindo o arquivo no modo leitura
        with open(path_file, mode="r") as file:
            # Abre o arquivo, retorna array splitado no \n
            file_data = file.read().split('\n')
            return file_data
    # Se houver algo, lança exception FileNotFoundError
    except FileNotFoundError:
        # Retornar a mensagem final
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
