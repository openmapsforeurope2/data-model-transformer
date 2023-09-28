# def function_name(context):

    name = context['data']['naam']
    name_list = []
    
    if name != "" and name is not None :      
        name_list.append({
            "spelling": name,
            "language": "dut",
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym"
        })
           
    return name_list
