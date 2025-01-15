# def function_name(context):

    cof_source = ""

    if 'conditionooffacility' in context['data']:
        cof_source = context['data']['conditionooffacility']

    if cof_source is None or cof_source == '':
        return "void_unk"
    else:
        cof_source = str.lower(cof_source)

    if cof_source == "underconstruction":
        return "under_construction"

    if cof_source == "projected":
        return "projected"

    if cof_source == "functional":
        return "functional"

    return "void_unk"