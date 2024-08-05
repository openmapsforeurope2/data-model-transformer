# def function_name(context):

    objektart = context['data']['objektart']

    if objektart == "Autostrasse" or objektart == "Autobahn":
        return "main_road"

    if objektart == "10m Strasse" or objektart == "8m Strasse":
        return "first_class"

    if objektart == "6m Strasse":
        return "second_class"

    if objektart == "4m Strasse":
        return "third_class"

    if objektart == "3m Strasse":
        return "fourth_class"

    if objektart == "2m Weg":
        return "fifth_class"

    if objektart == "1m Weg":
        return "sixth_class"

    if objektart == "2m Wegfragment":
        return "seventh_class"

    if objektart == "1m Wegfragment":
        return "eighth_class"

    return "void_unk"