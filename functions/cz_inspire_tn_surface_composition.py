# def function_name(context):
        
    surface_composition = ""

    if 'ome2_surface_composition_surfacecomposition' in context['data']:
        surface_composition = str.lower(context['data']['ome2_surface_composition_surfacecomposition'])

    if surface_composition is None or surface_composition == '':
        return "void_unk"

    # If a link is provided in the attribute, we keep the last part only
    if surface_composition.startswith("http"): 
        pos = str.rfind("surface_composition", "/")
        if pos == -1:
            pos = str.rfind("surface_composition", "\\")
        if pos != -1:                                   
            surface_composition = surface_composition[pos+1]
    
    
    match surface_composition:
        case "concrete":
            return "concrete"
        case "grass":
            return "grass"
        case "asphalt":
            return "asphalt"
        case _:
            return "void_unk"
    