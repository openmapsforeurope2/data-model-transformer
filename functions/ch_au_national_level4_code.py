# def function_name(context):

    national_level_code = "-32768"

    lake_area = float(context['data']['see_flaeche'])
    land_area = float(context['data']['gem_flaeche'])

    nature = context['data']['objektart']

    if nature == "Gemeindgebiet":
        national_level_code = "3104"

    elif nature == "Kommunanz":
        national_level_code = "3106"
    
    elif nature == "Kantonsgebiet":
        if lake_area == land_area:
            national_level_code = "3105"
        else:
            national_level_code = "3120"

    return national_level_code