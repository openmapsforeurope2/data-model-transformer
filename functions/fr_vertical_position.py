# def function_name(context):
    # Les valeurs possibles pour road_surface_category sont:
    # 'paved', 'unpaved'

    # 0 | 1 | -1 | 2 | -2 | 3 | -3 | 4 | -4 | Gué ou radier
    position = context['data']['position_par_rapport_au_sol']

    if position in ["-1","-2","-3","-4"]:
        return "underground"

    if position in ["1","2","3","4"]:
        return "suspended_or_elevated"

    return "on_ground_surface"