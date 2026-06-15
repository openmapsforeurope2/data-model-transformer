# def function_name(context):

    spelling = context['data']['gen']
    language = "ger"
    script = "latn"
    name_status = "void_unk"
    nativeness = "endonym"
    spelling_latn = context['data']['gen']
    display = 1

    name_list = []

    name_list.append({
        "spelling": spelling,
        "language": str.lower(language),
        "script": str.lower(script),
        "name_status": name_status,
        "nativeness": nativeness,
        "spelling_latn": spelling_latn,
        "country": "de",
        "display": display
        })

    return name_list