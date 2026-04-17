# def function_name(context):
    
    bkt = context['data'].get('bkt')

    
    if bkt == 1301:
        return "cog_railway"
    elif bkt in [1300,1302]:
        return "funicular"
    elif bkt == 1600:
        return "magnetic_levitation"
    elif bkt in [1200,1202]:
        return "metro"
    elif bkt in [1100,1101,1102,1104]:
        return "train"
    elif bkt == 1400:
        return "branch_line_train"
    elif bkt == 1201:
        return "tramway"
    elif bkt == 2500:
        return "suspended_rail"
    else:
        return "void_unk"