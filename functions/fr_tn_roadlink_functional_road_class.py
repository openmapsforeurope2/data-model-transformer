# def function_name(context):
    # Les valeurs possibles pour functional_road_class sont:
    # 'main_road', 'first_class', 'second_class', 'third_class', 'fourth_class',
    # 'fifth_class', 'sixth_class', 'seventh_class', 'eighth_class', 'ninth_class'

    # Bac ou liaison maritime | Bretelle | Chemin | Escalier | Rond-point | Route à 1 chaussée |
    # Route à 2 chaussées | Route empierrée | Sentier | Type autoroutier
    importance = context['data']['importance']

    if importance == "1":
        return "main_road"
    if importance == "2":
        return "first_class"
    if importance == "3":
        return "second_class"
    if importance == "4":
        return "third_class"
    if importance == "5":
        return "fourth_class"
    if importance == "6":
        return "fifth_class"

    return "void_unk"