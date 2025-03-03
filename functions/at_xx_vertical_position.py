# def function_name(context):
        
    position = ""

    if 'lage' in context['data']:
        position = context['data']['lage']

    if position is None or position == '':
        return "void_unk"

    if position in ["Tunnel", "Galerie"]:
        return "underground"

    if position in ["Brücke", "Steg", "Staumauer"]:
        return "suspended_or_elevated"

    if position == "Ebenerdig":
        return "on_ground_surface"

    return "void_unk"