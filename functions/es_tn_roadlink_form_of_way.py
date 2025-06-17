# def function_name(context):

    clase = context['data']['clase']
    tipovehic = context['data']['tipovehic']
    tipo_tramo = context['data']['tipo_tramo']
    calzada = context['data']['calzada']

    if tipovehic == 100: 
        return "pedestrian_zone"

    if tipo_tramo == 4:
        return "roundabout"

    if tipo_tramo == 3:
        return "service_road"

    if clase == 1002 and tipo_tramo != 2:
        return "freeway"

    if clase in [1001, 1002] and tipo_tramo != 2:
        return "motorway"

    if clase in [1003, 1005, 2000, 2001] and calzada == 2:
        return "dual_carriage_way"
    
    if clase in [1003, 2000, 2001] and calzada == 1:
        return "single_carriage_way"

    if clase in [1001, 1002] and tipo_tramo == 2:
        return "slip_road"

    if clase == 1004: 
        return "bicycle_road"

    if clase in [3001, 3002]:
        return "walkway"
    
    return "void_unk"
