# def function_name(context):

    code_insee = context['data']['code_insee']

    code_arrondissement = context['data']['code_insee_de_l_arrondissement']
    if code_arrondissement == "":
        code_arrondissement = 0

    code_departement = context['data']['code_insee_du_departement']
    if code_departement == "":
        code_departement = 0

    code_region = context['data']['code_insee_de_la_region']  
    if code_region == "":
        code_region = 0

    gcms_territoire = context['data']['gcms_territoire']  

    shn_code = ""
    code_commune = code_insee[len(code_insee)-4:len(code_insee-1)]

    match gcms_territoire:
        case 'GLP':
            code_commune = code_insee[len(code_insee)-3:len(code_insee-1)]
            shn_code = "GP{0}{1}{2}{3}".format(code_region, code_departement, code_arrondissement, code_commune)
        
        case 'GUF':
            code_commune = code_insee[len(code_insee)-3:len(code_insee-1)]
            shn_code = "GF{0}{1}{2}{3}".format(code_region, code_departement, code_arrondissement, code_commune)
        
        case 'H_T':
            shn_code = ""
        
        case 'MTQ':
            code_commune = code_insee[len(code_insee)-3:len(code_insee-1)]
            shn_code = "MQ{0}{1}{2}{3}".format(code_region, code_departement, code_arrondissement, code_commune)
        
        case 'MYT':
            code_commune = code_insee[len(code_insee)-3:len(code_insee-1)]
            shn_code = "YT{0}{1}{2}{3}".format(code_region, code_departement, code_arrondissement, code_commune)

        case 'REU':
            code_commune = code_insee[len(code_insee)-3:len(code_insee-1)]
            shn_code = "RE{0}{1}{2}{3}".format(code_region, code_departement, code_arrondissement, code_commune)

        case 'SPM':
            shn_code = "PM{0}{1}{2}{3}".format(code_insee)

        case _: # Cas général métropole (hors Paris, Marseille, Lyon)
            code_commune = code_insee[len(code_insee)-4:len(code_insee-1)]
            shn_code = "FR{0}{1}{2}{3}".format(code_region, code_departement, code_arrondissement, code_commune)


    return shn_code

