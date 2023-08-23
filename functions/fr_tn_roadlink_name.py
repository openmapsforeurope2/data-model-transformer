# -*- coding: utf-8 -*-
# def function_name(context):
    
    left_name = context['data']['nom_1_gauche']
    right_name = context['data']['nom_1_droite']

    if left_name == right_name:
        if left_name is None or left_name == "":
            return "void"
        else:
            return left_name
    
    if left_name != "" and left_name is not None and left_name.lower() != "null" and right_name != "" and right_name is not None and right_name.lower() != "null":
        geo_name = "{0}/{1}".format(left_name, right_name)
        return geo_name

    if right_name != "" and right_name is not None and right_name.lower() != "null":
        return right_name

    if left_name != "" and left_name is not None and left_name.lower() != "null":
        return left_name

    return "void"
