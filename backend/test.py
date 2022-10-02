import requests
import json

arrival = ''
destination = ''
num_adults = ''
departure_date = ''
arrival_date = ''




def run_api(arrival, destination, departure_date,num_adults):
    url = "https://priceline-com-provider.p.rapidapi.com/v2/flight/departures"

    querystring = {"sid": "iSiX639", "departure_date": departure_date, "adults": num_adults,
                   "origin_airport_code": arrival, "destination_airport_code": destination}

    headers = {
        "X-RapidAPI-Key": "75b97bcf14msh05aaf11d45af270p144a1djsn97dba5f65bc6",
        "X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    y = json.loads(response.text)
    airlineData = y['getAirFlightDepartures']['results']['result']['airline_data']
    returnA = []

    for x in airlineData.keys():
        returnA.append(x)
    print(returnA)
