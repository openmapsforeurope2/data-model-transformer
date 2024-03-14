# def function_name(context):

    if context['data']['typelandgebruik'] == "basaltblokken, steenglooiing":
        return "boulders"

    if context['data']['voorkomen'] == "dras, moerassig":
        return "mud"

    if context['data']['typelandgebruik'] == "duin":
        return "sand"

    return "void_unk"
