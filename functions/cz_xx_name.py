# def function_name(context):

    if 'text' in context['data']:
        name = context['data']['text']
    else:
        name = ""

    if 'language' in context['data']:
        language = context['data']['language']
    else:
        language = "void_unk"

    name_list = []
    
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
    
    return name_list