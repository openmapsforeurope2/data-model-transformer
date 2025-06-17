# def function_name(context):

    ome2_vial = context['data']['ome2_vial']

    label = ""

    for vial in ome2_vial:
        name = vial['nombre_alt']

        if name != "" and name is not None and name != '-997':
            name = name.replace('\"', '')
            name = name.replace('"', '')
            label += name + "#"
    
    if label != "":
        label = label[0:len(label)-1]
        return label
    
    return "void_unk"

