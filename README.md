## Installation

Install Python, NodeJS and Angular
Use the pip package manager [pip](https://pip.pypa.io/en/stable/) to install all the required dependencies.

+ sqlalchemy
+ flask_sqlalchemy
+ flask
+ python-dotenv 
+ Flask-Cors
To install dependencies:
```bash
pip install -U flask-cors
```
Go to the folder of frontend and do
```bash
npm install
```
Set Database URI as Environment variable
E.g in windows:
```bash
export SQLALCHEMY_DATABASE_URI_DEV="databaseURI..." 
```

Make sure that the port of backend in app.py is the same as the port that is configured in frontend. You can set it in frontend in the file: *./frontend/src/environments/environment.prod.ts*

Run Backend: 
```bash
cd src
python app.py
```
Run Frontend:
```bash
cd frontend
npm install
ng serve
```
