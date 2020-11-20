def current_weather_data(input: dict) -> dict:
    output = {}
    input = input["graph"]["data"]
    output["humidity"] = input["pHumidity"][-1]
    output["is_raining"] = input["pRaining"][-1]
    output["wind_speed"] = input["pWind Speed"][-1]
    output["track_temperature"] = input["pTrack"][-1]
    return output


