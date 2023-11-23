# def function_name(context):

    maximum_height = ""
    maximum_length = ""
    maximum_width = ""
    maximum_total_weight = ""
    maximum_single_axle_weight = ""

    restriction_string = "'{}'::json"
    restriction_list = []
    restriction_dict = {}

    if 'restriction_de_hauteur' in context['data']:
        maximum_height = context['data']['restriction_de_hauteur']
        if maximum_height != "" and maximum_height is not None:
            restriction_dict["maximum_height"] = maximum_height
            #restriction_list.append('"maximum_height": "' + str(maximum_height) + '"')

    if 'restriction_de_longueur' in context['data']:
        maximum_length = context['data']['restriction_de_longueur']
        if maximum_length != "" and maximum_length is not None:
            restriction_dict["maximum_length"] = maximum_length
            #restriction_list.append('"maximum_length": "' + str(maximum_length) + '"')


    if 'restriction_de_largeur' in context['data']:
        maximum_width = context['data']['restriction_de_largeur']
        if maximum_width != "" and maximum_width is not None:
            restriction_dict["maximum_width"] = maximum_width
            #restriction_list.append('"maximum_width": "' + str(maximum_width) + '"')

    if 'restriction_de_poids_total' in context['data']:
        maximum_total_weight = context['data']['restriction_de_poids_total']
        if maximum_total_weight != "" and maximum_total_weight is not None:
            restriction_dict["maximum_total_weight"] = maximum_total_weight
            #restriction_list.append('"maximum_total_weight": "' + str(maximum_total_weight) + '"')

    if 'restriction_de_poids_par_essieu' in context['data']:
        maximum_single_axle_weight = context['data']['restriction_de_poids_par_essieu']
        if maximum_single_axle_weight != "" and maximum_single_axle_weight is not None:
            restriction_dict["maximum_single_axle_weight"] = maximum_single_axle_weight
            #restriction_list.append('"maximum_single_axle_weight": "' + str(maximum_single_axle_weight) + '"')

    return restriction_dict
    
    nb_restriction = len(restriction_list)
    if nb_restriction > 0:
        restriction_string = '{'
        for rest in restriction_list:
            restriction_string += rest + ','
        restriction_string = restriction_string[0:len(restriction_string)-1] + '}'
        print (restriction_string)

    return restriction_string
