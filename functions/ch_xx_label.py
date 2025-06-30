# def function_name(context):

    if 'name' in context['data']:
        name = context['data']['name']
    else:
        name = ""

    name_list = []
    name_json = []
    pos_start = 0
    pos_pipe = 0

    label = ""

    if name is None or name == "":
        return "void_unk"

    # Remove spaces
    name = name.strip()

    while pos_pipe != -1:
        pos_pipe = name.find("|", pos_start)
        if pos_pipe != -1:
            name_list.append(name[pos_start:pos_pipe].strip())
        else:
            name_list.append(name[pos_start:].strip())
        pos_start = pos_pipe + 1
    
    if len(name_list) > 0 :
        for name in name_list:
            name = name.replace('\"', '')
            name = name.replace('"', '')
            label = label + '#' + name

    if label is not None and label != "":
        label = label[1:]
    else:
        label = "void_unk"

    return label       