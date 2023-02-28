# def function_name(context):
    # Les valeurs possibles pour type sont:
    # 'bus_station', 'parking', 'rest_area', 'toll'

    nature = context['data']['nature']

    if nature == "Parking":
        return "parking"

    if nature == "Péage":
        return "toll"

    if nature == "Gare routière":
        return "bus_station"

    if nature == "Aire de repos ou de service":
        return "rest_area"

    return ""