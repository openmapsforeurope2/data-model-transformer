# def function_name(context):

    national_code = str(context['data']['kantonsnummer'])
    if national_code == "" or national_code == None :
        national_code = "00"

    shn_code = ""
    if len(national_code) == 1:
        shn_code = "CH0{0}000000".format(national_code)
    else:
        shn_code = "CH{0}000000".format(national_code)

    return shn_code

