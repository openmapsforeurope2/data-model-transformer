# def function_name(context):

    if 'toponyme' in context['data']:
        nom = context['data']['toponyme']
    elif 'cpx_toponyme_de_cours_d_eau' in context['data']:
        nom = context['data']['cpx_toponyme_de_cours_d_eau']
    elif 'cpx_toponyme_de_plan_d_eau' in context['data']:
        nom = context['data']['cpx_toponyme_de_plan_d_eau']
    else:
        nom = ""
    name_list = []
    
    if nom != "" and nom is not None :
        nom = nom.replace('\"', '')
        nom = nom.replace('"', '')
        name_list.append({
            "spelling": nom,
            "language": "fre",
            "script": "latin",
            "name_status": "official",
            "nativeness": "endonym"
        })
    
    return name_list
