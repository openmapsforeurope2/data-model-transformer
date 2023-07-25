# def function_name(context):

    # TMP VERSION - a revoir

    gcms_territoire = context['data']['gcms_territoire']      

    code_epci = context['data']['code_epci_ebm']
    if code_epci == "" or code_epci == None:
        code_epci = "000"

    if gcms_territoire == 'GLP':
        shn_code = "GP000000{0}00".format(code_epci)
        
    elif gcms_territoire == 'GUF':
        shn_code = "GF000000{0}00".format(code_epci)
        
    elif gcms_territoire == 'H_T':
        shn_code = ""
        
    elif gcms_territoire == 'MTQ':
        shn_code = "MQ000000{0}00".format(code_epci)
        
    elif gcms_territoire == 'MYT':
        shn_code = "YT000000{0}00".format(code_epci)

    elif gcms_territoire == 'REU':
        shn_code = "RE000000{0}00".format(code_epci)

    else: # Cas général métropole
        shn_code = "FR00000{0}000".format(code_epci)

    return shn_code

