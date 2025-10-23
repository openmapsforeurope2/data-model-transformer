# def function_name(context):
    # Les valeurs possibles pour condition_of_facility sont:
    # 'disused', 'functional', 'projected', 'under_construction', 'decommissioned'

    # Sans valeur | En construction | En projet | En service
    etat = context['data']['etat_de_l_objet']

    if etat == "En construction":
        return "under_construction"

    if etat == "En projet":
        return "projected"

    if etat == "En service":
        return "functional"

    if etat == "Non exploité":
        return "disused"

    return "void_unk"