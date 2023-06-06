# def function_name(context):

    gcms_territoire = context['data']['gcms_territoire']      
    
    code_departement = context['data']['code_insee']
    if code_departement == "" or code_departement == None:
        if gcms_territoire == "FXX":
            code_departement = "00"
        else:
            code_departement = "000"

    code_region = context['data']['code_insee_de_la_region']  
    if code_region == "" or code_region == None:
        code_region = "00"


    shn_code = ""

    if gcms_territoire == 'GLP':
        shn_code = "GP{0}{1}000000".format(code_region, code_departement)
        
    elif gcms_territoire == 'GUF':
        shn_code = "GF{0}{1}000000".format(code_region, code_departement)
        
    elif gcms_territoire == 'MTQ':
        shn_code = "MQ{0}{1}000000".format(code_region, code_departement)
        
    elif gcms_territoire == 'MYT':
        shn_code = "YT{0}{1}000000".format(code_region, code_departement)

    elif gcms_territoire == 'REU':
        shn_code = "RE{0}{1}000000".format(code_region, code_departement)

    else: # Cas général métropole
        shn_code = "FR{0}{1}0000000".format(code_region, code_departement)

    return shn_code

