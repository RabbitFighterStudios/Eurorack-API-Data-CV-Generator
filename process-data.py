def map_to_teletype_cv(value, min_input, max_input, min_output=0, max_output=16384):
    return int((value - min_input) * (max_output - min_output) / (max_input - min_input) + min_output)

pressure = get_atmospheric_pressure()
pressure_cv = map_to_teletype_cv(pressure, 950, 1050)

fortnite_users = get_fortnite_users()
fortnite_cv = map_to_teletype_cv(fortnite_users, 0, 1000000)
, 1000000)
