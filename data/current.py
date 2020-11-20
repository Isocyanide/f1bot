import requests
import datetime


def clean_data(input: dict) -> dict:
    output = {}
    output["race_name"] = input["Meeting"]["Name"]
    output["location"] = input["Meeting"]["Location"]
    output["ongoing"] = datetime.datetime.strptime(input["EndDate"], '%Y-%m-%dT%H:%M:%S') > datetime.datetime.now()
    output["path"] = input["Path"]
    return output

def current_session_info():
    session_url = "https://livetiming.formula1.com/static/SessionInfo.json"
    data = requests.get(session_url).json()
    return clean_data(data)


print(current_session_info())