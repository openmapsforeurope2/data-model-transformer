# -*- coding: utf-8 -*-
# def function_name(context):
    # Les valeurs possibles pour functional_road_class sont:
    # 'main_road', 'first_class', 'second_class', 'third_class', 'fourth_class',
    # 'fifth_class', 'sixth_class', 'seventh_class', 'eighth_class', 'ninth_class'

    # Bac ou liaison maritime | Bretelle | Chemin | Escalier | Rond-point | Route à 1 chaussée |
    # Route à 2 chaussées | Route empierrée | Sentier | Type autoroutier
    nature = context['data']['nature']

    if nature in ["Type autoroutier", "Route à 2 chaussées", "Route à 1 chaussée", "Bretelle", "Rond-point"]:
        return "paved"
    if nature in ["Route empierrée", "Chemin"]:
        return "unpaved"

    return "void_unk"