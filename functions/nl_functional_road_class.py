# def function_name(context):
    # Les valeurs possibles pour functional_road_class sont:
    # 'main_road', 'first_class', 'second_class', 'third_class', 'fourth_class',
    # 'fifth_class', 'sixth_class', 'seventh_class', 'eighth_class', 'ninth_class'

    # Road-type:
    # Highway (Autosnelweg), Main road (Hoofdweg), Regional road (Regionale weg), Local road (Lokale weg), 
    # Street (Straat), Runway (Start/landingsbaan), PlatformOther road (Overige weg), Unknown (Onbekend)
    typeweg = context['data']['typeweg']

    if typeweg in ["Autosnelweg", "Hoofdweg"]:
        return "main_road"
    
    if typeweg == "Regionale weg":
        return "first_class"

    if typeweg == "Lokale weg":
        return "second_class"

    if typeweg == "Straat":
        return "third_class"

    return "fourth_class"