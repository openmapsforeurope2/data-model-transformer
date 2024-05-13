# def function_name(context):

    verkehr = context['data']['verkehrsbeschraenkung']
    richtung = context['data']['richtungsgetrennt']
    objektart = context['data']['objektart']
    kreisel = context['data']['kreisel']

    if objektart == 'Autobahn':
        return "freeway"
    
    if kreisel == "Wahr":
        return "roundabout"

    if verkehr.startswith("Radweg"): # Radweg / Radweg and Fussweg
        return "bicycle_road"

    if verkehr.startswith("Fuss"): # Fussgängerzone / Fussweg
        return "pedestrian_zone"
 
    if richtung == "Wahr":
        return "single_carriage_way"
    
    return "void_unk"
