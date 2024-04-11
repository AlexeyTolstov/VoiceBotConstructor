import requests

class WeatherInfo:
    def __init__(self, data_dict: dict):
        self.id = data_dict["id"]
        self.name = data_dict["name"]
        self.coord = data_dict["coord"]
        
        self.temp = data_dict["main"]["temp"]
        self.temp_min = data_dict["main"]["temp_min"]
        self.temp_max = data_dict["main"]["temp_max"]
        self.feel_like = data_dict["main"]["feels_like"]
        
        self.wind_speed = data_dict["wind"]["speed"]
        self.description = data_dict["weather"][0]["description"]


def get_weather_info(city: str, token: str, lang: str="ru") -> WeatherInfo:
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/find?q={city}&APPID={token}",
            params={'lang': lang, 'units': 'metric', 'type': 'like', })
    
    return WeatherInfo(res.json()["list"][0])


if __name__ == "__main__":
    api_token = "YOUR_TOKEN"
    data = get_weather_info(city="Бийск", token=api_token)