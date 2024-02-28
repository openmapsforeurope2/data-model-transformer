# def function_name(context):

    name = context['data']['text']
    language = context['data']['language']
    name_list = []
    
    if name != "" and name is not None :
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
