# def function_name(context):

    official_name = context['data']['naamofficieel']
    nl_name = context['data']['naamnl']
    fries_name = context['data']['naamfries']
    name_list = []
    
    if official_name != "" :
        if official_name == nl_name:
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
                
        else:
            name_list.append({
                "spelling": official_name,
                "language": "fry",
                "script": "latin",
                "name_status": "official",
                "nativeness": "endonym"
            })
            if nl_name != "":
                name_list.append({
                "spelling": nl_name,
                "language": "dut",
                "script": "latin",
                "name_status": "official",
                "nativeness": "endonym"
            })
    
    return name_list
