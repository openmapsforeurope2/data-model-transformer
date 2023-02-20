# def function_name(context):
    # Les valeurs possibles pour functional_road_class sont:
    # 'main_road', 'first_class', 'second_class', 'third_class', 'fourth_class',
    # 'fifth_class', 'sixth_class', 'seventh_class', 'eighth_class', 'ninth_class'

    # Autoroute / Bretelle d’accès / Route principale / Route secondaire 
    # / Route de liaison / Route locale / Route à restriction de circulation / Pas applicable
    roadstatus = context['data']['roadstatus']

    if roadstatus == "Autoroute":
        return "main_road"
    
    if roadstatus == "Route principale":
        return "first_class"

    if roadstatus == "Route secondaire":
        return "second_class"
    
    return "third_class"