def dd_to_dms(value, coord_type):

    if coord_type == "lon":
        direction = "E" if value >= 0 else "W"
    else:
        direction = "N" if value >= 0 else "S"

    value = abs(value)

    degrees = int(value)
    minutes_float = (value - degrees) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60

    return [degrees, minutes, round(seconds, 2), direction]


def convert_coordinates(dd_coords):
    
    longitude = dd_coords[0]
    latitude = dd_coords[1]

    lon_dms = dd_to_dms(longitude, "lon")
    lat_dms = dd_to_dms(latitude, "lat")

    return [lon_dms, lat_dms]


dd = [-118.2437, 34.0522]
result = convert_coordinates(dd)

print(result)
