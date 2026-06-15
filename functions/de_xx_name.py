# def function_name(context):
    
    if 'nam' in context['data']:
        nam = (context['data'].get('nam') or '').replace('"', "'")
    else:
        nam = ""
    if 'znm' in context['data']:
        znm = (context['data'].get('znm') or '').replace('"', "'")
    else:
        znm = ""

    name_list = []

    if nam is not None and nam != "":
        name_list.insert(0, {
                "spelling": nam,
                "language": "ger",
                "script": "latn",
                "name_status": "offical",
                "nativeness": "endonym",
                "spelling_latn": nam,
                "country": "de",
                "display": 1
                })
        
    if znm is not None and znm != "":
        name_list.append({
                "spelling": znm,
                "language": "ger",
                "script": "latn",
                "name_status": "void_unk",
                "nativeness": "endonym",
                "spelling_latn": znm,
                "country": "de",
                "display": 2
                })
        
    return name_list