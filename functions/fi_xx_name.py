# def function_name(context):

    spelling = ""
    script = "latn"
    display = 0

    list_name_attributes = ['nimi_suomi', 'namefin', 'nimi_ruotsi', 'nameswe', 'nimi_inarinsaame', 'nimi_koltansaame', 'nimi_pohjoissaame' ]
    
    name_config = {
        "nimi_suomi" :{
            "language": "fin",
            "name_status": "void_unk",
            "nativeness": "void_unk"
        },
        "namefin" :{
            "language": "fin",
            "name_status": "official",
            "nativeness": "endonym"
        },
        "nimi_ruotsi" :{
            "language": "swe",
            "name_status": "void_unk",
            "nativeness": "void_unk"
        },
        "nameswe" :{
            "language": "swe",
            "name_status": "official",
            "nativeness": "endonym"
        },
        "nimi_inarinsaame" :{
            "language": "smn",
            "name_status": "void_unk",
            "nativeness": "void_unk"
        },
        "nimi_koltansaame" :{
            "language": "sms",
            "name_status": "void_unk",
            "nativeness": "void_unk"
        },
        "nimi_pohjoissaame" :{
            "language": "sme",
            "name_status": "void_unk",
            "nativeness": "void_unk"
        }
    }

    name_list = []

    for name_att in list_name_attributes:
        spelling = ""
        if name_att in context['data']:
            spelling = context['data'][name_att]

        if spelling is not None and spelling != '':
            spelling = spelling.replace('\"', '')
            spelling = spelling.replace('"', '') 

            display += 1

            name_list.append({
                "spelling": spelling,
                "language": name_config[name_att]['language'],
                "script": script,
                "name_status": name_config[name_att]['name_status'],
                "nativeness": name_config[name_att]['nativeness'],
                "spelling_latn": spelling,
                "display": display
            })

    return name_list
