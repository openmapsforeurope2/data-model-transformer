# def function_name(context):
        
    surface_composition = ""

    if 'ome2_surface_composition_surfacecomposition' in context['data']:
        surface_composition = context['data']['ome2_surface_composition_surfacecomposition']

    if surface_composition is None or surface_composition == '':
        return "void_unk"
    else:
        surface_composition = str.lower(surface_composition)

    # If a link is provided in the attribute, we keep the last part only
    if surface_composition.startswith("http"): 
        pos = str.rfind("surface_composition", "/")
        if pos == -1:
            pos = str.rfind("surface_composition", "\\")
        if pos != -1:                                   
            surface_composition = surface_composition[pos+1]
    
    
    if surface_composition != "" and surface_composition is not None:
        return surface_composition
    else:
        return "void_unk"
    