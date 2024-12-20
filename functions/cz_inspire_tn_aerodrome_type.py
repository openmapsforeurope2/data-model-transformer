# def function_name(context):
        
    aerodrome_type = ""

    if 'ome2_aerodrome_type_aerodrometype' in context['data']:
        aerodrome_type = str.lower(context['data']['ome2_aerodrome_type_aerodrometype'])

    if aerodrome_type is None or aerodrome_type == '':
        return "void_unk"

    # If a link is provided in the attribute, we keep the last part only
    if aerodrome_type.startswith("http"): 
        pos = str.rfind("aerodrome_type", "/")
        if pos == -1:
            pos = str.rfind("aerodrome_type", "\\")
        if pos != -1:                                   
            aerodrome_type = aerodrome_type[pos+1]
    
    
    match aerodrome_type:
        case "aerodromeheliport":
            return "aerodrome_heliport"
        case "aerodromeonly":
            return "aerodrome_only"
        case "heliportonly":
            return "heliport_only"
        case "landingsite":
            return "landing_site"
        case _:
            return "void_unk"
    