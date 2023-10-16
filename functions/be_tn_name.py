# def function_name(context):

    linename = context['data']['linename']
    name_list = []
    
    if linename != "" :
        name_list.append({
            "spelling": linename,
            "language": "void",
            "script": "latin",
            "name_status": "official",
            "nativeness": "endonym"
        })
    
    return name_list
