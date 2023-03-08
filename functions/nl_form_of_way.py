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

    # Main traffic use:
    # Fast traffic  (Snelverkeer), Mixed traffic (Gemengd verkeer), Bus traffic (Busverkeer), 
    # Air traffic (vliegverkeer), Bikes/Mopeds (Fietsers/bromfietsers), Pedestrian (Voetgangers), 
    # Rider (Ruiter), Parking (parkeren), Parking: P+R (Parkeren P+R), Parking: Carpool (Carpoolplaats),
    # Other (Overig), Unkown (Onbekend)
    Hoofdverkeersgebruik = context['data']['hoofdverkeersgebruik']

    # Separate lancourt
    # Yes, No
    gescheidenrijbaan = context['data']['gescheidenrijbaan']

    if typeweg == "Autosnelweg":
        return "motorway"
    if gescheidenrijbaan == "Yes":
        return "dual_carriage_way"
    if gescheidenrijbaan == "No":
        return "single_carriage_way"
    if Hoofdverkeersgebruik == "Voetgangers":
        return "walkway" 
    
    return "single_carriage_way"
