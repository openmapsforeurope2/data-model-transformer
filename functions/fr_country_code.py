# def function_name(context):
    # Les valeurs possibles pour country_code sont:
    # FR, GP, GF, HT, MQ, YT, RE, PM

    #FXX | GLP | GUF | H_T | MTQ | MYT | REU | SPM

    # Bac ou liaison maritime | Bretelle | Chemin | Escalier | Rond-point | Route à 1 chaussée |
    # Route à 2 chaussées | Route empierrée | Sentier | Type autoroutier
    territoire = context['data']['gcms_territoire']

    if territoire == "FXX":
        return "fr"
    if territoire == "GLP":
        return "gp"
    if territoire == "GUF":
        return "gf"
    if territoire == "H_T":
        return "ht"
    if territoire == "MTQ":
        return "mq"
    if territoire == "MYT":
        return "yt"
    if territoire == "REU":
        return "re"
    if territoire == "SPM":
        return "pm"
    
    return ""

