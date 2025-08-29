# def function_name(context):
    # Les valeurs possibles pour functional_road_class sont:
    # 'main_road', 'first_class', 'second_class', 'third_class', 'fourth_class',
    # 'fifth_class', 'sixth_class', 'seventh_class', 'eighth_class', 'ninth_class'

    # Bac ou liaison maritime | Bretelle | Chemin | Escalier | Rond-point | Route à 1 chaussée |
    # Route à 2 chaussées | Route empierrée | Sentier | Type autoroutier
    orden = context['data']['orden']

    if orden == 'P':
        return "main_road"

    if orden == '1':
        return "first_class"

    if orden == '2':
        return "second_class"

    if orden == '3':
        return "third_class"
    
    if orden == 'N':
        return "fourth_class"

    return "void_unk"