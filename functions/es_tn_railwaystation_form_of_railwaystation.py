# def function_name(context):

    ome2_nodoffcc = context['data']['ome2_nodoffcc']
    tipo_estfc = context['data']['tipo_estfc']

    name_list = ""

    if tipo_estfc == 3:
        return "railway_station"

    for nodo in ome2_nodoffcc:
        tipo_nodo = nodo['tip_nodofc']

        if tipo_nodo == 1:
            return "junction"
        
        if tipo_nodo == 5:
            return "railway_stop"
        
        intermodal = nodo['intermodal']
        if intermodal == 1:
            return "intermodal_rail_transport_terminal"
    
    return "void_unk"


