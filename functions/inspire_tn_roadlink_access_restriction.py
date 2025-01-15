# -*- coding: utf-8 -*-
# def function_name(context):

    access = ""
    
    if 'restriction' in context['data']:
        access = context['data']['restriction']

    if access is None or access == '':
        return "void_unk"
    else:
        access = str.lower(access) 

    if access == "physicallyimpossible":
        return "physically_impossible"
    
    if access == "toll":
        return "toll"

    if access == "private":
        return "private"

    if access == "seasonal":
        return "seasonal"

    if access == "publicaccess":
        return "public_access"

    return "void_unk"
