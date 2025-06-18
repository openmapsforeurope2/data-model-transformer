# def function_name(context):

    spelling = ""
    label = ""

    list_name_attributes = ['nimi_suomi', 'namefin', 'nimi_ruotsi', 'nameswe', 'nimi_pohjoissaame', 'nimi_inarinsaame', 'nimi_koltansaame'  ]

    if "ome2_targetcode" in context['data']:
        targetcode = context['data']['ome2_targetcode']

        if targetcode == '2' or targetcode == '3': #Swedish name first
            list_name_attributes = ['nimi_ruotsi', 'nameswe', 'nimi_suomi', 'namefin', 'nimi_pohjoissaame', 'nimi_inarinsaame', 'nimi_koltansaame' ]

    list_spelling = []

    for name_att in list_name_attributes:
        spelling = ""
        if name_att in context['data']:
            spelling = context['data'][name_att]

        if spelling in list_spelling:
            continue

        if spelling is not None and spelling != '' :
            label = label + '#' + spelling
            list_spelling.append(spelling)

    if label is not None and label != "":
        label = label[1:]
    else:
        label = "void_unk"

    return label       