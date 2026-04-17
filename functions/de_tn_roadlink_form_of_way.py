# def function_name(context):
    
    objart = context['data'].get('objart')

    if objart == 42003:
        wdm = context['data'].get('wdm')
        fkt = context['data'].get('fkt')
        if wdm == 1301:
            return "motorway"
        elif ftr == 2000:
            return "dual_carriage_way"
        elif fkt == 1808:
            return "pedestrian_zone"
        else:
            return "single_carriage_way"
        
    elif objart == 42008:
        fkt = context['data'].get('fkt')
        if fkt == 5211:
            return "single_carriage_way"
        elif fkt == 5212:
            return "tractor_road"
        elif fkt in [5240,5250]:
            return "bicycle_road"
        
    elif objart == 53003:
        art = context['data'].get('art')
        if art in [1106,1110]:
            return "bicycle_road"
        elif art == 1103:
            return "walkway"
        
    return "void_unk"