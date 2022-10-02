import requests
import json


def getCities(name, state, country, checkIn):

    temp = int(checkIn[-2] + checkIn[-1])
    num = len(checkIn) - 2
    temp += 7
    checkOut = checkIn[0: num] + str(temp)
    
    url = "https://priceline-com-provider.p.rapidapi.com/v1/hotels/locations"

    querystring = {"name":name,"search_type":"CITY"}

    headers = {
        "X-RapidAPI-Key": "75b97bcf14msh05aaf11d45af270p144a1djsn97dba5f65bc6",
        "X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    y = json.loads(response.text)

    city = ''
    stateC = ''
    count = ''
    id = ''

    for x in range(len(y)):
        city = y[x]['cityName']
        stateC = y[x]['stateCode']
        count = y[x]['countryName']
        id = y[x]['id']

        if city == name:
            if stateC == state:
                if count == country.upper():
                    break

    return getHotels(checkIn, checkOut, id)



def getHotels(checkIn, checkOut, id):
    url = "https://priceline-com-provider.p.rapidapi.com/v1/hotels/search"

    querystring = {"sort_order":"STAR","location_id":id,"date_checkout":checkOut,"date_checkin":checkIn,"rooms_number":"1"}

    headers = {
        "X-RapidAPI-Key": "75b97bcf14msh05aaf11d45af270p144a1djsn97dba5f65bc6",
        "X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    y = json.loads(response.text)

    arrHotels = []

   for x in range(0, int(len(y['hotels'])/10)):
        temp = []
        if u'name' in y['hotels'][x]:
            temp.append(y['hotels'][x][u'name'])
        #if u'hotelId' in y['hotels'][x]:
         #   temp.append(y['hotels'][x][u'hotelId'])
        #if u'address' in y['hotels'][x]['location']:
         #   adre = list(y['hotels'][0]['location']['address'].values())
         #   temp.append(adre[0] + ', ' + adre[1] + ' ' + adre[2] + ', ' + adre[3] + ', ' + adre[5])
        if u'ratesSummary' in y['hotels'][x]:
            temp.append(y['hotels'][x]['ratesSummary']['minPrice'])

        if temp: 
            arrHotels.append(temp)
    return arrHotels
