# def function_name(context):
 # Les valeurs possibles pour condition_of_facility sont:
    # 'disused', 'functional', 'projected', 'under_construction', 'decommissioned'

    # 1-Operational / 2-Under construction / 3-Out of use/ 999-Not applicable
    opstate = context['data']['opstate']

    if opstate == 1:
        return "functional"

    if opstate == 2: 
        return "under_construction"

    if opstate == 3:
        return "disused"

    return ""
    