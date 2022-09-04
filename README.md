# A to-do list app in Flask

---

> ***v1.1*** - This is an initial project in a learning path.

*Some features*

- It uses blueprints: it's a route series that can be integrated into the main app but from another directory.

- It includes config file.

- It includes forms with FlaskForm.

- The project include some tests.

- It include error handler for 404 and 500 errors.

- It uses templates for views with template inheritance and jinja 2.

- The project doesn't use (currently) any database.

## Versions

```
Flask 2.1.3
Flask-Bootstrap 3.3.7.1
Flask-Testing 0.8.1
Flask-WTF 1.0.1
```

You can see complete list in [requirements.txt](requirements.txt)

## Endpoints

| route | meaning |
| --- | --- |
| / | index site |
| /hello/ | to-do list |
| /login/ | login view |

---
---

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
