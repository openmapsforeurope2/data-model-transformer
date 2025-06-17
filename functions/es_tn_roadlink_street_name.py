# def function_name(context):

    clase = context['data']['clase']
    ome2_vial = context['data']['ome2_vial']
    titular = context['data']['titular']

    pattern = r'^[A-Z]{1,2}-\d+$'

    name_list = []

    for vial in ome2_vial:
        name = vial['nombre']
        tipo_vial = vial['tipo_vial']
        codigo = vial['codigo']
        dgc_via = vial['dgc_via']

        if ((tipo_vial >= 2000 and tipo_vial <= 2999 and (codigo not in (-997,-998) or dgc_via not in (-997,-998))) or (tipo_vial != 1000 and titular != -997)) and not re.match(pattern, name) and name != "" and name is not None:
            name = name.replace('\"', '')
            name = name.replace('"', '')
            name_list.append({
                "spelling": name,
                "language": "spa",
                "script": "latn",
                "name_status": "official",
                "nativeness": "endonym",
                "spelling_latn": name,
                "display": 1
            })
    
    return name_list

