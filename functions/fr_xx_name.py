# def function_name(context):

    if 'toponyme' in context['data']:
        nom = context['data']['toponyme']
    elif 'cpx_toponyme_route_nommee' in context['data']:
        nom = context['data']['cpx_toponyme_route_nommee']
    elif 'cpx_toponyme_de_cours_d_eau' in context['data']:
        nom = context['data']['cpx_toponyme_de_cours_d_eau']
    elif 'cpx_toponyme_de_plan_d_eau' in context['data']:
        nom = context['data']['cpx_toponyme_de_plan_d_eau']
    elif 'cpx_toponyme' in context['data']:
        nom = context['data']['cpx_toponyme']
    elif 'ome2_toponyme_troncon_hydrographique' in context['data']:
        nom = context['data']['ome2_toponyme_troncon_hydrographique']
    else:
        nom = ""
    name_list = []
    
    if nom != "" and nom is not None :
        nom = nom.replace('\"', '')
        nom = nom.replace('"', '')
        name_list.append({
            "spelling": nom,
            "language": "fre",
            "script": "latn",
            "name_status": "official",
            "nativeness": "endonym",
            "spelling_latn": nom,
            "display": 1
        })
    
    return name_list
