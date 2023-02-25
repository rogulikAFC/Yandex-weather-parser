from main import YandexForecast

forecast = YandexForecast()

forecast.set_lat_lon(lat=60.055183, lon=30.349606)
forecast.generate_url()
forecast.parse_by_hours()

print(forecast.forecast)
