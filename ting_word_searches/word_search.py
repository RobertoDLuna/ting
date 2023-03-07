def exists_word(word, instance):
    # array de ocorrencias
    occurrences = []
    # para cada indice da lista
    for i in range(len(instance)):
        item = instance.search(i)
        found_occurrences = []  # array para adição de ocorrencias encontradas

        # para cada elemento e linha criada pelo enumerate
        for e, line in enumerate(item["linhas_do_arquivo"], start=1):
            # usando caixa baixa para case insensitive
            # Se existir a palavra na linha
            if word.lower() in line.lower():
                # adiciona no array
                found_occurrences.append({"linha": e})
        # se as ocorrencias encontradas forem =! de 0
        # adiciona nas ocorrencias
        if found_occurrences:
            occurrences.append({
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": found_occurrences
            })

    return occurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
