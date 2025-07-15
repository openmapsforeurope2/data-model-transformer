# def function_name(context):

    ome2_lineaffc = context['data']['ome2_lineaffc']

    pattern_code_name = r'^\d{3} - .+$'

    railway_line_label = ""

    for linea in ome2_lineaffc:
        name = linea['nombre']

        if name is None or name == "" or name == "-997" or name == "-998":
            continue

        if re.match(pattern_code_name, name) :
            railway_line_label += name[6:] + "#"
        else:
            railway_line_label += name + "#"
        
    if railway_line_label != "":
        railway_line_label = railway_line_label[0:len(railway_line_label)-1]
        railway_line_label = railway_line_label[0:255]
        return railway_line_label
    
    return 'void_unk'

