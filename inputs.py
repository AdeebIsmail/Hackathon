
from api_testing import run_api

arrival = input('enter home airport: ')
destination = input('enter destination airport: ')
num_adults = input('enter number of adults: ')
departure_date = input('enter departure date: ')



run_api(arrival,destination,departure_date,num_adults)