# Django RestFrameWork demo

## [GET]ting Started

### Installing Dependencies

#### Python 3.7

- [ ] Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

###### Key Dependencies

- [DJANGO](https://docs.djangoproject.com/en/3.0/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source..
- [Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers) A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python manage.py runserver
```

# API EndPoints

### Users

####### [POST] '/api/auth/register'

```json
- Creates A new user
- Requires username, email, password:
{
    "username":"jhon",
    "email":"jhon@mail.com",
    "password":"testPassword"
}
- Returns:
{
    "user": {
        "id": 4,
        "username": "jhon",
        "email": "jhon@mail.com"
    },
    "token": "64f2d9f88e93f612a0f376a39977b63b26955051b0e1d5c0ad0791d8ae83f71d"
}
- returned token is valid for 10 Hours by default can be changed in settings.py
```

###### [POST] '/api/auth/login'

```
- Requiers username, password:
{
    "username":"jhon",
    "password":"testPassword"
}
- Returns:
{
    "user": {
        "id": 4,
        "username": "jhon",
        "email": "jhon@mail.com"
    },
    "token": "9157a4beccf4485c567619984612d1f654f1ccfdbd763064f1a464c66163afc1"
}
```

###### [POST] '/api/auth/logout'

```
- logout from the current device
- Requires  *Header {"Authorization" : "Token 9157a4beccf4485c567619984612d1f654f1ccfdbd763064f1a464c66163afc1"}
```

###### [POST] '/api/auth/logoutall'

```
- logout form all devices
- Requires  *Header {"Authorization" : "Token 9157a4beccf4485c567619984612d1f654f1ccfdbd763064f1a464c66163afc1"}
```

###### [GET] '/api/auth/user'

```
- Fetchs the quizzes of a sepcifec user
- Requires *Header {"Authorization" : "Token 9157a4beccf4485c567619984612d1f654f1ccfdbd763064f1a464c66163afc1"}
- Returns:{
    "id": 4,
    "username": "jhon",
    "email": "jhon@mail.com"
}
```

### Products's

###### [GET] '/api/products/'

```json
- returns a list of products
```
