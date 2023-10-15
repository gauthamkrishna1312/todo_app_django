# GTM TODO App

The GTM TODO App is a simple web application built using Django that allows users to manage their tasks and to-do lists. Users can add, edit, mark as completed, and delete tasks.

## Features

- User Registration and Login
- Create a new task with a title, description, due date, and completion status automatically set as pending while creating a new task
- Edit existing tasks
- Mark tasks as completed
- Delete tasks
- View tasks by different categories: All, Pending, Checked, Expired
- Cancel button to exit the editing mode
- Responsive and user-friendly interface

## Prerequisites

Before running the app locally, make sure you have the following installed on your system:

```bash
- Python 
- Django 
- Git (optional if you want to clone the repository)
```

## Getting Started

### Clone the Repository
You can start by cloning the project's repository from GitHub using the following command:
```bash
git clone https://github.com/yourusername/gtm-todo-app.git
cd gtm-todo-app
```
### Create a Virtual Environment
We recommend using a virtual environment to isolate project dependencies. If you don't have virtualenv installed, you can install it using:
```bash
pip install virtualenv
```
Once virtualenv is installed, you can create and activate a virtual environment as follows:
```bash
python -m venv venv
```
Activate virtualenv <br>
* On windows: <br><br>
    ```bash
    venv\Scripts\activate
    ```
* On Mac/Linux: <br><br>
    ```bash
    source venv/bin/activate
    ```
### Install Dependencies
Install the required Python packages listed in the requirements.txt file using pip:
```bash
pip install -r requirements.txt
```
### Apply Database Migrations
Apply the database migrations to create the necessary database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```
### Create a Superuser (Admin)
To access the admin panel and manage tasks, you can create a superuser account by running the following command:

```bash
python manage.py createsuperuser
```
### Start the Development Server
Now, you can start the Django development server:
```bash
python manage.py runserver
```
The development server will run locally at http://localhost:8000/. You can access the app by opening this URL in your web browser.

## Usage
* Register or log in to your account.
* Add new tasks with a title, description, due date, and completion status.
* Edit existing tasks by clicking the "Edit" button.
* Mark tasks as completed using the checkbox.
* Delete tasks by clicking the "Delete" button.
* View tasks by different categories using the navigation buttons.

### Live Demo
### A live demo of the GTM TODO App is available at https://gtmtodo.onrender.com/
# License
This project is licensed under the MIT License - see the LICENSE file for details.