# def function_name(context):

    if 'name' in context['data']:
        name = context['data']['name']
    else:
        name = ""

    name_list = []
    name_json = []
    pos_start = 0
    pos_pipe = 0

    if name is None or name == "":
        return name_json

    # Remove spaces
    name = name.strip()

    while pos_pipe != -1:
        pos_pipe = name.find("|", pos_start)
        if pos_pipe != -1:
            name_list.append(name[pos_start:pos_pipe])
        else:
            name_list.append(name[pos_start:])
        pos_start = pos_pipe + 1
    
    if len(name_list) > 0 :
        for name in name_list:
            name = name.replace('\"', '')
            name = name.replace('"', '')
            name_json.append({
                "spelling": name,
                "language": "void_unk",
                "script": "latn",
                "name_status": "official",
                "nativeness": "endonym",
                "spelling_latn": name,
                "display": 1
            })
    
    return name_json