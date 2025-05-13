# def function_name(context):
    
    origin = ""

    if 'origin' in context['data']:
        origin = context['data']['origin']
    if 'ome2_watercourse_origin' in context['data']:
        origin = context['data']['ome2_watercourse_origin']

    if origin is None or origin == '':
        return "void_unk"
    else:
        origin = str.lower(origin) 

    # If a link is provided in the attribute, we keep the last part only
    if origin.startswith("http"): 
        pos = str.rfind(origin, "/")
        if pos == -1:
            pos = str.rfind(origin, "\\")
        if pos != -1:                                   
            origin = str.lower(origin[pos+1:])

    # Other cases
    if origin == "manmade":
        return "man_made"

    if origin == "natural":
        return origin

    return "void_unk"