# def function_name(context):

    # Retrieve name value

    ome2_vial = context['data']['ome2_vial']

    name = ""
    name_list = []

    # Name as JSON

    for vial in ome2_vial:
        name = vial['nombre_alt']

        if name != "" and name is not None and name != "-997" and name != '-998':
            name = name.replace('\"', '')
            name = name.replace('"', '')
            name_list.append({
                "spelling": name,
                "language": "spa",
                "script": "latn",
                "name_status": "void_unk",
                "nativeness": "void_unk",
                "spelling_latn": name,
                "display": 1
            })

    return name_list
