# def function_name(context):
    # Les valeurs possibles pour condition_of_facility sont:
    # 'disused', 'functional', 'projected', 'under_construction', 'decommissioned'

    # Sans valeur | En construction | En projet | En service
    access = context['data']['etat_de_l_objet']

    if access == "En construction":
        return "under_construction"

    if access == "En projet ":
        return "projected"

    return "functional"