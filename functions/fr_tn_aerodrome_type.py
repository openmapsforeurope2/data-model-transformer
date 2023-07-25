# def function_name(context):
    
    nature = context['data']['nature']

    if nature == "Aérodrome":
        return "aerodrome_only"

    if nature == "Héliport":
        return "heliport_only"

    if nature == "Altiport" or nature == "Hydrobase":
        return "landing_site"

    return "void"