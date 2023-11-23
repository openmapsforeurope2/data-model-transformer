# def function_name(context):

    if 'naamofficieel' in context['data']:
        official_name = context['data']['naamofficieel']
    else:
        official_name = ""
    
    if 'naamnl' in context['data']:
        nl_name = context['data']['naamnl']

    elif 'naam' in context['data']:
        nl_name = context['data']['naam']
        
    else:
        nl_name = ""

    if 'naamfries' in context['data']:  
        fries_name = context['data']['naamfries']
    else:
        fries_name = ""
    name_list = []
    
    if official_name != "" and official_name is not None:
        if official_name == nl_name:
            name_list.append({
                "spelling": official_name.replace('"', ''),
                "language": "dut",
                "script": "latn",
                "name_status": "official",
                "nativeness": "endonym",
                "spelling_latn": official_name.replace('"', ''),
                "display": 1
            })
            if fries_name != "" and fries_name is not None:
                name_list.append({
                "spelling": fries_name.replace('"', ''),
                "language": "fry",
                "script": "latn",
                "name_status": "official",
                "nativeness": "endonym",
                "spelling_latn": fries_name.replace('"', ''),
                "display": 0
            })
                
        else:
            name_list.append({
                "spelling": official_name.replace('"', ''),
                "language": "fry",
                "script": "latn",
                "name_status": "official",
                "nativeness": "endonym",
                "spelling_latn": official_name.replace('"', ''),
                "display": 1
            })
            if nl_name != "" and nl_name is not None:
                name_list.append({
                "spelling": nl_name.replace('"', ''),
                "language": "dut",
                "script": "latn",
                "name_status": "official",
                "nativeness": "endonym",
                "spelling_latn": nl_name.replace('"', ''),
                "display": 0
            })
    
    else:
        if nl_name != "" and nl_name is not None:
            name_list.append({
                "spelling": nl_name.replace('"', ''),
                "language": "dut",
                "script": "latin",
                "name_status": "official",
                "nativeness": "endonym",
                "spelling_latn": nl_name.replace('"', ''),
                "display": 1
            })
        if fries_name != "" and fries_name is not None:
            name_list.append({
                "spelling": fries_name.replace('"', ''),
                "language": "fry",
                "script": "latin",
                "name_status": "official",
                "nativeness": "endonym",
                "spelling_latn": fries_name.replace('"', ''),
                "display": 2
            })

    return name_list
