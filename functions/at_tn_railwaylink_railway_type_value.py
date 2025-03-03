# def function_name(context):

    f_code = context['data']['f_code']

    if f_code == 1306:
        return "cog_railway"

    if f_code == 1305:
        return "metro"

    if f_code == 1304:
        return "tramway"

    return "train"