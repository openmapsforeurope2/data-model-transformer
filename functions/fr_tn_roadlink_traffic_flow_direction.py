# def function_name(context):
    # Les valeurs possibles pour vertical_position sont:
    # 'both_directions', 'indirection', 'opposite_direction'

    # Double sens | Sans objet | Sens direct | Sens inverse
    direction = context['data']['sens_de_circulation']

    if direction == "Double sens":
        return "both_directions"

    if direction == "Sens direct":
        return "indirection"

    if direction == "Sens inverse":
        return "opposite_direction"

    return "void"