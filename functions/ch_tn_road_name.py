# def function_name(context):

    if 'ome2_road_name' in context['data']:
        name_array = context['data']['ome2_road_name']
    else:
        name_array = []

    print(name_array)
        
    name_list = []

    if name_array != [] :
        for name in name_array:
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