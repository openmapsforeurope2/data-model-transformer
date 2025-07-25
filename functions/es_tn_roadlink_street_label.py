# def function_name(context):

    clase = context['data']['clase']
    ome2_vial = context['data']['ome2_vial']
    titular = context['data']['titular']

    pattern = r'^[A-Z]{1,2}-\d+$'

    label = ""

    for vial in ome2_vial:
        name = vial['nombre']
        tipo_vial = vial['tipo_vial']
        codigo = vial['codigo']
        dgc_via = vial['dgc_via']

        if name is None or name == "" or name == '-997' or name == '-998' or tipo_vial is None:
            continue

        if ((tipo_vial >= 2000 and tipo_vial <= 2999 and (codigo not in (-997,-998) or dgc_via not in (-997,-998))) or (tipo_vial != 1000 and titular != -997)) and not re.match(pattern, name):
            name = name.replace('\"', '')
            name = name.replace('"', '')
            label += name + "#"
    
    if label != "":
        label = label[0:len(label)-1]
        label = label[0:255]
        return label
    
    return "void_unk"

