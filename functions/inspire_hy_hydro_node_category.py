# def function_name(context):
        
    category = ""

    if 'hydronodecategory' in context['data']:
        category = context['data']['hydronodecategory']

    if category is None or category == '':
        return "void_unk"
    else:
        category = str.lower(category) 

    # If a link is provided in the attribute, we keep the last part only
    if category.startswith("http"): 
        pos = str.rfind(category, "/")
        if pos == -1:
            pos = str.rfind(category, "\\")
        if pos != -1:                                   
            category = str.lower(category[pos+1:])

    if category == "flowconstriction":
        return "flowconstriction"

    if category == "flowregulation":
        return "flowregulation"

    if category in ["boundary", "junction", "outlet", "source"]:
        return category

    return "void_unk"