def all_drivers(input: dict) -> dict:
    output = {}
    input = input["data"]["Drivers"]
    for each_driver in input:
        output[each_driver["Initials"]] = (each_driver["FirstName"] + " " + each_driver["LastName"], each_driver["Team"], each_driver["Num"])
    
    return output


def starting_grid(input: dict) -> list:
    output = []
    input = input["data"]["Drivers"]

    for each_driver in input:
        output.append(each_driver["Initials"])
    
    return output