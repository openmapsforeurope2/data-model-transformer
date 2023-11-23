# def function_name(context):
    
    nature = context['data']['nature']

    if nature == "Aérodrome" or nature == "Altiport":
        return "aerodrome_only"

    if nature == "Héliport":
        return "heliport_only"

    return "void_unk"