import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from geopy.geocoders import Nominatim
high = ""
length = ""
number = "+359885988811"

my_number = phonenumbers.parse(number)
print(geocoder.description_for_number(my_number, "en"))

time_zone = timezone.time_zones_for_number(my_number)
print(time_zone)

operator = carrier.name_for_number(my_number, "en")
print(operator)

country_code = "+" + str(my_number.country_code)

geolocator = Nominatim(user_agent="geo_locator")
location = geolocator.geocode(country_code)

if location:
    length = location.longitude
    high = location.latitude
    print(f"Location for {number}: Latitude {location.latitude}, Longitude {location.longitude}")
else:
    print(f"Location for {number} not found.")

