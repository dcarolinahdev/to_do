# A to-do list app in Flask

# Versions

    Flask 2.1.3

You can see complete list in requirements.txt.

# How to run this app in localhost?

1. Create and activate your virtualenv with python version 3.8.10

2. Run

```
pip install -r requirements.txt
```

3. Run

```
./flask_script.sh
```

This command run `flask run`... remember to chmod with 774 like this `sudo chmod 774 flask_script.sh`

**Environment variable**

    For debugging mode: `FLASK_DEBUG=1`
    For work in development environment: `FLASK_ENV=development`
    For define main file: `FLASK_APP=main.py`

## How to run tests

```
flask test
```

[please read this other README (from Flask basic project)](https://github.com/dcarolinahdev/py_flask_hello_world/blob/main/README.md)
