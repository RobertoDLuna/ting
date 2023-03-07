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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
