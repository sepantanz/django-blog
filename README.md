# Django Blog Application

A simple blog application built with Django 4.2 that allows users to perform basic CRUD (Create, Read, Update, Delete) operations on blog posts.

## Features
* Create, Read, Update, and Delete blog posts.
* User authentication system for managing posts.
* Simple and clean user interface for a pleasant blogging experience.
* Customized dashboard

## Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.9 or higher
* Django 4.2
* Git (for cloning the repository)

## Installation
1. Clone the repository to your local machine:
   git clone https://github.com/sepantanz/django-blog.git
2. Navigate to the project directory:
   cd django-blog
3. Create a virtual environment (optional but recommended):
   python -m venv venv
4. Activate the virtual environment:
   * On Windows:
     venv\Scripts\activate
   * On macOS and Linux:
     source venv/bin/activate
5. Install the project dependencies:
   pip install -r requirements.txt
6. Apply migrations to set up the database:
   python manage.py migrate

## Usage
1. Start the development server:
   python manage.py runserver
2. Open your web browser and go to http://localhost:8000 to access the blog application.
3. Register a new account or log in if you already have one.
4. Create, read, update, and delete blog posts as needed.

## Configuration
* You can customize various aspects of the blog application by modifying the settings in the settings.py file. For example, you can change the database, configure static files, or set up email settings.

## Contributing
Contributions are welcome! To contribute to this project, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork on GitHub.
5. Create a pull request from your fork to the main repository.

Please make sure to follow the project's code of conduct and style guidelines.

## License
This project is licensed under the MIT License.


