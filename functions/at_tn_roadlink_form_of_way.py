# def function_name(context):
    
    f_code = ""
    kreisverkehr = ""

    if f_code in context['data']:
        f_code = context['data']['f_code']
    if kreisverkehr in context['data']:
        kreisverkehr =  context['data']['kreisverkehr']

    if kreisverkehr == 'Ja':
        return "roundabout"
    
    if f_code == 1112:
        return "entrance_or_exit_service"

    if f_code == 1101 or f_code == 1102:
        return "motorway"

    if f_code == 1111:
        return "service_road"

    if f_code in [1103, 1104, 1105, 1121, 1131]:
        return "single_carriage_way"  
 
    if f_code == 1113:
        return "slip_road"

    if f_code == 1122:
        return "tractor_road"

    if f_code in [1141,1142,1143]:
        return "walkway"
    
    return "void_unk"
