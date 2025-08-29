# def function_name(context):

    ome2_lineaffc = context['data']['ome2_lineaffc']

    pattern_code_name = r'^\d{3} - .+$'

    name_list = []

    for linea in ome2_lineaffc:
        name = linea['nombre']

        if name == "" or name is None or name == '-997' or name == "-998":
            continue

        # To be used for the original version where codes and names were stored in the same "nombre" field       
        #if re.match(pattern_code_name, name):
        #    name = name[6:]
             
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


