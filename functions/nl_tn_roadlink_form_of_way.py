# def function_name(context):
    # Les valeurs possibles pour form_of_way sont:
    # 'bicycle_road', 'dual_carriage_way', 'enclosed_traffic_area', 'entrance_or_exit_car_park', 
    # 'entrance_or_exit_service', 'freeway', 'motorway', 
    # 'pedestrian_zone', 'roundabout', 'service_road', 'single_carriage_way', 
    # 'slip_road', 'tractor', 'traffic_square', 'walkway'

    # Road-type:
    # Highway (Autosnelweg), Main road (Hoofdweg), Regional road (Regionale weg), Local road (Lokale weg), 
    # Street (Straat), Runway (Start/landingsbaan), PlatformOther road (Overige weg), Unknown (Onbekend)
    typeweg = context['data']['typeweg']
    if typeweg == "autosnelweg":
        return "motorway"


    # Main traffic use:
    # Fast traffic  (Snelverkeer), Mixed traffic (Gemengd verkeer), Bus traffic (Busverkeer), 
    # Air traffic (vliegverkeer), Bikes/Mopeds (Fietsers/bromfietsers), Pedestrian (Voetgangers), 
    # Rider (Ruiter), Parking (parkeren), Parking: P+R (Parkeren P+R), Parking: Carpool (Carpoolplaats),
    # Other (Overig), Unkown (Onbekend)
    hoofdverkeersgebruik = context['data']['hoofdverkeersgebruik']

    if hoofdverkeersgebruik == "snelverkeer":
        return "freeway"
    if hoofdverkeersgebruik == "fietsers, bromfietsers":
        return "bicycle_road"
    if hoofdverkeersgebruik == "voetgangers":
        return "pedestrian_zone" 


    # Roundabouts and slip roads
    fysiekvoorkomen = context['data']['fysiekvoorkomen']

    if fysiekvoorkomen == "op rotonde":
        return "roundabout"
    if fysiekvoorkomen == "op oprit / afrit":
        return "slip_road"


    # Separate lancourt
    # Yes, No
    gescheidenrijbaan = context['data']['gescheidenrijbaan']
    if gescheidenrijbaan == "ja":
        return "dual_carriage_way"
    if gescheidenrijbaan == "nee":
        return "single_carriage_way"

    # Possible value: bus lane. To be placed before the test on gescheidenrijbaan if we want to retrieve them
    if hoofdverkeersgebruik == "busverkeer":
        return "void_bus_lane"

    return "void_unk"
