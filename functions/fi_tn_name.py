# def function_name(context):

    spelling = ""
    language = "void_unk"
    script = "latn"
    name_status = "official"
    nativeness = "void_unk"
    spelling_latn = ""
    display = 1

    list_spelling = []
    list_language = []

    # nimi_suomi
    if 'nimi_suomi' in context['data']:
        spelling = context['data']['nimi_suomi']
        if spelling is not None and spelling != '':
            list_spelling.append(spelling)
            list_language.append("fin")
    
    # nimi_ruotsi
    if 'nimi_ruotsi' in context['data']:
        spelling = context['data']['nimi_ruotsi']
        if spelling is not None and spelling != '':
            list_spelling.append(spelling)
            list_language.append("swe")

    # nimi_inarinsaame
    if 'nimi_inarinsaame' in context['data']:
        spelling = context['data']['nimi_inarinsaame']
        if spelling is not None and spelling != '':
            list_spelling.append(spelling)
            list_language.append("smn")

    # nimi_koltansaame
    if 'nimi_koltansaame' in context['data']:
        spelling = context['data']['nimi_koltansaame']
        if spelling is not None and spelling != '':
            list_spelling.append(spelling)
            list_language.append("sms")

    # nimi_pohjoissaame
    if 'nimi_pohjoissaame' in context['data']:
        spelling = context['data']['nimi_pohjoissaame']
        if spelling is not None and spelling != '':
            list_spelling.append(spelling)
            list_language.append("sme")

    name_list = []
    
    for spelling in list_spelling:
        ind = list_spelling.index(spelling)
        language = list_language[ind]
        if spelling != "" and spelling is not None :  
            spelling = spelling.replace('\"', '')
            spelling = spelling.replace('"', '') 
            spelling_latn = spelling   
            name_list.append({
                "spelling": spelling,
                "language": language,
                "script": script,
                "name_status": name_status,
                "nativeness": nativeness,
                "spelling_latn": spelling_latn,
                "display": display
            })
           
    return name_list
