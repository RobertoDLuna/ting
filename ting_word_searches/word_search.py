def exists_word(word, instance):
    # array com as ocorrencias
    occurrences = []
    # para cada elemento da lista
    for e in instance.list:
        occurrences_lines = []  # linhas da ocorrencia
        # adicionando informaçoes da ocorrencia
        occurrences.append({
            'palavra': word,
            'arquivo': e['nome_do_arquivo'],
            'ocorrencias': occurrences_lines
        })
        # Para cada indice e linha na lista criada pelo enumerate
        for i, line in enumerate(e['linhas_do_arquivo']):
            # enumerate criará uma lista a partir do
            # indico 0 ou determinado no segundo parametro da func
            if word in line:  # caso a palavra exista na linha
                # adiciona no array
                occurrences_lines.append({
                    'linha': i + 1
                })
        # caso não ajam ocorrencias
        if len(occurrences_lines) == 0:
            # removerá e retornará o primeiro elemento da fila
            occurrences.pop()
    return occurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
