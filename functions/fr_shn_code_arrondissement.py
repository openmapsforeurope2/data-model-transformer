# def function_name(context):

    gcms_territoire = context['data']['gcms_territoire']      
    
    code_departement = context['data']['code_insee_du_departement']
    if code_departement == "" or code_departement == None:
        if gcms_territoire == "FXX":
            code_departement = "00"
        else:
            code_departement = "000"

    code_arrondissement = context['data']['code_insee_de_l_arrondissement']
    if code_arrondissement == "" or code_arrondissement == None :
        code_arrondissement = "0"

    code_region = context['data']['code_insee_de_la_region']  
    if code_region == "" or code_region == None:
        code_region = "00"


    shn_code = ""
    code_commune = "00"

    if gcms_territoire == 'GLP':
        shn_code = "GP{0}{1}{2}00000".format(code_region, code_departement, code_arrondissement)
        
    elif gcms_territoire == 'GUF':
        shn_code = "GF{0}{1}{2}00000".format(code_region, code_departement, code_arrondissement)
        
    elif gcms_territoire == 'MTQ':
        shn_code = "MQ{0}{1}{2}00000".format(code_region, code_departement, code_arrondissement)

    elif gcms_territoire == 'REU':
        shn_code = "RE{0}{1}{2}00000".format(code_region, code_departement, code_arrondissement)

    else: # Cas général métropole
        shn_code = "FR{0}{1}{2}00000".format(code_region, code_departement, code_arrondissement)

    return shn_code

