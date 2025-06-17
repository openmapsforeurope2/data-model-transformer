# def function_name(context):

    ome2_vial = context['data']['ome2_vial']

    tent_network = "false"

    for vial in ome2_vial:
        tipo_vial = vial['tipo_vial']

        if tipo_vial == 4005:
            return "true"
    
    return tent_network

