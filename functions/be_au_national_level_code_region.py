# def function_name(context):

    niscode = context['data']['niscode']

    national_level_code = '4202'
    
    if niscode == '04000': 
        national_level_code = '4203'
            
    return national_level_code
