import requests
import json
from hotels_api_data import *


#local location data
localLocationCity = ''
localLocationState = ''
localLocationCountry = ''

#destination data
destinationCity = ''
destinationState = ''
destinationCountry = ''

num_adults = ''
departureDate = ''
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

    cityData = y['getAirFlightDepartures']['results']['result']['search_data']['search_0'] # getting city data

    
    global localLocationCity 
    localLocationCity = cityData['origin']['city']

    global localLocationState
    localLocationState = cityData['origin']['state']

    global localLocationCountry
    localLocationCountry = cityData['origin']['country']
    
    global destinationCity 
    destinationCity = cityData['destination']['city']

    global destinationState
    destinationState = cityData['destination']['state']

    global destinationCountry
    destinationCountry = cityData['destination']['country']

    global departureDate
    departureDate = departure_date
    

    airlineData = y['getAirFlightDepartures']['results']['result']['airline_data'] # getting airline data
    allInfo = []

    for x in airlineData.keys():
        temp = []
        temp.append(airlineData[x]['name'])
        temp.append(airlineData[x]['code'])
        temp.append(airlineData[x]['websiteUrl'])
        temp.append(airlineData[x]['phoneNumber'])
        allInfo.append(temp)


    hotelsAndPlanes = []
    hotelsAndPlanes.append(allInfo)
    hotelsAndPlanes.append(getCities(destinationCity, destinationState, destinationCountry, departure_date))
    return hotelsAndPlanes
