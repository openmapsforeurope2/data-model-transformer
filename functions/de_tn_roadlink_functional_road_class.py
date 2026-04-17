# def function_name(context):
    
    objart = context['data'].get('objart')

    if objart == 42003:
        wdm = context['data'].get('wdm')
        if wdm == 1301:
            return "main_road"
        elif wdm == 1303:
            return "first_class"
        elif wdm == 1305:
            return "second_class"
        elif wdm == 1306:
            return "third_class"
        elif wdm == 1307:
            return "fourth_class"
        elif wdm == 9997:
            return "fifth_class"
        
    elif objart == 42008:
        fkt = context['data'].get('fkt')
        if fkt == 5211:
            return "sixth_class"
        elif fkt == 5212:
            return "seventh_class"
        elif fkt in [5240,5250]:
            return "eighth_class"
        
    elif objart == 53003:
        art = context['data'].get('art')
        if art in [1106,1110]:
            return "eighth_class"
        elif art == 1103:
            return "ninth_class"
        
    return "void_unk"