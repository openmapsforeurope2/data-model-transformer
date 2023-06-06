# def function_name(context):

    gcms_territoire = context['data']['gcms_territoire']      

    code_insee = context['data']['code_insee']
    if code_insee == "" or code_insee == None :
        code_insee = "0"

    country_code = ""

    if gcms_territoire == 'GLP':
        country_code = 'GP'
        
    elif gcms_territoire == 'GUF':
        country_code = 'GF'
        
    elif gcms_territoire == 'MTQ':
        country_code = 'MQ'
        
    elif gcms_territoire == 'MYT':
        country_code = 'YT'

    elif gcms_territoire == 'REU':
        country_code = 'RE'

    elif gcms_territoire == 'FXX':
        country_code = 'FR'
    
    else:
        country_code = 'N_A'

    shn_code = "{0}{1}000000000".format(country_code, code_insee)

    return shn_code

