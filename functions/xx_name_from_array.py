# def function_name(context):

    language = 'void_unk'    

    if 'ome2_road_name' in context['data']:
        name_array = context['data']['ome2_road_name']
    if 'ome2_toponyme_troncon_hydrographique' in context['data']:
        name_array = context['data']['ome2_toponyme_troncon_hydrographique']
        language = 'fre'
    else:
        name_array = []
        
    name_list = []

    if name_array != [] and name_array is not None:
        for name in name_array:
            if name != "" and name is not None:
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
    
    return name_list