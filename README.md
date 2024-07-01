##DEVELOPER: EDWIN WARMING GUNAWAN
##EMAIL : kubilk56@gmail.com
##PHONE:+62 85710583303
##COUNTRY : INDONESIA

## About
with FastAPI.
It uses SQLAlchemy as the ORM. 

## Features

- [x] Database Connection Using SQLAlchemy
- [x] FastAPI Server
- [x] Unit Testing with PyTest
- [x] Basic CRUD for Feedback

## running alembic for db default with feedback table
- go to folder migration then run command : python -m alembic upgrade head

## Dependencies

- Python 3.7.0
- Pip
- PostgreSQL :
    database : postgres
    username : postgres
    password : sa (depend on your local credential)
- Other listed in requirements.txt

## Running

- Clone the repo using 

```bash
git clone https://github.com/edwintea/feedback.git
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Setting up environment variables

| Key     | Value |
| ----------- | ----------- |
| DATABASE_URL   | postgresql://postgres:sa@host:port/db|

- To run the backend

```bash
python -m uvicorn main:app --reload

```

=============================== FRONTEND ==================================
#requirements:
node v20.11.1
vue 2.7.16

=============================== step frontend ==================================
- go to frontend folder
    cd /frontend/feedback
- run command:
    npm install

=============================== RUNNING APPLICATION =======================
- run command:
    npm run dev
- open in browser: 
    http://localhost:5173/
- do click the star for feedback and check the table feedback 

=============================== RUNNING TEST APPLICATION =======================
- go to test folder
- run command : 
    pip install pytest
    python -m pytest test_feedback.py


=============================== RUNNING APPLICATION VIA DOCKER =======================
docker build -t feedback ./


