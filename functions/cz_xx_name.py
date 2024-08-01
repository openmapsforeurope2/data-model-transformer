# def function_name(context):

    if 'text' in context['data']:
        name = context['data']['text']
    else:
        name = ""

    print ("name1 = " + name)

    if 'language' in context['data']:
        language = context['data']['language']
    else:
        language = "void_unk"

    name_list = []
    
    if name != "" and name is not None :
        name = name.replace('\"', '')
        name = name.replace('"', '')
        print ("name2 = " + name)
        name_list.append({
            "spelling": name,
            "language": language,
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": name,
            "display": 1
        })
    
    print (name_list)
    
    return name_list