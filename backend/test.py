<<<<<<< HEAD
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
=======
from flask import Flask

api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body

@api.route('/data')
def flightdata():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
>>>>>>> 3ed1671a73636f0de8f3d3b3410866d8e9e4761e
