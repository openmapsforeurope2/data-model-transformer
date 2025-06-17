# def function_name(context):

    tipo_linea = context['data']['tipo_linea']
    tipo_tramo = context['data']['tipo_tramo']

    if tipo_linea == 5:
        return "cog_railway"

    if tipo_linea == 4:
        return "funicular"

    if tipo_linea == 3:
        return "metro"

    if tipo_linea == 1:
        if tipo_tramo == 1:
            return "main_line_train"
        elif tipo_tramo == 2:
            return "branch_line_train"
        else:
            return "train"
        
    if tipo_linea in [2,6]:
        return "tramway"

    return "void_unk"