def current_track_data(input: dict) -> dict:
    output = {}
    input = input["graph"]
    output["current_lap"] = input["TrackStatus"][-2]
    output["track_status"] = input["TrackStatus"][-1]
    
    return output