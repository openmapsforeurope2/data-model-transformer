# def function_name(context):

    # Retrieve name value

    name = ""

    if 'nombre' in context['data']:
        name = context['data']['nombre']

    name_list = []

    # Name as JSON
    if name != "" and name is not None and name != "-997" and name != "-998" :
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
