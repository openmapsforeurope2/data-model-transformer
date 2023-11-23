# -*- coding: utf-8 -*-
# def function_name(context):
    
    left_name = context['data']['nom_1_gauche']
    right_name = context['data']['nom_1_droite']

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

    
    name_list = []
    
    if nom != "" and nom is not None and nom != "void" :
        nom = nom.replace('\"', '')
        nom = nom.replace('"', '')
        name_list.append({
            "spelling": nom,
            "language": "fre",
            "script": "latin",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": nom,
            "display": 1
        })
    
    return name_list
    
