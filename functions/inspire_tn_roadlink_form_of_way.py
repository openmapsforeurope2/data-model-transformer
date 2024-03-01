# def function_name(context):
    
    fow_source = ""

    if 'formofway' in context['data']:
        fow_source = str.lower(context['data']['formofway'])

    if fow_source == "dualcarriageway":
        return "dual_carriage_way"

    if fow_source == "motorway":
        return "motorway"

    if fow_source == "roundabout":
        return "roundabout"

    if fow_source == "sliproad":
        return "slip_road"  
 
    if fow_source == "singlecarriageway":
        return "single_carriage_way"

    if fow_source == "walkway":
        return "walkway"

    if fow_source == "tractorroad":
        return "tractor_road"
    
    return "void_unk"