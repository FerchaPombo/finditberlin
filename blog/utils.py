
# Utility functions fot getting the location from the adress field to latitude and longitude

import googlemaps
from django.conf import settings

def get_google_maps_data(street_name, street_number, city):
    address = f"{street_number} {street_name}, {city}"

    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    geocode_result = gmaps.geocode(address)

    if geocode_result:
        formatted_address = geocode_result[0]['formatted_address']
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']

        return formatted_address, latitude, longitude

    return None, None, None
