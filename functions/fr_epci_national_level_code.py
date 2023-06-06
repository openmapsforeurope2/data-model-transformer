# def function_name(context):

    # TMP VERSION - a revoir

    gcms_territoire = context['data']['gcms_territoire']      

    nature = context['data']['nature']
    
    national_level_code = 0
    
    if gcms_territoire in ['GLP','GUF','MTQ','MYT','REU']:
        if nature == "Métropole":
            national_level_code = 1028
        elif nature == "Communauté urbaine":
            national_level_code = 1029
        elif nature == "Communauté d'agglomération":
            national_level_code = 1030
        elif nature == "Communauté de communes":
            national_level_code == 1031

    else: # Cas général métropole
        if nature == "Métropole":
            national_level_code = 1024
        elif nature == "Communauté urbaine":
            national_level_code = 1025
        elif nature == "Communauté d'agglomération":
            national_level_code = 1026
        elif nature == "Communauté de communes":
            national_level_code == 1027

    return national_level_code

