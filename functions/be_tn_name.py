# def function_name(context):

    linename = context['data']['linename']
    name_list = []
    
    if linename != "" :
        name_list.append({
            "spelling": linename,
            "language": "dut#fre",
            "script": "latn",
            "name_status": "standardised",
            "nativeness": "endonym",
            "spelling_latn": linename,
            "display": 1
        })
    
    return name_list
