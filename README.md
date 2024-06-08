---
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

- Python 3.7+
- Pip
- Other listed in requirements.txt

## Running

- Clone the repo using https://github.com/edwintea/feedback.git

```bash
git clone 
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Setting up environment variables

| Key     | Value |
| ----------- | ----------- |
| DATABASE_URL   | postgresql://postgres:sa@host:port/db|

- To run the project

```bash
python -m uvicorn main:app --reload
```

============= FRONT END WITH VUEJS==========================
#requirements:
node v20.11.1
vue 2.7.16

====run command ========
cd feedback
npm install

== running application==
npm run dev
#open in browser :



== run via docker =========
docker build -t feedback ./


