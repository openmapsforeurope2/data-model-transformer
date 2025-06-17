# def function_name(context):

    name = ''
    name_tmp = ''

    language = 'void_unk'


    # Retrieve name values

    if 'etiqueta' in context['data']:
        name_tmp = context['data']['etiqueta']

        if name_tmp != '' and name_tmp is not None and name_tmp != "-997":
            name = name_tmp

    if name == '' and 'nombre' in context['data']:
        name_tmp = context['data']['nombre']
        if name_tmp != '' and name_tmp is not None and name_tmp != "-997":
            name = name_tmp


    name_list = []

    # Name as JSON
    if name != "" and name is not None :
        name = name.replace('\"', '')
        name = name.replace('"', '')
        name_list.append({
            "spelling": name,
            "language": 'void_unk',
            "script": "latn",
            "name_status": "void_unk",
            "nativeness": "void_unk",
            "spelling_latn": name,
            "display": 1
        })

    return name_list
