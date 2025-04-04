# def function_name(context):
    
    surface_category = ""

    # Retrieve source formofway value
    if 'ome2_road_surface_category_surfacecategory' in context['data']:
        surface_category = context['data']['ome2_road_surface_category_surfacecategory']
        if surface_category != '' and surface_category is not None:
            surface_category = str.lower(surface_category)
        else:
            return "void_unk"

    # If formofway is provided as a link, we keep only the final part
    if surface_category.startswith("http"): 
        pos = str.rfind(surface_category, "/")
        if pos == -1:
            pos = str.rfind(surface_category, "\\")
        if pos != -1:                                   
            surface_category = str.lower(surface_category[pos+1:])

    if surface_category in ["paved", "unpaved"]:
        return surface_category
    
    return "void_unk"