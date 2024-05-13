# -*- coding: utf-8 -*-
# def function_name(context):
    # Les valeurs possibles pour access_restriction sont:
    # 'forbidden_legally', 'physically_impossible', 'private', 'public_access', 'seasonal', 'toll'

    # A péage | Libre | Physiquement impossible | Restreint aux ayants droit
    verkehr = context['data']['verkehrsbeschraenkung']
    befahr = context['data']['befahrbarkeit']

    # Json
    if befahr == 1:
        return "physically_impossible"
    
    if verkehr == "Gebührenpflichtig":
        return "toll"

    if verkehr == "Wintersperre":
        return "seasonal"

    if verkehr == "Keine":
        return "public_access"

    return "void_unk"

