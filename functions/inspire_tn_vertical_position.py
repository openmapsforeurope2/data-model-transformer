# def function_name(context):
        
    position = ""

    if 'ome2_vertical_position_verticalposition' in context['data']:
        position = context['data']['ome2_vertical_position_verticalposition']
    elif 'verticalposition' in context['data']:
        position = context['data']['verticalposition']

    if position is None or position == '':
        return "void_unk"
    else:
        position = str.lower(position) 

    # If a link is provided in the attribute, we keep the last part only
    if position.startswith("http"): 
        pos = str.rfind(position, "/")
        if pos == -1:
            pos = str.rfind(position, "\\")
        if pos != -1:                                   
            position = str.lower(position[pos+1:])

    if position == "underground":
        return "underground"

    if position == "suspendedorelevated":
        return "suspended_or_elevated"

    if position == "ongroundsurface":
        return "on_ground_surface"

    return "void_unk"