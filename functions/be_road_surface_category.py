# def function_name(context):
    # Les valeurs possibles pour road_surface_category sont:
    # 'paved', 'unpaved'

    # Route revêtue en dur / Route empierrée / Pas applicable
    surftype = context['data']['surftype']

    if surftype == "Route empierrée":
        return "paved"
        
    return "unpaved"
    