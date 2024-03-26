# def function_name(context):

    bezirks_code = str(context['data']['bezirksnummer'])

    if bezirks_code == "" or bezirks_code == None :
        bezirks_code = "0000"
    if len(bezirks_code) == 3:
        bezirks_code = "0{0}".format(bezirks_code)

    shn_code = "CH{0}00".format(bezirks_code)

    return shn_code

