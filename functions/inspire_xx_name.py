# def function_name(context):

    spelling = ""
    language = "void_unk"
    script = "latn"
    name_status = "void_unk"
    nativeness = "endonym"
    spelling_latn = ""
    display = 1

    if 'geographicalname_spelling_text' in context['data']:
        spelling = context['data']['geographicalname_spelling_text']
        spelling_latn = spelling
    elif 'name_gn_spell_spellofna_text' in context['data']:
        spelling = context['data']['name_gn_spell_spellofna_text']
        spelling_latn = spelling
    elif 'geographicalname' in context['data']:
        spelling = context['data']['geographicalname']
        spelling_latn = spelling
    elif 'text' in context['data']:
        spelling = context['data']['text']
        spelling_latn = spelling

    if 'geographicalname_spelling_script' in context['data']:
        script = context['data']['geographicalname_spelling_script']
    elif 'name_gn_spell_spellofna_script' in context['data']:
        script = context['data']['name_gn_spell_spellofna_script']
    elif 'script' in context['data']:
        script = context['data']['script']

    if 'geographicalname_nativeness' in context['data']:
        nativeness = context['data']['geographicalname_nativeness']
    elif 'name_gn_nativeness' in context['data']:
        nativeness = context['data']['name_gn_nativeness']
    elif 'nativeness' in context['data']:
        nativeness = context['data']['nativeness']
    
    if 'geographicalname_namestatus' in context['data']:
        name_status = context['data']['geographicalname_namestatus']
    elif 'name_gn_namestatus' in context['data']:
        name_status = context['data']['name_gn_namestatus']
    elif 'namestatus' in context['data']:
        name_status = context['data']['namestatus']

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
            "language": language,
            "script": script,
            "name_status": name_status,
            "nativeness": nativeness,
            "spelling_latn": spelling_latn,
            "display": display
        })
           
    return name_list
