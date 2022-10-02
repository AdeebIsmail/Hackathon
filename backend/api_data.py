from flask import Flask
from flask_cors import CORS
from flask import request
import requests
import json
arrival = ''
destination = ''
num_adults = ''
departure_date = ''
arrival_date = ''
api = Flask(__name__)
CORS(api)
@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    return response_body

@api.route('/data/<arrival>&<destination>')
def run_api(arrival,destination):   
    print(arrival)
    print(destination)
    x = arrival[8:len(arrival)]
    y = destination[12:len(destination)]
    url = "https://priceline-com-provider.p.rapidapi.com/v2/flight/departures"
    querystring = {"sid": "iSiX639", "departure_date": "2022-10-05", "adults": 1,
                   "origin_airport_code": x, "destination_airport_code": y}

    headers = {
        "X-RapidAPI-Key": "75b97bcf14msh05aaf11d45af270p144a1djsn97dba5f65bc6",
        "X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com"
        
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
  
    y = json.loads(response.text)
    airlineData = y['getAirFlightDepartures']['results']['result']['airline_data']
    returnA = []

    for x in airlineData.keys():
        returnA.append(airlineData[x]['name'])
    print(returnA)
    return returnA
