# def function_name(context):

    if 'ome2_toponyme_troncon_hydrographique' in context['data']:
        nom = context['data']['ome2_toponyme_troncon_hydrographique']
    else:
        nom = ""
    name_list = []
    
    if nom != "" and nom is not None :
        nom = nom.replace('\"', '')
        nom = nom.replace('"', '')
        name_list.append({
            "spelling": nom,
            "language": "fre",
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": nom,
            "display": 1
        })
    
    return name_list
