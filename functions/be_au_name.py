# def function_name(context):

    nameger = context['data']['nameger']
    namefre = context['data']['namefre']
    namedut = context['data']['namedut']
    name_list = []
    
    if nameger != "" :
        name_list.append({
            "spelling": nameger,
            "language": "ger",
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": nameger,
            "display": 3
        })

    if namefre != "" :
        name_list.append({
            "spelling": namefre,
            "language": "fre",
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": namefre,
            "display": 2
        })

    if namedut != "" :
        name_list.append({
            "spelling": namedut,
            "language": "dut",
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": namedut,
            "display": 1
        })
    
    return name_list
