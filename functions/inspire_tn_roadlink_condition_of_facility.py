# def function_name(context):
    
    condition_of_facility = ""

    # Retrieve source formofway value
    if 'ome2_condition_of_facility_currentstatus' in context['data']:
        condition_of_facility = context['data']['ome2_condition_of_facility_currentstatus']
        if condition_of_facility != '' and condition_of_facility is not None:
            condition_of_facility = str.lower(condition_of_facility)
        else:
            return "void_unk"

    # If ome2_condition_of_facility_currentstatus is provided as a link, we keep only the final part
    if condition_of_facility.startswith("http"): 
        pos = str.rfind("condition_of_facility", "/")
        if pos == -1:
            pos = str.rfind("condition_of_facility", "\\")
        if pos != -1:                                   
            condition_of_facility = condition_of_facility[pos+1]

    if condition_of_facility in ["disused", "functional", "projected", "decommissioned"]:
        return condition_of_facility
    
    if condition_of_facility == "underconstruction":
        return "under_construction"

    return "void_unk"