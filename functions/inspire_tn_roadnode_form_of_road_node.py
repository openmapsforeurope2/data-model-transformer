# def function_name(context):
    
    form_of_road_node = ""

    # Retrieve source formofway value
    if 'formofroadnode' in context['data']:
        form_of_road_node = context['data']['formofroadnode']

    if form_of_road_node is None or form_of_road_node == '':
        return "void_unk"
    else:
        form_of_road_node = str.lower(form_of_road_node) 

    # If formofway is provided as a link, we keep only the final part
    if form_of_road_node != "" and form_of_road_node is not None and form_of_road_node.startswith("http"): 
        pos = str.rfind(form_of_road_node, "/")
        if pos == -1:
            pos = str.rfind(form_of_road_node, "\\")
        if pos != -1:                                   
            form_of_road_node = str.lower(form_of_road_node[pos+1:])

    if form_of_road_node in ["junction", "interchange", "roundabout"]:
        return "form_of_road_node"

    if form_of_road_node == "enclosedtrafficarea":
        return "enclosed_traffic_area"

    if form_of_road_node == "levelcrossing":
        return "level_crossing"

    if form_of_road_node == "pseudonode":
        return "pseudo_node"  
 
    if form_of_road_node == "roadend":
        return "road_end"

    if form_of_road_node == "trafficsquare":
        return "traffic_square"

    if form_of_road_node == "roadservicearea":
        return "road_service_area"
    
    return "void_unk"