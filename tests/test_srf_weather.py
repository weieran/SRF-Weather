import json
import unittest
import os
from srf_weather.weather import Weather, convert_json_forecast_to_class


def guard_client_id_secret():
    print(os.environ.get("POETRY_SRF_METEO_CLIENT_ID"))
    print(os.environ.get("POETRY_SRF_METEO_CLIENT_SECRET"))
    srf_client_id = os.environ.get("SRF_METEO_CLIENT_ID")
    srf_client_secret = os.environ.get("SRF_METEO_CLIENT_SECRET")
    if srf_client_id is None or srf_client_secret is None:
        raise unittest.SkipTest("SRF_METEO_CLIENT_ID or SRF_METEO_CLIENT_SECRET not set")
    else:
        return srf_client_id, srf_client_secret


class TestWeather(unittest.TestCase):
    TEST_LOCATION = "Sachseln"
    TEST_LOCATION_ID = "46.8689,8.2391"

    def test_get_access_token(self):
        srf_client_id, srf_client_secret = guard_client_id_secret()

        token = Weather.get_access_token(client_id=srf_client_id, client_secret=srf_client_secret)
        self.assertIsNotNone(token)

    def test_get_geo_location_id(self):
        srf_client_id, srf_client_secret = guard_client_id_secret()

        sachseln = Weather(srf_client_id, srf_client_secret, TestWeather.TEST_LOCATION)
        self.assertIsNotNone(sachseln.geo_location_id)
        self.assertEqual(sachseln.geo_location_id, TestWeather.TEST_LOCATION_ID)

    def test_get_weather_forcast_url(self):
        url = Weather.get_weather_forcast_url(TestWeather.TEST_LOCATION_ID)
        self.assertIsNotNone(url)
        self.assertEqual("https://api.srgssr.ch/srf-meteo/forecast/46.8689%2C8.2391", url)

    def test_get_weather_forecast(self):
        srf_client_id, srf_client_secret = guard_client_id_secret()

        sachseln = Weather(srf_client_id, srf_client_secret, TestWeather.TEST_LOCATION)
        forecast = sachseln.get_weather_forecast(Weather.ForecastDuration.hour)
        print(forecast)
        self.assertIsNotNone(forecast)


class test_convert_json_to_weather_forecast(unittest.TestCase):
    # load json from file
    # convert json to weather forecast
    # compare weather forecast with expected weather forecast

    testfile = os.path.join(os.path.dirname(__file__), 'weather_day_response.json')
    data = json.load(open(testfile))
    forecast = convert_json_forecast_to_class(data)
    print(forecast)
