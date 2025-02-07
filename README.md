HazieOlu Task Management App
============================

### Introduction

HazieOlu is a simple and efficient task management web application built using Flask and MySQL. It allows users to register, log in, and manage their tasks in an organized manner. With HazieOlu, you can add, edit, and mark tasks as completed seamlessly.


### Setting Up the MySQL Database

Before running the application, you need to set up the MySQL database. Follow these steps:

Create a designated user and database for the application using:
```bash
cat mysql_dev_setup.sql | mysql -uroot -p
```

### Generating a Unique Secret Key

To ensure session security, generate a unique secret key using:
```bash
./generate_key.py
```

Update your .env file with the database parameters and secrete key.

### Running the App

Install dependencies:
```bash
pip install -r requirements.txt
```

Set up environment variables (optional, if using .env file).

Run the Flask application:

```bash
python3 app.py
```
Open your browser and go to: http://127.0.0.1:5000


### Register as a User

- Click on Register.

- Fill in your details (Username, Email, Password).

- Click Register.

- You will be redirected to the login page.


### Login

- Enter your registered email and password.

- Click Login.

- You will be taken to your task dashboard.


### Start Adding Tasks

- Click on Add Task.

- Enter task details:

	- Title

	- Description

	- Priority

	- Deadline

- Click Save Task.

- Your task will be added and displayed on your dashboard.

- Check the task checkbox to mark it as completed.

- Use the Edit button to update a task.


### Watch How Your Tasks Organize Themselves!

HazieOlu sorts and organizes your tasks based on their status as active, behind schedule and completed tasks. Completed tasks are marked separately for better clarity, helping you stay productive!

Enjoy using HazieOlu to keep track of your tasks efficiently! 🚀


#### AUTHOR:
- Johnkennedy Umeh
