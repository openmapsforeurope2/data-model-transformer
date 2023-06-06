# def function_name(context):

    # TMP VERSION - a revoir

    gcms_territoire = context['data']['gcms_territoire']      

    code_epci = context['data']['code_epci_ebm']
    if code_epci == "" or code_epci == None:
        code_epci = "000"
    
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


    if gcms_territoire == 'GLP':
        shn_code = "GP000000{0}00".format(code_epci)
        
    elif gcms_territoire == 'GUF':
        shn_code = "GF000000{0}00".format(code_epci)
        
    elif gcms_territoire == 'H_T':
        shn_code = ""
        
    elif gcms_territoire == 'MTQ':
        shn_code = "MQ000000{0}00".format(code_epci)
        
    elif gcms_territoire == 'MYT': # Cas particulier : pas d'arrondissements
        shn_code = "YT000000{0}00".format(code_epci)

    elif gcms_territoire == 'REU':
        shn_code = "RE000000{0}00".format(code_epci)

    else: # Cas général métropole
        shn_code = "FR00000{0}000".format(code_epci)

    return shn_code

