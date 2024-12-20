# def function_name(context):
        
    aerodrome_category = ""

    if 'ome2_aerodrome_category_aerodromecategory' in context['data']:
        aerodrome_category = str.lower(context['data']['ome2_aerodrome_category_aerodromecategory'])

    if aerodrome_category is None or aerodrome_category == '':
        return "void_unk"

    # If a link is provided in the attribute, we keep the last part only
    if aerodrome_category.startswith("http"): 
        pos = str.rfind("aerodrome_category", "/")
        if pos == -1:
            pos = str.rfind("aerodrome_category", "\\")
        if pos != -1:                                   
            aerodrome_category = aerodrome_category[pos+1]
    
    
    match aerodrome_category:
        case "domesticnational":
            return "domestic_national"
        case "domesticregional":
            return "domestic_regional"
        case "international":
            return "international"
        case "recreational":
            return "recreational"
        case _:
            return "void_unk"