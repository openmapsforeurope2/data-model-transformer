# def function_name(context):

    verkehr = context['data']['verkehrsbeschraenkung']
    richtung = context['data']['richtungsgetrennt']
    objektart = context['data']['objektart']
    kreisel = context['data']['kreisel']

    if kreisel == "Wahr":
        return "roundabout"

    if verkehr.startswith("Radweg"): # Radweg / Radweg and Fussweg
        return "bicycle_road"

    if verkehr.startswith("Fuss"): # Fussgängerzone / Fussweg
        return "pedestrian_zone"
    
    if objektart == 'Ausfahrt' or objektart == 'Einfahrt' or objektart == 'Zufahrt' :
        return "slip_road"
    
    if objektart == 'Dienstzufahrt':
        return "service_road"

    if objektart == 'Autobahn':
        return "motorway"

    if objektart == 'Raststaette':
        return "enclosed_traffic_area"

    if objektart == 'Autostrasse':
        return "freeway"
    
    if objektart in ["10m Strasse",'8m Strasse']:
        return "void_single_or_dual_carriage_way"

    if objektart in ['6m Strasse','4m Strasse','3m Strasse']:
        return "single_carriage_way"
 
    if objektart == 'Platz':
        return "traffic_square"

    if objektart == '2m Weg':
        return "tractor_road"

    if objektart == '1m Weg' or objektart == '1m Wegfragment' or objektart == '2m Wegfragment' or objektart == 'Markierte Spur':
        return "walkway"

    if objektart == 'Provisorium':
        return "void_bicycle_or_pedetrian"
    
    return "void_unk"
