# def function_name(context):

    natcode = context['data']['nationalcode']

    shn = 'void_unk'
    
    if natcode is not None and natcode != "":
        shn = str(natcode)
        if len(shn) == 3:
            shn = "0" + shn
            
    return shn
