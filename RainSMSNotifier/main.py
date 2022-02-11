import requests
import os
from twilio.rest import Client


MY_LAT = 43.653225
MY_LONG = -79.383186
MY_API_KEY = os.environ.get('OWM_API_KEY")
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": MY_API_KEY,
}

r = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
# print(r.status_code)
# print(r.json())

r.raise_for_status()
next12hrs = r.json()['hourly'][:12]

print(next12hrs)
is_rain = False
for hour in next12hrs:
    weather_id = hour['weather'][0]['id']
    if int(weather_id) < 700:
        is_rain = True
        print(weather_id)
if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body = "It's going to rain within the next 12 hours. You should definitely bring an umbrella before heading out if you don't want to become a wet monkey 🦧💦",
            from_=os.environ.get('PHONE_NUMBER_FROM_TWILIO'),
            to=os.environ.get('TARGETED_PHONE_NUMBER')
    )
    print(message.status)
