# NOTE API

An API that lets users integrate a note management feature into their web apps.

## FUNCTIONALITIES

- All CRUD operations on note management - *Done*

- User Login and Authentication - *Comming Soon*

- Grouping notes together by name and date - *Comming Soon*

## TECHNOLOGIES IN USE.
- [Python (FastAPI)](https://fastapi.tiangolo.com/)
- [Prosgres Database](https://www.postgresqltutorial.com/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)

## FAST API

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It has the following key features: Fast to run: It offers very high performance, on par with NodeJS and Go, thanks to Starlette and pydantic.

This project is built with FastAPI. [User guide intro](https://fastapi.tiangolo.com/tutorial/)

## How to Use

**Step 1:**

Download or clone this repo by using the link below

```
https://github.com/rotex5/NOTES_API.git 
```
**Step 2:**

Navigate to project root directory and execute the following command in terminal to install required dependencies:

```
pip install -r requirements.txt
```

**Step 3:**

Setup environmental variables by creating a "**.env**" file in root directory. Using this suggest format.
```
DATABASE_HOSTNAME= "set database name"
DATABASE_PORT="set database port number"
DATABASE_PASSWORD="set database password"
DATABASE_NAME="set database name"
DATABASE_USERNAME="set database username"

```

**Note:** Please ensure database instance has been setup. 

**Step 4:**

Execute the following commands in root directiory to push database migrations

```
alembic upgrade head
```
**Step 5:**

Execute the following commands to run FASTAPI server 

```
app.main:app --reload 
```

**Step 6:**

Navigate to

```
http://127.0.0.1:8000/
```

or

```
http://127.0.0.1:8000/docs
```
to use fastapi generate documention, as well as test the api.


## Folder Structure
```
NOTES_API/
|-app
    |-routers/
    |-database.py
    |-main.py
|-migrations/
```

## Conclusion

Please, note that project is still in development.

I will be happy to answer any questions that you may have on this project. 🙂

If you liked my work, don’t forget to ⭐ star the repo.
