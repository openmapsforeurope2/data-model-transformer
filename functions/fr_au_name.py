# def function_name(context):

    nom_officiel = context['data']['nom_officiel']
    name_list = []
    
    if nom_officiel != "" :
        nom_officiel = nom_officiel.replace('\"', '')
        nom_officiel = nom_officiel.replace('"', '')
        name_list.append({
            "spelling": nom_officiel,
            "language": "fre",
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": nom_officiel,
            "display": 1
        })
    
    return name_list
