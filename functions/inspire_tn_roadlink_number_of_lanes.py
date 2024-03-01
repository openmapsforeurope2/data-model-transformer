# def function_name(context):

    min_max_type = ""
    nb_of_lanes = ""

    if 'minmaxnumberoflanes' in context['data']:
        minmaxnumberoflanes = str.lower(context['data']['minmaxnumberoflanes'])
    
    if 'numberoflanes' in context['data']:
        nb_of_lanes = str(context['data']['numberoflanes'])

    if nb_of_lanes == "" or nb_of_lanes is None:
        return "void_unk"

    if minmaxnumberoflanes is not None and minmaxnumberoflanes != "" and minmaxnumberoflanes != "average":
        return "void_unk"

    return nb_of_lanes