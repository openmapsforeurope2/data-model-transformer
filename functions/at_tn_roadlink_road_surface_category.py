# -*- coding: utf-8 -*-
# def function_name(context):
    # Les valeurs possibles pour functional_road_class sont:
    # 'main_road', 'first_class', 'second_class', 'third_class', 'fourth_class',
    # 'fifth_class', 'sixth_class', 'seventh_class', 'eighth_class', 'ninth_class'

    # Bac ou liaison maritime | Bretelle | Chemin | Escalier | Rond-point | Route à 1 chaussée |
    # Route à 2 chaussées | Route empierrée | Sentier | Type autoroutier
    f_code = context['data']['f_code']

    if f_code in [1101, 1102, 1103, 1104, 1105, 1111, 1112, 1113, 1131]:
        return "paved"
    if f_code in [1122, 1141,1142]:
        return "unpaved"

    return "void_unk"