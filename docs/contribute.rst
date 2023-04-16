Contributing
-----------

In order to develop this package, you need to install the following
tools: \* `poetry <https://python-poetry.org/docs/#installation>`__ \*
`tox <https://tox.readthedocs.io/en/latest/install.html>`__

poetry is used to manage the dependencies and to build the package. tox
is used to run automated tests.

Build
~~~~~

.. code:: bash

   poetry build

Test
~~~~

Tox is used to run automated tests. Tox is configured to run tests for
python 3.8 and 3.10 To run tests, install tox and run ``tox`` in the
root directory of the project. In order to run the tests, the following
environment variables must be set in the poetry environment: \*
``SRF_WEATHER_API_KEY``: The api key to use for the tests \*
``SRF_WEATHER_API_SECRET``: The api secret to use for the tests

.. code:: bash

    pip install tox
    export SRF_WEATHER_API_KEY=****
    export SRF_WEATHER_API_SECRET=****
    tox

Publish
~~~~~~~

To publish the package, you need to have an account on
`pypi.org <https://pypi.org/>`__. You also need to have a token for the
account. To create a token, go to the account settings and create a new
token.

The token must be stored in the poetry config. To do so, run the
following command:

.. code:: bash

    poetry config pypi-token.pypi poetry publish


Documentation
~~~~~~~~~~~~~
poetry run sphinx-build -b html docs/source docs/build