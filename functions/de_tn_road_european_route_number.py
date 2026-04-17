# def function_name(context):
    
    bez = context['data'].get('bez')

    european = []
    
    if bez is not None and bez != "":
        bez_list = bez.split('#')
        for element in bez_list:
            if element.startswith('E'):
                european.append(element)
    
    if european:
        return "#".join(european)
        
    return "void_unk"