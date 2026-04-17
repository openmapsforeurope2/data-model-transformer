# def function_name(context):
    
    bkt = context['data'].get('bkt')

    
    if bkt == 1102:
        return "cargo"
    elif bkt in [1100,2500]:
        return "mixed"
    elif bkt in [1101,1104,1200,1201,1202,1500,1600]:
        return "passengers"
    else:
        return "void_unk"