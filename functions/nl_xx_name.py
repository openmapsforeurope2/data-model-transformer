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
    
    if official_name != "" :
        if official_name == nl_name:
            name_list.append({
                "spelling": official_name,
                "language": "dut",
                "script": "latn",
                "name_status": "official",
                "nativeness": "endonym"
            })
            if fries_name != "":
                name_list.append({
                "spelling": fries_name,
                "language": "fry",
                "script": "latn",
                "name_status": "official",
                "nativeness": "endonym"
            })
                
        else:
            name_list.append({
                "spelling": official_name,
                "language": "fry",
                "script": "latn",
                "name_status": "official",
                "nativeness": "endonym"
            })
            if nl_name != "":
                name_list.append({
                "spelling": nl_name,
                "language": "dut",
                "script": "latn",
                "name_status": "official",
                "nativeness": "endonym"
            })
    
    else:
        if nl_name != "":
            name_list.append({
                "spelling": official_name,
                "language": "dut",
                "script": "latin",
                "name_status": "official",
                "nativeness": "endonym"
            })
        if fries_name != "":
            name_list.append({
                "spelling": fries_name,
                "language": "fry",
                "script": "latin",
                "name_status": "official",
                "nativeness": "endonym"
            })

    return name_list
