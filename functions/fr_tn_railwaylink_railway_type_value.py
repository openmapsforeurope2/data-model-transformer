# def function_name(context):
    # Les valeurs possibles pour type sont:
    # 'cog_railway', 'funicular', 'magnetic_levitation', 'metro', 'monorail', 'suspended_rail', 'train', 'tramway'

    # Funiculaire ou crémaillère | LGV | Métro | Sans objet | Tramway | Voie de service | Voie ferrée principale
    nature = context['data']['nature']

    if nature == "Funiculaire ou crémaillère":
        return "funicular"

    if nature in ["LGV", "Voie ferrée principale"]:
        return "main_line_train"

    if nature == "Voie de service":
        return "branch_line_train" 

    if nature == "Métro":
        return "metro"

    if nature == "Tramway":
        return "tramway"

    return "void_unk"