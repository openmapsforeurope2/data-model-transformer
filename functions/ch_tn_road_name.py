# def function_name(context):

    if 'ome2_road_name' in context['data']:
        name_array = context['data']['ome2_road_name']
    else:
        name_array = []
        
    name_list = []

    if name_array != [] and name_array is not None:
        for name in name_array:
            if name != "":
                name = name.replace('\"', '')
                name = name.replace('"', '')
                name_list.append({
                    "spelling": name,
                    "language": "void_unk",
                    "script": "latn",
                    "name_status": "official",
                    "nativeness": "endonym",
                    "spelling_latn": name,
                    "display": 1
                })
    
    return name_list