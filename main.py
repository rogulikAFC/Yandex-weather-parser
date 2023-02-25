from bs4 import BeautifulSoup as bs
import requests


class YandexForecast:
    def __init__(self):
        self.lat = float
        self.lon = float
        self.url = str
        self.urlTemplate = 'https://yandex.ru/pogoda/?lat={lat}&lon={lon}'
        self.forecast = {}

    def set_lat_lon(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def generate_url(self):
        self.url = self.urlTemplate.format(lat=self.lat, lon=self.lon)

    def parse_by_hours(self):
        request = requests.get(self.url)
        html = bs(request.content, 'html.parser')

        for hour_temp in html.select('.fact__hour-elem'):
            time = hour_temp.select('.fact__hour-label')
            temp = hour_temp.select('.fact__hour-temp')
            print(time[0].text, temp[0].text)

            self.forecast[time[0].text] = temp[0].text
