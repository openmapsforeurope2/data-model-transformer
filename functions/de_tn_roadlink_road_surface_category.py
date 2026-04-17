# def function_name(context):
    
    objart = context['data'].get('objart')

    if objart == 42003:
        ofm = context['data'].get('ofm')
        if ofm in [1220,1230,1240]:
            return "paved"
        elif ofm == 1250:
            return "unpaved"

    elif objart == 42008:
        fkt = context['data'].get('fkt')
        if fkt == 5211:
            return "paved"
        elif fkt == 5212:
            return "unpaved"
        
    return "void_unk"