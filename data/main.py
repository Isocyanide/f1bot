import data
import requests
from collections import OrderedDict


def match_data_to_driver(starting_grid: dict, current_timing: list, fastest_timing: list, tire_history: list, all_drivers: dict) -> OrderedDict:
    ordered_timing = sorted(current_timing)
    result = OrderedDict()

    for each_driver in ordered_timing:
        driver_index = each_driver[1]
        driver_initials = starting_grid[driver_index]

        result[driver_initials] = each_driver[2], fastest_timing[driver_index], tire_history[driver_index], all_drivers[driver_initials]
    
    return result


def get_data():
    current = data.current_session_info()
    output = []

    latest_data = requests.get("https://livetiming.formula1.com/static/" + current["path"] + "SPFeed.json").json()
    output.append(data.current_weather_data(latest_data["Weather"]))
    output.append(data.current_track_data(latest_data["Scores"]))

    all_drivers = data.all_drivers(latest_data["init"])
    starting_grid = data.starting_grid(latest_data["init"])

    latest_timing = data.get_latest_timing(latest_data["opt"])
    fastest_lap = data.get_fastest_lap(latest_data["best"])
    tire_history = data.get_tire_history(latest_data["xtra"])
    current_grid = match_data_to_driver(starting_grid, latest_timing, fastest_lap, tire_history, all_drivers)

    output.append(current_grid)

    return output