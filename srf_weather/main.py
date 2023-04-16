from srf_weather.weather import Weather
import os
import sys


def main():
    srf_client_id = os.environ.get("SRF_METEO_CLIENT_ID")
    srf_client_secret = os.environ.get("SRF_METEO_CLIENT_SECRET")

    sachseln = Weather(srf_client_id, srf_client_secret, "Sachseln")
    forecast = sachseln.get_weather_forecast(Weather.ForecastDuration.hour)
    print(forecast)
    sys.exit()


if __name__ == '__main__':
    main()
