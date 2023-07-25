# def function_name(context):

    nom = context['data']['toponyme']
    name_list = []
    
    if nom != "" and nom is not None :
        nom = nom.replace('\"', '')
        nom = nom.replace('"', '')
        name_list.append({
            "spelling": nom,
            "language": "fre",
            "script": "latin",
            "name_status": "official",
            "nativeness": "endonym"
        })
    
    return name_list
