# def function_name(context):

    land_cover_type = "land_area"

    lake_area = float(context['data']['see_flaeche'])

    land_area = 0
    if 'landesflaeche' in context['data']:
        land_area = float(context['data']['landesflaeche'])
    elif 'kantonsflaeche' in context['data']:
        land_area = float(context['data']['kantonsflaeche'])
    elif 'bezirksflaeche' in context['data']:
        land_area = float(context['data']['bezirksflaeche'])
    elif 'gem_flaeche' in context['data']:
        land_area = float(context['data']['gem_flaeche'])

    if lake_area == land_area:
        land_cover_type = "inland_water"

    return land_cover_type
