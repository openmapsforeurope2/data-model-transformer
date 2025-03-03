# def function_name(context):
    # Les valeurs possibles pour functional_road_class sont:
    # 'main_road', 'first_class', 'second_class', 'third_class', 'fourth_class',
    # 'fifth_class', 'sixth_class', 'seventh_class', 'eighth_class', 'ninth_class'

    # Bac ou liaison maritime | Bretelle | Chemin | Escalier | Rond-point | Route à 1 chaussée |
    # Route à 2 chaussées | Route empierrée | Sentier | Type autoroutier
    f_code = context['data']['f_code']

    if f_code == 1101 or f_code == 1102:
        return "main_road"

    if f_code == 1103:
        return "first_class"

    if f_code == 1104:
        return "second_class"

    if f_code == 1105:
        return "third_class"

    if f_code in [1111,1112,1113]:
        return "fourth_class"

    if f_code == 1131:
        return "fifth_class"

    if f_code == 1121:
        return "sixth_class"

    if f_code == 1122:
        return "seventh_class"

    if f_code in [1141, 1143]:
        return "eigth_class"

    if f_code == 1142:
        return "ninth_class"

    return "void_unk"