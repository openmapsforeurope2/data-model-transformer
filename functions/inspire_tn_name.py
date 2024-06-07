# def function_name(context):

    name = ""
    language = "void_unk"
    script = "latn"
    name_status = "void_unk"
    nativeness = "endonym"
    spelling_latn = ""
    display = 1

    if 'streetname' in context['data']:
        name = context['data']['streetname']
    elif 'spellingofname_text' in context['data']:
        name = context['data']['spellingofname_text']
    
    name_list = []
    
    if name != "" and name is not None :  
        name = name.replace('\"', '')
        name = name.replace('"', '')    
        name_list.append({
            "spelling": name,
            "language": language,
            "script": script,
            "name_status": name_status,
            "nativeness": nativeness,
            "spelling_latn": spelling_latn,
            "display": display
        })
           
    return name_list
