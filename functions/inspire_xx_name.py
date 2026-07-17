# def function_name(context):

    spelling = ""
    language = "void_unk"
    script = "latn"
    name_status = "void_unk"
    nativeness = "endonym"
    spelling_latn = ""
    display = 1


    country = 'void_unk' if 'country' not in context['data'] or context['data'] == '' or context['data'] is None else context['data']['country']

    ## spelling and spelling_latn
    if 'geographicalname_spelling_text' in context['data']:
        spelling = context['data']['geographicalname_spelling_text']
    elif 'name_gn_spell_spellofna_text' in context['data']:
        spelling = context['data']['name_gn_spell_spellofna_text']
    elif 'geographicalname' in context['data']:
        spelling = context['data']['geographicalname']
    elif 'text' in context['data']:
        spelling = context['data']['text']
    elif 'ome2_watercourse_geographicalname' in context['data']:
        spelling = context['data']['ome2_watercourse_geographicalname']
    elif 'streetname' in context['data']:
        spelling = context['data']['streetname']
    elif 'spellingofname_text' in context['data']:
        spelling = context['data']['spellingofname_text']

    spelling_latn = spelling

    ## script
    if 'geographicalname_spelling_script' in context['data']:
        script = context['data']['geographicalname_spelling_script']
    elif 'name_gn_spell_spellofna_script' in context['data']:
        script = context['data']['name_gn_spell_spellofna_script']
    elif 'script' in context['data']:
        script = context['data']['script']

    ## nativeness
    if 'geographicalname_nativeness' in context['data']:
        nativeness = context['data']['geographicalname_nativeness']
    elif 'name_gn_nativeness' in context['data']:
        nativeness = context['data']['name_gn_nativeness']
    elif 'nativeness' in context['data']:
        nativeness = context['data']['nativeness']
    
    if nativeness != "" and nativeness is not None and nativeness.startswith("http"): 
        pos = str.rfind(nativeness, "/")
        if pos == -1:
            pos = str.rfind(nativeness, "\\")
        if pos != -1:                                   
            nativeness = str.lower(nativeness[pos+1:])

    ## name_status
    if 'geographicalname_namestatus' in context['data']:
        name_status = context['data']['geographicalname_namestatus']
    elif 'name_gn_namestatus' in context['data']:
        name_status = context['data']['name_gn_namestatus']
    elif 'namestatus' in context['data']:
        name_status = context['data']['namestatus']

    if name_status != "" and name_status is not None and name_status.startswith("http"): 
        pos = str.rfind(name_status, "/")
        if pos == -1:
            pos = str.rfind(name_status, "\\")
        if pos != -1:                                   
            name_status = str.lower(name_status[pos+1:])

    ## language
    if 'geographicalname_language' in context['data']:
        language = context['data']['geographicalname_language']
    elif 'name_gn_language' in context['data']:
        language = context['data']['name_gn_language']
    elif 'language' in context['data']:
        language = context['data']['language']

    name_list = []
    
    if spelling != "" and spelling is not None :  
        spelling = spelling.replace('\"', '')
        spelling = spelling.replace('"', '')    
        name_list.append({
            "spelling": spelling,
            "language": str.lower(language),
            "script": str.lower(script),
            "name_status": name_status,
            "nativeness": nativeness,
            "spelling_latn": spelling_latn,
            "country": country,
            "display": display
        })
           
    return name_list
