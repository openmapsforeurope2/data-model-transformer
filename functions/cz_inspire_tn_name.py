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
    
    if 'geographicalname_spelling_script' in context['data']:
        script = context['data']['geographicalname_spelling_script']
    
    if 'geographicalname_nativeness' in context['data']:
        nativeness = context['data']['geographicalname_nativeness']
    
    if 'geographicalname_namestatus' in context['data']:
        name_status = context['data']['geographicalname_namestatus']

    if 'geographicalname_language' in context['data']:
        language = context['data']['geographicalname_language']

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
