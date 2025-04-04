# def function_name(context):
        
    use_restriction = ""

    if 'ome2_use_restriction_restriction' in context['data']:
        use_restriction = context['data']['ome2_use_restriction_restriction']

    if use_restriction is None or use_restriction == '':
        return "void_unk"
    else:
        use_restriction = str.lower(use_restriction)

    # If a link is provided in the attribute, we keep the last part only
    if use_restriction.startswith("http"): 
        pos = str.rfind(use_restriction, "/")
        if pos == -1:
            pos = str.rfind(use_restriction, "\\")
        if pos != -1:                                   
            use_restriction = str.lower(use_restriction[pos+1:])
    
    
    if use_restriction == "reservedformilitary":
        return "reserved_for_military"
    if use_restriction == "temporalrestrictions":
        return "void_temporal_restrictions"
    else:
        return "void_unk"
    