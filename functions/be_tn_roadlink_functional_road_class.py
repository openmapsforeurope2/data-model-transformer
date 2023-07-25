# def function_name(context):
    # Les valeurs possibles pour functional_road_class sont:
    # 'main_road', 'first_class', 'second_class', 'third_class', 'fourth_class',
    # 'fifth_class', 'sixth_class', 'seventh_class', 'eighth_class', 'ninth_class'

    # Autoroute / Bretelle d’accès / Route principale / Route secondaire 
    # / Route de liaison / Route locale / Route à restriction de circulation / Pas applicable
    roadstatus = context['data']['roadstatus']

    if roadstatus == 1:
        return "main_road"
    
    if roadstatus == 3:
        return "first_class"

    if roadstatus == 4:
        return "second_class"

    if roadstatus == 5:
        return "third_class"

    if roadstatus == 6:
        return "fourth_class"
    
    return ""