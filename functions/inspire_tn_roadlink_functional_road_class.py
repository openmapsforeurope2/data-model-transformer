# def function_name(context):

    frc_source = ""
    if 'functionalroadclass' in context['data']:
        frc_source = context['data']['functionalroadclass']
    elif 'ome2_functional_road_class_functionalclass' in context['data']:
        frc_source = context['data']['ome2_functional_road_class_functionalclass']

    print ("frc_source = " + frc_source)

    if frc_source is None or frc_source == '':
        return "void_unk"
    else:
        frc_source = str.lower(frc_source) 

    if frc_source == "":
        return "void_unk"

    if frc_source == "mainroad":
        return "main_road"

    if frc_source == "firstclass":
        return "first_class"

    if frc_source == "secondclass":
        return "second_class"

    if frc_source == "thirdclass":
        return "third_class"

    if frc_source == "fourthclass":
        return "fourth_class"

    if frc_source == "fifthclass":
        return "fifth_class"

    if frc_source == "sixthclass":
        return "sixth_class"

    if frc_source == "seventhclass":
        return "seventh_class"

    if frc_source == "eighthclass":
        return "eighth_class"

    if frc_source == "ninthclass":
        return "ninth_class"

    return "void_unk"