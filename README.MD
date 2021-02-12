### Commands:

1) check version = `python --version/ pytest --version/ pipenv --version`
2) after downloaded project to pull dependencies = `pipenv install`
2) to run all tests = `pipenv run python -m pytest`
3) to install pipenv = `pip install pipenv`
4) download extension for pytest = `pipenv install pytest-***`
5) to run test module = `pipenv run python -m pytest folder/test_***.py`
6) to run a specific test = `pipenv run python -m pytest folder/test_***.py::test_***`
7) to run pytest in parallel = `pipenv run python -m pytest -n 3(before that is required to install pytest-xdist)`
8) to run particular test by regex
   = `pipenv run python -m pytest folder/test_***.py -k "text contained in name of function"`
9) set up retry analyzer = `pipenv install pytest-rerunfailures`