# def function_name(context):
    # Les valeurs possibles pour form_of_way sont:
    # 'bicycle_road', 'dual_carriage_way', 'enclosed_traffic_area', 'entrance_or_exit_car_park', 
    # 'entrance_or_exit_service', 'freeway', 'motorway', 
    # 'pedestrian_zone', 'roundabout', 'service_road', 'single_carriage_way', 
    # 'slip_road', 'tractor', 'traffic_square', 'walkway'

    # Autoroute / Bretelle d’accès / Route principale / Route secondaire 
    # / Route de liaison / Route locale / Route à restriction de circulation / Pas applicable
    roadstatus = context['data']['roadstatus']

    # boolean
    sepcarrway = context['data']['sepcarrway']

    if roadstatus == "Autoroute":
        return "motorway"
    if roadstatus == "Bretelle d’accès":
        return "slip_road"
    if sepcarrway:
        return "dual_carriage_way"
        
    return "single_carriage_way"

    # différence 'freeway', 'motorway', ?
    # date de changement ?
