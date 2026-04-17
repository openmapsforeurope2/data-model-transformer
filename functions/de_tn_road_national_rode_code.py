# def function_name(context):
    
    bez = context['data'].get('bez')

    national = []
    
    if bez is not None and bez != "":
        bez_list = bez.split('#')
        for element in bez_list:
            if not element.startswith('E'):
                national.append(element)
    
    if national:
        return "#".join(national)
        
    return "void_unk"