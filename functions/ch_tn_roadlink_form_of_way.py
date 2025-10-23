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
    
    if objektart == 'Autostrasse':
        return "freeway"

    if objektart == 'Raststaette':
        return "entrance_or_exit_service"
    
    if objektart in ["10m Strasse",'8m Strasse','6m Strasse','4m Strasse','3m Strasse']:
        if richtung == 'Wahr':
            return 'dual_carriage_way'
        else:
            return 'single_carriage_way'
 
    if objektart == 'Platz':
        return "traffic_square"

    if objektart == '2m Weg':
        return "tractor_road"

    if objektart in ['1m Weg', '1m Wegfragment','2m Wegfragment','Markierte Spur']:
        return "walkway"

    if objektart == 'Provisorium':
        return "void_unk"
    
    return "void_unk"
