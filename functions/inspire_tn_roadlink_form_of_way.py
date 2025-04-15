# def function_name(context):
    
    fow_source = ""

    # Retrieve source formofway value
    if 'formofway' in context['data']:
        fow_source = context['data']['formofway']
    elif 'ome2_form_of_way_formofway' in context['data']:
        fow_source = context['data']['ome2_form_of_way_formofway']

    if fow_source is None or fow_source == '':
        return "void_unk"
    else:
        fow_source = str.lower(fow_source) 

    # If formofway is provided as a link, we keep only the final part
    if fow_source.startswith("http"): 
        pos = str.rfind(fow_source, "/")
        if pos == -1:
            pos = str.rfind(fow_source, "\\")
        if pos != -1:                                   
            fow_source = str.lower(fow_source[pos+1:])

    if fow_source in ["freeway", "motorway", "walkway", "roundabout"]:
        return fow_source

    if fow_source == "dualcarriageway":
        return "dual_carriage_way"

    if fow_source == "singlecarriageway":
        return "single_carriage_way"

    if fow_source == "sliproad":
        return "slip_road" 

    if fow_source == "enclosedtrafficarea":
        return "enclosed_traffic_area" 
 
     if fow_source == "tractorroad":
        return "tractor_road"

    if fow_source == "bicycleroad":
        return "bicycle_road"

    if fow_source == "entranceorexitcarpark":
        return "entrance_or_exit_car_park"

    if fow_source == "entranceorexitservice":
        return "entrance_or_exit_service"

    if fow_source == "pedestrianzone":
        return "pedestrian_zone"

    if fow_source == "trafficsquare":
        return "traffic_square"

    if fow_source == "serviceroad":
        return "service_road"

    return "void_unk"