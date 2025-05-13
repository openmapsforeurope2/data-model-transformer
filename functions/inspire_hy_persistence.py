# def function_name(context):
    
    persistence = ""

    if 'persistence' in context['data']:
        persistence = context['data']['persistence']
    elif 'ome2_watercourse_persistence' in context['data']:
        persistence = context['data']['ome2_watercourse_persistence']
        

    if persistence is None or persistence == '':
        return "void_unk"
    else:
        persistence = str.lower(persistence) 

    # If a link is provided in the attribute, we keep the last part only
    if persistence.startswith("http"): 
        pos = str.rfind(persistence, "/")
        if pos == -1:
            pos = str.rfind(persistence, "\\")
        if pos != -1:                                   
            persistence = str.lower(persistence[pos+1:])

    # Other cases
    if persistence != "" and persistence is not None:
        return persistence

    return "void_unk"