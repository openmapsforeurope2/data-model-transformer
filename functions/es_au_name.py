# def function_name(context):

    name = ''
    name2 = ''

    language = 'void_unk'
    language2 = 'void_unk'

    # Retrieve name values
    ## Case 1 : Iberic peninsula + Baleares
    if 'ome2_identificador_geografico' in context['data']:
        name = context['data']['ome2_identificador_geografico']
        if 'ome2_nombre_alternativo_2' in context['data']:
            name2 = context['data']['ome2_nombre_alternativo_2']
    ## Case 2 : Canary islands
    elif 'nameunit' in context['data']:
        name = context['data']['nameunit']

    # Retrieve language values
    ## Case 1 : Iberic peninsula + Baleares
    if 'ome2_idioma_idg' in context['data']:
        language = context['data']['ome2_idioma_idg']
        if 'ome2_idioma_alternativo_2' in context['data']:
            language2 = context['data']['ome2_idioma_alternativo_2']
    ## Case 2 : Canary islands
    elif 'nameunit' in context['data']:
        language = "spa"

    name_list = []

    # Main name
    if name != "" and name is not None :
        name = name.replace('\"', '')
        name = name.replace('"', '')
        name_list.append({
            "spelling": name,
            "language": language,
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": name,
            "display": 1
        })
    
    # Alternative name
    if name2 != "" and name2 is not None:
        name2 = name2.replace('\"', '')
        name2 = name2.replace('"', '')

        name_list.append({
            "spelling": name2,
            "language": language2,
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": name2,
            "display": 2
        })

    return name_list
