# Flask Tutorial

Building an API with Flask-RESTful

Inspired by Jake Wright (https://www.youtube.com/watch?v=4T5Gnrmzjak&t=537s&pp=ugMICgJmchABGAE%3D) 

## How to run :
```bash
git clone <this repo>
cd <directory>
python3 -m venv ./venv
. venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Use a custom data structure + put endpoints

- [x] add resource "fruits"
  - [x] add function in app.py
  - [x] add resource in resources/
    done file name myfruits.py
- [x] add array w data (in myfruits.py)

## Add tests

How ?
- [x] import unittest - battery included
- [x] prepare ground
    ```bash
    mkdir tests
    cd tests
    touch __init__.py
    touch test_req.py
    ```
- [x] add test function
- [x] launch test :
  ```python3 -m unittest```

Based on https://dev.to/paurakhsharma/flask-rest-api-part-6-testing-rest-apis-4lla
Documentation : https://docs.python.org/3/library/unittest.html

todo
- create base test case
- split test_req
- chech ```python3 -m unittest``` still test everything

## Add database - use SQL alchemy


1. install Flask-SQLAlchemy
2. ???
3. Profit