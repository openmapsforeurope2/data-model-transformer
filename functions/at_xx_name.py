# def function_name(context):

    if 'name' in context['data']:
        name = context['data']['name']
    else:
        name = ""
    name_list = []
    
    if name != "" and name is not None :
        name = name.replace('\"', '')
        name = name.replace('"', '')
        name_list.append({
            "spelling": name,
            "language": "ger",
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": name,
            "display": 1
        })
    
    return name_list
