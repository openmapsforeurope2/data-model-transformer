# def function_name(context):
    # Les valeurs possibles pour form_of_way sont:
    # 'bicycle_road', 'dual_carriage_way', 'enclosed_traffic_area', 'entrance_or_exit_car_park', 
    # 'entrance_or_exit_service', 'freeway', 'motorway', 
    # 'pedestrian_zone', 'roundabout', 'service_road', 'single_carriage_way', 
    # 'slip_road', 'tractor', 'traffic_square', 'walkway'

    # Bac ou liaison maritime | Bretelle | Chemin | Escalier | Rond-point | Route à 1 chaussée |
    # Route à 2 chaussées | Route empierrée | Sentier | Type autoroutier

    nature = context['data']['nature']

    if nature == "Route à 2 chaussées":
        return "dual_carriage_way"

    if nature == "Type autoroutier":
        return "motorway"

    if nature == "Rond-point":
        return "roundabout"

    if nature == "Bretelle":
        return "slip_road"  
 
    if nature in ["Route à 1 chaussée", "Route empierrée"]:
        return "single_carriage_way"

    if nature in ["Sentier","Escalier"]:
        return "walkway"

    if nature == "Chemin":
        return "tractor_road"
    
    return "void_unk"
