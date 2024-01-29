# Employee Management System
Employee Management System - Python & Flask CRUD App

## Summary

This project's purpose was to skills in full-stack development, focusing on creating a robust and user-friendly employee management system.

The application serves as an efficient tool to manage employee records by allowing the addition of new employees, storing and updating their information, and also facilitating the deletion of records as needed.

Built using Python and the Flask framework, this web application offers a seamless and intuitive user interface. The backend is powered by MySQL, with SQLAlchemy as the ORM (Object-Relational Mapping) tool.

## Setup
Clone directory:
```
$ cd [workspace folder]
$ git clone https://github.com/johanfortus/Employee-Management-System.git
```

Create Python virtual environment:
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Start XAMPP and create a database
- Open XAMPP Control Panel and start Apache and MySQL services.
- Create a new database named `crud` through phpMyAdmin.

Initialize the database with Flask:
```
python
from app import app, db
with app.app_context():
    db.create_all()
exit()
```

Start server:
```
(venv) $ flask run
```

Open http://localhost:5000/ to view project in the browser.


## Built With

- <img src="https://img.shields.io/badge/-Python-blue?style=for-the-badge&logo=python&logoColor=FFFF2E" />
- <img src="https://img.shields.io/badge/-Flask-black?style=for-the-badge&logo=flask" />
- <img src="https://img.shields.io/badge/bootstrap-%237952B3.svg?&style=for-the-badge&logo=bootstrap&logoColor=white" />
- <img src="https://img.shields.io/badge/mysql-%23316192.svg?style=for-the-badge&logo=mysql&logoColor=white" /> 

## Demonstration

<img src="https://github.com/johanfortus/Employee-Management-System/blob/main/Assets/EmployeeManagementDemo.gif" /> 
