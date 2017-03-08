from weather import Weather
weather = Weather()

"""
Taking advantage of the weather api to get the weather for Nairobi kenya.  
Lookup weather via weather.yahoo.com
"""

def get_weather(list_of_cities):
    for cities in list_of_cities:
        location = weather.lookup_by_location(cities)
        condition = location.condition()
    print condition['text']

list_of_cities = ['Nairobi', 'Lagos', 'Newyork', 'Kampala']    

print get_weather(list_of_cities) 