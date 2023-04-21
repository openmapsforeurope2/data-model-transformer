# def function_name(context):

    nameger = context['data']['nameger']
    namefre = context['data']['namefre']
    namedut = context['data']['namedut']
    name_list = []
    
    if nameger != "" :
        name_list.append({
            "spelling": nameger,
            "language": "ger",
            "script": "latin",
            "name_status": "official",
            "nativeness": "endonym"
        })

    if namefre != "" :
        name_list.append({
            "spelling": namefre,
            "language": "fre",
            "script": "latin",
            "name_status": "official",
            "nativeness": "endonym"
        })

    if namedut != "" :
        name_list.append({
            "spelling": namedut,
            "language": "dut",
            "script": "latin",
            "name_status": "official",
            "nativeness": "endonym"
        })
    
    return name_list
