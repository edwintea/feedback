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

- Clone the repo using

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

## Contributors

<table>
	<tr align="center">
		<td>
		Md Hishaam Akhtar
		<p align="center">
			<img src = "https://user-images.githubusercontent.com/58990970/103586688-9cde9700-4f0b-11eb-915c-0d8b9a555159.JPG" width="150" height="150" alt="Md Hishaam Akhtar">
		</p>
			<p align="center">
				<a href = "https://github.com/mdhishaamakhtar">
					<img src = "https://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/>
				</a>
				<a href = "https://www.linkedin.com/in/mdhishaamakhtar">
					<img src = "https://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="LinkedIn"/>
				</a>
			</p>
		</td>
	</tr>
</table>