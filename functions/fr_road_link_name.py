# -*- coding: utf-8 -*-
# def function_name(context):
    
    left_name = context['data']['nom_1_gauche']
    right_name = context['data']['nom_1_droite']


    if left_name == right_name:
        return left_name
    
    if left_name != "" and right_name != "":
        geo_name = "{0}#{1}".format(left_name, right_name)
        return geo_name

    if right_name != "":
        return right_name

    if left_name != "":
        return left_name

    return ""