import requests


def get_weather_info(city: str, token: str, lang: str="ru"):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/find?q=Biysk&type=like&APPID={token}",
                params={'q': city, 'lang': lang, 'units': 'metric'})

    return res.json()["list"][0]
