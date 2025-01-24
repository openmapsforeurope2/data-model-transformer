# -*- coding: utf-8 -*-
# def function_name(context):

    form_source = ""

    if 'formofroadnode' in context['data']:
        form_source = context['data']['formofroadnode']

    if form_source is None or form_source == '':
        return "void_unk"
    else:
        form_source = str.lower(form_source) 

    if form_source == "roadservicearea":
        return "road_service_area"

    if form_source == "levelcrossing":
        return "level_crossing"
    
    return "void_unk"