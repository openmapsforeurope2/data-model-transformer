# def function_name(context):
    # Les valeurs possibles pour type sont:
    # 'cog_railway', 'funicular', 'magnetic_levitation', 'metro', 'monorail', 'suspended_rail', 'train', 'tramway'

    # Funiculaire ou crémaillère | LGV | Métro | Sans objet | Tramway | Voie de service | Voie ferrée principale
    nature = context['data']['nature']

    if nature == "Funiculaire ou crémaillère":
        return "funicular"
        # cog_railway = chemin de fer à crémaillère

    if nature in ["LGV", "Voie de service", "Voie ferrée principale"]:
        return "train"

    if nature == "Métro":
        return "metro"

    if nature == "Tramway":
        return "tramway"

    return "train"