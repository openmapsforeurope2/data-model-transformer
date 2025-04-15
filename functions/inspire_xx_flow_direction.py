# def function_name(context):
        
    flowdirection = ""

    if 'ome2_net_watercourse_link_flowdirection' in context['data']:
        flowdirection = context['data']['ome2_net_watercourse_link_flowdirection']
    elif 'flowdirection' in context['data']:
        flowdirection = context['data']['flowdirection']

    if flowdirection is None or flowdirection == '':
        return "void_unk"
    else:
        flowdirection = str.lower(flowdirection) 

    # If a link is provided in the attribute, we keep the last part only
    if flowdirection.startswith("http"): 
        pos = str.rfind(flowdirection, "/")
        if pos == -1:
            pos = str.rfind(flowdirection, "\\")
        if pos != -1:                                   
            flowdirection = str.lower(flowdirection[pos+1:])

    if flowdirection == "bothdirections":
        return "both_directions"

    if flowdirection == "indirection":
        return "in_direction"

    if flowdirection == "oppositedirection":
        return "opposite_direction"

    return "void_unk"