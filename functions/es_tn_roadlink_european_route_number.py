# def function_name(context):

    clase = context['data']['clase']
    ome2_vial = context['data']['ome2_vial']

    pattern = r'^E-\d+$'

    if clase not in [1001, 1002, 1003]:
        return "void_unk"

    road_code = ""

    for vial in ome2_vial:
        name = vial['nombre']
        tipo_vial = vial['tipo_vial']

        if re.match(pattern, name) and tipo_vial == 4006:
            road_code += name + "#"
    
    if road_code != "":
        road_code = road_code[0:len(road_code)-1]
        return road_code

    return "void_unk"
