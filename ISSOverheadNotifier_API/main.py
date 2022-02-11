import requests
import smtplib
from datetime import datetime
import time

# FILL YOUR OWN EMAIL AND PASSWORD (GMAIL)
my_email = "****"
password = "****"

# Got from https://www.latlong.net/ for Toronto, Canada
MY_LAT = 43.653225
MY_LONG = -79.383186

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
iss_overhead = MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour

while True:
    time.sleep(60)# BONUS: run the code every 60 seconds.
    if iss_overhead:
        if hour < 7 or hour > 17:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="lysoju21@yahoo.com",
                    msg="Subject: ISS Overhead\n\nHey! The ISS is above you in the sky. Look up to see it yourself!"
                )
