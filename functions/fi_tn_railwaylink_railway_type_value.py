# def function_name(context):

    kohdeluokka = context['data']['kohdeluokka']

    if kohdeluokka == 14131:
        return "metro"

    if kohdeluokka in [14111, 14112, 14121]:
        return "train"

    if kohdeluokka in [14141, 14142, 14151, 14152]:
        return "tramway"

    return "void_unk"