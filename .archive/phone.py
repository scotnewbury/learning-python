import phonenumbers
from phonenumbers import timezone
from phonenumbers import carrier
from phonenumbers import geocoder

# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx

phone_number = input('Please enter your phone number including country code: ')
phone_number_parsed = phonenumbers.parse(phone_number, 'en')
phone_number_timezone = timezone.time_zones_for_number(phone_number_parsed)
phone_number_carrier = carrier.name_for_number(phone_number_parsed, 'en') # doesn't seem to work with US numbers
phone_number_geocode = geocoder.description_for_number(phone_number_parsed, 'en')

# Print some of the information about the phone number
print(phone_number_parsed)
print(phone_number_timezone)

if phone_number_carrier == '':
  print('No carrier information found.')
else:
  print(phone_number_carrier)

print(phone_number_geocode)
