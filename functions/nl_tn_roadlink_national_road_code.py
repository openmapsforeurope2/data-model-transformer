# def function_name(context):
    # Les valeurs possibles pour condition_of_facility sont:
    # 'disused', 'functional', 'projected', 'under_construction', 'decommissioned'

    # Planned (In ontwerp), Under construction (In uitvoering), In use (In gebruik),
    # Out of use(Niet meer in gebruik), Unknown (Onbekend)
    awegnummer = context['data']['awegnummer']
    nwegnummer = context['data']['nwegnummer']


    if awegnummer != "" and awegnummer is not None:
        return awegnummer

    if nwegnummer != "" and nwegnummer is not None:
        return nwegnummer

    return "void_unk"