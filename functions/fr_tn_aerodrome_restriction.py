# def function_name(context):
    
    use = context['data']['usage']

    if use == "Militaire":
        return "reserved_for_military"

    if use == "Civil":
        return "civilian"

    if use == "Civil et militaire":
        return "void_civilian_and_military"

    if use == "Privé":
        return "void_private"

    return "void_unk"