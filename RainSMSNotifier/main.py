import requests
from twilio.rest import Client

MY_LAT = 42.44
MY_LONG = 96.22
MY_API_KEY = '0fe0d301f9523cb832dc93c1c6fadcd4'
account_sid = 'AC0fafa1e06487238da818973251f606ee'
auth_token = '7517aa6511c3c6c6c1bae3946d68e097'

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
            from_='+18456979659',
            to='+12676214004'
    )
    print(message.status)
