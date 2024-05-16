# def function_name(context):


    # 0 | 1 | -1 | 2 | -2 | 3 | 4 | 5 | 6
    stufe = int(context['data']['stufe'])

    if stufe < 0:
        return "underground"

    if stufe > 0:
        return "suspended_or_elevated"

    if stufe == 0:
        return "on_ground_surface"

    return "void_unk"