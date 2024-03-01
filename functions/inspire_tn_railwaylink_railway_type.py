# def function_name(context):
    
    type = ""

    if 'type' in context['data']:
        type = str.lower(context['data']['type'])

    if type != "":
        return type

    return "void_unk"