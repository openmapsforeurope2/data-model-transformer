# def function_name(context):
    # Les valeurs possibles pour condition_of_facility sont:
    # 'disused', 'functional', 'projected', 'under_construction', 'decommissioned'

    # Planned (In ontwerp), Under construction (In uitvoering), In use (In gebruik),
    # Out of use(Niet meer in gebruik), Unknown (Onbekend)
    awegnummer = context['data']['awegnummer']
    nwegnummer = context['data']['nwegnummer']


    if awegnummer != "":
        return awegnummer

    if nwegnummer != "":
        return nwegnummer

    return ""