# def function_name(context):

    cof_source = ""

    if 'conditionooffacility' in context['data']:
        cof_source = str.lower(context['data']['conditionooffacility'])

    if cof_source == "underconstruction":
        return "under_construction"

    if cof_source == "projected":
        return "projected"

    if cof_source == "functional":
        return "functional"

    return "void_unk"