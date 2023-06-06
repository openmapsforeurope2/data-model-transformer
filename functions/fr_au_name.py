# def function_name(context):

    nom_officiel = context['data']['nom_officiel']
    name_list = []
    
    if nom_officiel != "" :
        nom_officiel = nom_officiel.replace('"', '\"')
        name_list.append({
            "spelling": nom_officiel,
            "language": "fre",
            "script": "latin",
            "name_status": "official",
            "nativeness": "endonym"
        })
    
    return name_list
