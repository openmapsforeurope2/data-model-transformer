# def function_name(context):

    frc_source = ""
    if 'functionalclass' in context['data']:
        frc_source = str.lower(context['data']['functionalclass'])

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