# def function_name(context):
        
    position = ""

    if 'verticalposition' in context['data']:
        position = str.lower(context['data']['verticalposition'])

    if position == "underground":
        return "underground"

    if position == "suspendedorelevated":
        return "suspended_or_elevated"

    if position == "ongroundsurface":
        return "on_ground_surface"

    return "void_unk"