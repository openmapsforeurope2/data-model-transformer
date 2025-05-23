# def function_name(context):
    # Les valeurs possibles pour type sont:
    # 'bus_station', 'parking', 'rest_area', 'toll'

    type = ""

    if 'type' in context['data']:
        type = context['data']['type']   
    elif 'ome2_road_service_type_type' in context['data']:
        type = context['data']['ome2_road_service_type_type']   

    if type is None or type == '':
        return "void_unk"
    else:
        type = str.lower(type) 

    # If type is provided as a link, we keep only the final part
    if type.startswith("http"): 
        pos = str.rfind(type, "/")
        if pos == -1:
            pos = str.rfind(type, "\\")
        if pos != -1:                                   
            type = str.lower(type[pos+1:])


    if type in ["parking","toll"]:
        return type

    if type == "busstation":
        return "bus_station"

    if type == "restarea":
        return "rest_area"

    if type == "electricalvehicalchargingstation":
        return "electric_car_loading_stations"

    return "void_unk"