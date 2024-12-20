# def function_name(context):
    
    type = ""

    if 'ome2_railway_type_type' in context['data']:
        type = str.lower(context['data']['ome2_railway_type_type'])
    if 'type' in context['data']:
        type = str.lower(context['data']['type'])

    # If a link is provided in the attribute, we keep the last part only
    if type.startswith("http"): 
        pos = str.rfind("type", "/")
        if pos == -1:
            pos = str.rfind("type", "\\")
        if pos != -1:                                   
            type = type[pos+1]

    # If the type is "train", we check if it could be further refined into "main_line_train" or "branch_line_train" with the ome2_railway_class_railwayclass attribute
    if type == "train":
        railwayclass = ""
        if 'ome2_railway_class_railwayclass' in context['data']:
            railwayclass = str.lower(context['data']['ome2_railway_class_railwayclass'])
            if railwayclass.startswith("http"): 
                pos = str.rfind("railwayclass", "/")
                if pos == -1:
                    pos = str.rfind("railwayclass", "\\")
                if pos != -1:                                   
                    railwayclass = railwayclass[pos+1]

        if railwayclass == "main line" or railwayclass == "mainline":
            return "main_line_train"
        if railwayclass == "branch-line" or railwayclass == "branch line" or railwayclass == "branchline":
            return "branch_line_train"
        else:
            return "train"

    # Other cases
    if type != "" and type is not None and type in ["funicular","metro","monorail","tramway"]:
        return type
    if type == "cograilway":
        return "cog_railway"
    if type == "magneticlevitation":
        return "magnetic_levitation"
    if type == "suspendedrail":
        return "suspended_rail"
    return "void_unk"