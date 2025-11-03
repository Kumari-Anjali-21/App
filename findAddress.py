# get address from given log / lat
#pip install geopy

from geopy.geocoders import Nominatim

def location(lat,lon):
    # calling the nominatim tool
    geoLoc = Nominatim(user_agent="GetLoc")
    # passing the coordinates
    locname = geoLoc.reverse(lat+","+lon)

    # printing the address/location name
    return str(locname)