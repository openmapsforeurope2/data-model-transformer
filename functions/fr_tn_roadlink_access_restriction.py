# -*- coding: utf-8 -*-
# def function_name(context):
    # Les valeurs possibles pour access_restriction sont:
    # 'forbidden_legally', 'physically_impossible', 'private', 'public_access', 'seasonal', 'toll'

    # A péage | Libre | Physiquement impossible | Restreint aux ayants droit
    access = context['data']['acces_vehicule_leger']

    # Json
    period = context['data']['periode_de_fermeture']

    if access == "Physiquement impossible":
        return "physically_impossible"
    
    if access == "A péage":
        return "toll"

    if access == "Restreint aux ayants droit":
        return "private"

    # priorité par rapport aux autres infos ?
    if period is not None:
        return "seasonal"

    if access == "Libre":
        return "public_access"

    return "void_unk"


    # forbidden_legally ? 
    # BDUNI : prive = Indique le caractère privé d'un tronçon de route carrossable. Une voie privée peut être ouverte à la circulation publique. 