# def function_name(context):

    minmaxnumberoflanes = ""
    nb_of_lanes = ""

    if 'minmaxnumberoflanes' in context['data']:
        minmaxnumberoflanes = context['data']['minmaxnumberoflanes']
    elif 'ome2_number_of_lanes_minmaxnumberoflanes' in context['data']:
        minmaxnumberoflanes = context['data']['ome2_number_of_lanes_minmaxnumberoflanes']
    if minmaxnumberoflanes is not None:
        minmaxnumberoflanes = str.lower(minmaxnumberoflanes)
    
    if 'numberoflanes' in context['data']:
        nb_of_lanes = context['data']['numberoflanes']
    elif 'ome2_number_of_lanes_numberoflanes' in context['data']:
        nb_of_lanes = context['data']['ome2_number_of_lanes_numberoflanes']
    if nb_of_lanes is not None:
        nb_of_lanes = str(nb_of_lanes)

    if nb_of_lanes == "" or nb_of_lanes is None:
        return "-32768"

    # This test should theoretically be applied but minmaxnumberoflanes is generally not filled
    #if minmaxnumberoflanes is not None and minmaxnumberoflanes != "" and minmaxnumberoflanes != "average":
    #    return "-32768"

    return nb_of_lanes