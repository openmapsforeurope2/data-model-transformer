# -*- coding: utf-8 -*-
# def function_name(context):
    
    left_name = context['data']['nom_collaboratif_gauche']
    right_name = context['data']['nom_collaboratif_droite']

    nom = ""
    
    if left_name == right_name:
        if left_name is None or left_name == "":
            nom = "void"
        else:
            nom = left_name
    
    if left_name != "" and left_name is not None and left_name.lower() != "null" and right_name != "" and right_name is not None and right_name.lower() != "null":
        geo_name = "{0}/{1}".format(left_name, right_name)
        nom = geo_name

    if right_name != "" and right_name is not None and right_name.lower() != "null":
        nom = right_name

    if left_name != "" and left_name is not None and left_name.lower() != "null":
        nom = left_name

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


    name_list = []
    
    if nom != "" and nom is not None and nom != "void" :
        nom = nom.replace('\"', '')
        nom = nom.replace('"', '')
        name_list.append({
            "spelling": nom,
            "language": "fre",
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": nom,
            "country": country,
            "display": 1
        })
    
    return name_list
    
