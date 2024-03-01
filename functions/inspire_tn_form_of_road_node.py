# -*- coding: utf-8 -*-
# def function_name(context):

    form_source = ""

    if 'formofroadnode' in context['data']:
        form_source = str.lower(context['data']['formofroadnode'])    

    if form_source == "roadservicearea":
        return "road_service_area"

    if form_source == "levelcrossing":
        return "level_crossing"
    
    return "void_unk"