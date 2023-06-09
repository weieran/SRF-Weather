import logging
from enum import Enum
import requests
from datetime import datetime, timedelta
import urllib.parse


class InvalidTokenException(Exception):
    """Raised when the received access token is invalid """
    pass


class InvalidGeoLocationException(Exception):
    """Raised when the received access token is invalid """
    pass


class InvalidWeatherException(Exception):
    """Raised when the received access token is invalid """
    pass


def return3():
    return 3


class Weather:
    """ Class to get the weather from SRF Meteo for a specific place using the SRF Meteo API
        see also https://developer.srgssr.ch/api-catalog/srf-weather#/Forecast/Forecast%20by%20geolocationid
        In order to use this class, you need to register at https://developer.srgssr.ch/ and create an application.
        The application will provide you with a client_id and a client_secret.
        You can then use these values to instantiate the class.
        The class will automatically update the access token every 7 days.

    """
    TOKEN_VALIDITY_DAY = timedelta(days=7)

    def __init__(self, client_id: str, client_secret: str, location: str):
        self.logger = logging.getLogger(__name__)
        self.client_id = client_id
        self.client_secret = client_secret
        self.last_header_update = None
        self.headers = None
        self.geo_location_id = self.get_geo_location_id(location)

    def _get_headers(self):
        if self.last_header_update is None or self.last_header_update + self.TOKEN_VALIDITY_DAY < datetime.now():
            self.logger.debug("Updating token, as it is older than 7 days")
            self.last_header_update = datetime.now()
            access_token = self.get_access_token(self.logger, self.client_id, self.client_secret)
            self.headers = {'Authorization': f"Bearer {access_token}"}
        return self.headers

    @staticmethod
    def get_access_token(logger: logging.Logger = None, client_id: str = None, client_secret: str = None):
        # Define the authentication API endpoint URL and parameters
        url = "https://api.srgssr.ch/oauth/v1/accesstoken"
        params = {
            "grant_type": "client_credentials"
        }

        # Send a POST request to the authentication API endpoint
        response = requests.post(url, params=params, auth=(client_id, client_secret))
        if not response.ok:
            logger.error(f"Invalid token, response: {response.status_code}  ")
            raise InvalidTokenException

        # Parse the JSON response data
        data = response.json()

        # Extract the access token from the response data
        return data["access_token"]

    def get_geo_location_id(self, location: str):
        # Define the API endpoint URL and parameters
        url = "https://api.srgssr.ch/srf-meteo/geolocationNames"
        params = {"name": location}

        # Send a GET request to the API endpoint
        response = requests.get(url, params=params, headers=self._get_headers())

        if response.status_code != 200:
            self.logger.error(f"Invalid geolocation, response: {response.status_code}  ")
            raise InvalidGeoLocationException

        # Parse the JSON response data
        data = response.json()

        # Extract the location ID from the response data
        geo_location_id = data[0]["geolocation"]["id"]
        self.logger.debug(f"retrieved location data: {data}")
        return geo_location_id

    class ForecastDuration(Enum):
        minutes60 = "60minutes"
        hour = "hour"
        day = "day"

    @staticmethod
    def get_weather_forcast_url(location_id: str):
        url = f"https://api.srgssr.ch/srf-meteo/forecast/{urllib.parse.quote(location_id)}"
        return url

    def get_weather_forecast(self, forcast_duration: ForecastDuration):
        url = self.get_weather_forcast_url(self.geo_location_id)
        params = {"type": forcast_duration.value}

        # Send a GET request to the API endpoint
        response = requests.get(url, params=params, headers=self._get_headers())

        if response.status_code != 200:
            self.logger.error(f"Invalid weather, response: {response.status_code}  ")
            raise InvalidWeatherException

        # Parse the JSON response data
        data = response.json()

        # Extract the forecast data from the response data
        forecast = data["forecast"]

        return forecast

    @staticmethod
    def get_hours_of_sun(forecast):
        sun_h_today = forecast["day"][0]["SUN_H"]
        sun_h_tomorrow = forecast["day"][1]["SUN_H"]
        return sun_h_today, sun_h_tomorrow
