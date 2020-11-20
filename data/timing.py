def get_latest_timing(raw_data: dict) -> list:
    """
    Returns timings of each driver in the order of the starting grid.
    """

    output = []
    filtered_data = raw_data["data"]["DR"]

    for index, each_driver in enumerate(filtered_data):
        each_driver = each_driver["O"]
        latest_position = each_driver[4]
        latest_lap_time = each_driver[1]
        latest_sectors = [each_driver[5], each_driver[6], each_driver[7]]
        latest_gap_to_leader = each_driver[9]
        latest_gap_to_front = each_driver[14]

        output.append([latest_position, index, [latest_lap_time, latest_sectors, latest_gap_to_leader, latest_gap_to_front]])
    
    return output


def get_fastest_lap(raw_data: dict) -> list:
    """
    Returns fastest lap/sector times in order of starting grid.
    """

    output = []
    filtered_data = raw_data["data"]["DR"]

    for each_driver in filtered_data:
        each_driver = each_driver["B"]
        fastest_lap = each_driver[1]
        fastest_sectors = [each_driver[4], each_driver[7], each_driver[10]]
        output.append([fastest_lap, fastest_sectors])
    
    return output