# def function_name(context):
    
    zus = context['data'].get('zus')

    
    if zus == 2100:
        return "disused"
    elif zus == 4000:
        return "under_construction"
    else:
        return "void_unk"