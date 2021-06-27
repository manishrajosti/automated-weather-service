from pyowm import OWM, owm
from twilio.rest import Client
from credentials import account_sid, auth_token, my_twilio_phone, my_phone_number

own = OWM('14d97b9f127c2c5f2154cbf1d955b50f')


forecast = own.weather_manager().weather_at_zip_code("48503", "US")
current_weather = forecast.weather
status = current_weather.status.lower().strip()
humidity = current_weather.humidity
tempreture = current_weather.temp["temp"]
heatindex = current_weather.heat_index
wind = current_weather.wnd["speed"]


def umbNotRequired():

    rain = current_weather.rain

    if len(rain) == 0 or status == "clear":
        return True


def send_sms():
    
    client  = Client(account_sid, auth_token)

    if umbNotRequired():
        client.messages.create(
            from_  = my_twilio_phone,
            to = my_phone_number,
            body = f'''
                    You dont need umbrella today. Today's: \n 1. Sky is {status}. \n 2. Humidity is {humidity}\n 3. Tempreture is {tempreture}\n 4. Heat Index is {heatindex} \n 5. Wind is {wind}.
            
            '''
        )
    else:
        client.messages.create(
            from_  = my_twilio_phone,
            to = my_phone_number,
            body = f'''
                    Alert!!! You need umbrella today. Today's: \n 1. Sky is {status}. \n 2. Humidity is {humidity}\n 3. Tempreture is {tempreture}\n 4. Heat Index is {heatindex} \n 5. Wind is {wind}.
            
            '''
        )

if __name__ == "__main__":
    send_sms()