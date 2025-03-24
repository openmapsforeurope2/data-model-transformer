# def function_name(context):

    if 'name' in context['data']:
        name = context['data']['name']
    elif 'name_bauten' in context['data']:
        name = context['data']['name_bauten']
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
    
    if 'variantname' in context['data']:
        variantname = context['data']['variantname']
    
        if variantname != "" and variantname is not None and variantname != "periodisch" :
            variantname = variantname.replace('\"', '')
            variantname = variantname.replace('"', '')
            
            nativeness = "void_unk"
            if variantname == "Fertö":
                nativeness = "exonym"

            name_list.append({
                "spelling": variantname,
                "language": "ger",
                "script": "latn",
                "name_status": "other",
                "nativeness": nativeness,
                "spelling_latn": variantname,
                "display": 0
            })

    return name_list
