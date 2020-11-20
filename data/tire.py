def get_tire_history(raw_data: dict) -> list:
    filtered_data = raw_data["data"]["DR"]
    output = []

    for each_driver in filtered_data:
        tire_history = each_driver["X"][9]
        tire_laps = []
        for index, value in enumerate(tire_history):
            tire_laps.append([value, each_driver["TI"][(3 * index) + 1]])
        
        output.append(tire_laps)
    
    return output
