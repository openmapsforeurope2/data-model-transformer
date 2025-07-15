# def function_name(context):

    ome2_lineaffc = context['data']['ome2_lineaffc']

    pattern_code_name = r'^\d{3} - .+$'

    code = ""

    for linea in ome2_lineaffc:
        name = linea['nombre']

        if name is None or name == "" or name == "-997" or name == "-998":
            continue

        if re.match(pattern_code_name, name) :
            code += name[0:4] + "#"
        
    if code != "":
        code = code[0:len(code)-1]
        return code
    
    return 'void_unk'

