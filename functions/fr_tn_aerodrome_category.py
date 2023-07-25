# def function_name(context):
    
    category = context['data']['categorie']

    if category == "Nationale":
        return "domestic_national"

    if category == "Internationale":
        return "international"

    return "void"