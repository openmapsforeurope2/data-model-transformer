# def function_name(context):
    
    surface_category = ""

    # Retrieve source formofway value
    if 'ome2_road_surface_category_surfacecategory' in context['data']:
        surface_category = str.lower(context['data']['ome2_road_surface_category_surfacecategory'])

    # If formofway is provided as a link, we keep only the final part
    if surface_category.startswith("http"): 
        pos = str.rfind("surface_category", "/")
        if pos == -1:
            pos = str.rfind("surface_category", "\\")
        if pos != -1:                                   
            surface_category = surface_category[pos+1]

    if surface_category in ["paved", "unpaved"]:
        return "surface_category"
    
    return "void_unk"