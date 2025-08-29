# def function_name(context):

    # Retrieve name value

    ome2_vial = context['data']['ome2_vial']
    titular = context['data']['titular']

    # Pattern for road numbers : 1 or 2 letters, hyphen, then digits
    pattern = r'^[A-Z]{1,2}-\d+$'

    name = ""
    name_list = []

    # Name as JSON

    for vial in ome2_vial:
        name = vial['nombre']
        tipo_vial = vial['tipo_vial']

        if name is None or name == "" or name == '-997' or name == '-998' or tipo_vial is None or titular is None:
            continue

        if (tipo_vial == 1000 and titular != -997) and not re.match(pattern, name):
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
