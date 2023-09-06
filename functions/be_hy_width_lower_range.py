# def function_name(context):

    width = context['data']['width']

    if width == 1:
        return "0"

    if width == 2:
        return "1"

    if width == 3:
        return "2"

    if width == 4:
        return "3"  
 
    if width == 5:
        return "4"

    if width == 6:
        return "5"

    if width == 7:
        return "6"

    if width == 8:
        return "15"

    if width == 9:
        return "25"

    if width == 10:
        return "50"

    return "-32768"
