# def function_name(context):
    # Les valeurs possibles pour form_of_way sont:
    # 'bicycle_road', 'dual_carriage_way', 'enclosed_traffic_area', 'entrance_or_exit_car_park', 
    # 'entrance_or_exit_service', 'freeway', 'motorway', 
    # 'pedestrian_zone', 'roundabout', 'service_road', 'single_carriage_way', 
    # 'slip_road', 'tractor', 'traffic_square', 'walkway'

    # Bac ou liaison maritime | Bretelle | Chemin | Escalier | Rond-point | Route à 1 chaussée |
    # Route à 2 chaussées | Route empierrée | Sentier | Type autoroutier

    if 'classe_de_largeur' in context['data']:
        largeur = context['data']['classe_de_largeur']
    else:
        largeur == ""

    if largeur == "Entre 0 et 5 m" or largeur == "Entre 0 et 15 m":
        return "0"

    if largeur == "Entre 5 et 15 m":
        return "5"

    if largeur == "Entre 15 et 50 m":
        return "15"

    if largeur == "Entre 50 et 250 m" or largeur == "Plus de 50 m":
        return "50"  
 
    if largeur == "Entre 250 et 1250 m":
        return "250"

    if largeur == "Plus de 1250 m":
        return "1250"

    return "-32768"
