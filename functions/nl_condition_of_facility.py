# def function_name(context):
    # Les valeurs possibles pour condition_of_facility sont:
    # 'disused', 'functional', 'projected', 'under_construction', 'decommissioned'

    # Planned (In ontwerp), Under construction (In uitvoering), In use (In gebruik),
    # Out of use(Niet meer in gebruik), Unknown (Onbekend)
    status = context['data']['status']

    if status == "In uitvoering":
        return "under_construction"

    if status == "In ontwerp":
        return "projected"

    if status == "In gebruik":
        return "functional"

    if status == "Niet meer in gebruik":
        return "disused"

    return "functional"