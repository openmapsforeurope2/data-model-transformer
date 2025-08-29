# def function_name(context):

    ome2_lineaffc = context['data']['ome2_lineaffc']

    pattern_code_name = r'^\d{3} - .+$'

    code = ""

    # Code after receiving an adapted version of rt_lineaffcc_a with codigo and nombre separated
    for linea in ome2_lineaffc:
        codigo = linea['codigo']

        if codigo is None or codigo == "" or codigo == "-997" or codigo == "-998":
            continue

        code += codigo + "#"
        
    if code != "":
        code = code[0:len(code)-1]
        return code

    return 'void_unk'