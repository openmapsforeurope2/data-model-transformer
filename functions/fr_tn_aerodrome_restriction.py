# def function_name(context):
    
    use = context['data']['usage']

    if use == "Militaire":
        return "reserved_for_military"

    if use == "Civil":
        return "civilian"

    if use == "Civil et militaire":
        return "mixed"

    if use == "Privé":
        return "void_private"

    return "void_unk"