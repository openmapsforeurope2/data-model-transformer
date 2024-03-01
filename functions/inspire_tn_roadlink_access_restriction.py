# -*- coding: utf-8 -*-
# def function_name(context):

    access = ""
    
    if 'restriction' in context['data']:
        access = str.lower(context['data']['restriction'])

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
