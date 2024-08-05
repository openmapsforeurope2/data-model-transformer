# def function_name(context):

    if 'strassenname' in context['data']:
        name = context['data']['strassenname']
    else:
        name = ""

    name_list = []
    
    if name != "" and name is not None :
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