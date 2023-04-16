# SRF Weather
Wrapper around the SRF freemium API (https://developer.srgssr.ch/api-catalog/srf-weather/srf-weather-description)
For api definition see also https://developer.srgssr.ch/api-catalog/srf-weather


## Installation
~~~ bash
pip install srf-weather
~~~

## Development
In order to develop this package, you need to install the following tools:
* [poetry](https://python-poetry.org/docs/#installation)
* [tox](https://tox.readthedocs.io/en/latest/install.html)

poetry is used to manage the dependencies and to build the package.
tox is used to run automated tests.


### Build
~~~ bash
poetry build
~~~

### Test
Tox is used to run automated tests. Tox is configured to run tests for python 3.8 and 3.10
To run tests, install tox and run `tox` in the root directory of the project.
In order to run the tests, the following environment variables must be set in the poetry environment:
* `SRF_WEATHER_API_KEY`: The api key to use for the tests
* `SRF_WEATHER_API_SECRET`: The api secret to use for the tests
~~~ bash
pip install tox
export SRF_WEATHER_API_KEY=<api_key>
export SRF_WEATHER_API_SECRET=<api_secret>
tox
~~~

### Publish
To publish the package, you need to have an account on [pypi.org](https://pypi.org/).
You also need to have a token for the account. To create a token, go to the account settings and create a new token.

The token must be stored in the poetry config. To do so, run the following command:
~~~ bash
poetry config pypi-token.pypi <token>
poetry publish
~~~



