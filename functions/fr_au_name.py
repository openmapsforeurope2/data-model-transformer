# def function_name(context):

    nom_officiel = context['data']['nom_officiel']
    name_list = []
    
    country = "void_unk"
    territoire = context['data']['gcms_territoire']

    if territoire == "FXX":
        country = "fr"
    if territoire == "GLP":
        country = "gp"
    if territoire == "GUF":
        country = "gf"
    if territoire == "H_T":
        country = "ht"
    if territoire == "MTQ":
        country = "mq"
    if territoire == "MYT":
        country = "yt"
    if territoire == "REU":
        country = "re"
    if territoire == "SPM":
        country = "pm"

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
            "country": country,
            "display": 1
        })
    
    return name_list
