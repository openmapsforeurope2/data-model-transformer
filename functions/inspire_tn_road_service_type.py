# def function_name(context):
    # Les valeurs possibles pour type sont:
    # 'bus_station', 'parking', 'rest_area', 'toll'

    type = ""

    if 'type' in context['data']:
        type = str.lower(context['data']['type'])    

    if type == "parking":
        return "parking"

    if type == "toll":
        return "toll"

    if type == "busstation":
        return "bus_station"

    if type == "restarea":
        return "rest_area"

    if type == "electricalvehicalchargingstation":
        return "electric_car_loading_stations"

    return "void_unk"