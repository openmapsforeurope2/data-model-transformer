# def function_name(context):

    spelling = ""
    list_spelling = []
    label = ""

    # nimi_pohjoissaame
    if 'nimi_pohjoissaame' in context['data']:
        spelling = context['data']['nimi_pohjoissaame']
        if spelling is not None and spelling != '':
            list_spelling.append(spelling)

    # nimi_koltansaame
    if 'nimi_koltansaame' in context['data']:
        spelling = context['data']['nimi_koltansaame']
        if spelling is not None and spelling != '':
            list_spelling.append(spelling)

    # nimi_inarinsaame
    if 'nimi_inarinsaame' in context['data']:
        spelling = context['data']['nimi_inarinsaame']
        if spelling is not None and spelling != '':
            list_spelling.append(spelling)

    # nimi_ruotsi
    if 'nimi_ruotsi' in context['data']:
        spelling = context['data']['nimi_ruotsi']
        if spelling is not None and spelling != '':
            list_spelling.append(spelling)

    # nimi_suomi
    if 'nimi_suomi' in context['data']:
        spelling = context['data']['nimi_suomi']
        if spelling is not None and spelling != '':
            list_spelling.append(spelling)


    for spelling in list_spelling:
        label = label + '#' + spelling

    label = label[1:]

    return label       