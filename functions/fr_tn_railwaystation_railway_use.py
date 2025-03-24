# def function_name(context):
    # Les valeurs possibles pour type sont:
    # 'cargo', 'passenger', 'mixed', 'car_shuttle'

    # 'Arrêt voyageurs', 'Gare fret uniquement', 'Gare voyageurs et fret', 'Gare voyageurs uniquement', 'Station de métro', 'Station de tramway'
    nature = context['data']['nature']

    if nature in ["Arrêt voyageurs", "Gare voyageurs uniquement", "Station de métro", "Station de tramway"]:
        return "passengers"

    if nature == "Gare fret uniquement":
        return "cargo"

    if nature == "Gare voyageurs et fret":
        return "mixed"

    # if nature == "Gare routière":
    #     return "car_shuttle"

    return "void_unk"