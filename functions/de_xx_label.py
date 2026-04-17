# def function_name(context):
    
    if 'nam' in context['data']:
        nam = (context['data'].get('nam') or '').replace('"', "'")
    else:
        nam = ""
    if 'znm' in context['data']:
        znm = (context['data'].get('znm') or '').replace('"', "'")
    else:
        znm = ""

    if nam is not None and nam != "":
        return nam
        
    elif znm is not None and znm != "":
        return znm
        
    return "void_unk"