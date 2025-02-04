# def function_name(context):
    # Les valeurs possibles pour type sont:
    # 'cog_railway', 'funicular', 'magnetic_levitation', 'metro', 'monorail', 'suspended_rail', 'train', 'tramway'

    # Funiculaire ou crémaillère | LGV | Métro | Sans objet | Tramway | Voie de service | Voie ferrée principale
    nature = context['data']['nature_detaillee']

    if nature == '' or nature is None:
        return "void_unk"

    nature = str.lower(nature)

    if nature == "brise-lames":
        return "breakwater"

    if nature == "epi" or nature == "épi":
        return "groin"

    if nature == "pêche au carrelet":
        return "recreational_pier"

    if nature == "jetée de dérivation":
        return "training_wall"

    if nature == "digue":
        return "seawall"

    return "void_quay"