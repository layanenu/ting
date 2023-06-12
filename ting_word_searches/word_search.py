def exists_word(word, instance):
    search_results = []

    queue_list = list(instance.queue)

    for index_one, content in enumerate(queue_list):
        line_list = content["linhas_do_arquivo"]

        occurrences = []
        for index_two, line in enumerate(line_list):
            if word.lower() in line.lower():
                occurrences.append({"linha": index_two + 1})

        if occurrences:
            search_results.append({
                "palavra": word,
                "arquivo": content["nome_do_arquivo"],
                "ocorrencias": occurrences,
            })

    return search_results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
