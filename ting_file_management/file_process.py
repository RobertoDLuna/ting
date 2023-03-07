from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # instânica da fila retornada pela lista()
    for index in range(len(instance)):
        # se o arquivo tiver o mesmo nome, retorna nada
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    # dados do arquivo
    file = txt_importer(path_file)
    data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": (file),
        }
    # carrega uma instânica de enqueue com os dados
    instance.enqueue(data)
    # É necessário sempre transformar em string
    sys.stdout.write(str(data))  # imprimir no terminal
    return data  # apenas pra testar


def remove(instance):
    # se não existe instancia ou len == 0
    if not instance or instance.__len__() == 0:
        return sys.stdout.write('Não há elementos\n')

    file_to_dequeue = instance.dequeue()
    # caminho do arquivo com a propriedade de nome
    path_file = file_to_dequeue["nome_do_arquivo"]
    # Retorno
    sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        # Procurando obj pelo índice
        info_data = instance.search(position)
        # Saída das infos do elem
        sys.stdout.write(str(info_data))
        return str(info_data)
    # Caso indice não exista
    except IndexError:
        # Saída
        sys.stderr.write('Posição inválida')
