# Django Blog Project
## Overview
This project is a blog designed with the Django framework. It allows users to sign up, log in, and interact with posts in various ways. Users can create new posts, add topics, view post details, comment on posts, and edit or delete posts if they have the necessary permissions. Additionally, clicking on a post's topic will navigate to a page listing all posts associated with that topic. 
## Features
- User authentication (sign up and login).
- Ability to create, view, edit, and delete posts.
- Functionality to add and view comments on posts.
- Topic-based post organization and navigation. 
- Responsive web design for an optimal viewing experience across a wide range of devices.
- ## Requirements
- All required libraries are listed in the requirements.txt file. Install them using the following command: 
```
pip install -r requirements.txt
```

## Configuration 
Before running the application, you must configure your local settings. Copy sample_setting.py to local_setting.py and follow the instructions within to set up your database connection and other necessary settings. ## Setting Up the Database Run the following commands to set up your database: 
```
python manage.py makemigrations
```
```
python manage.py migrate
```

## Running the Application
To start the server, run: 
```
python manage.py runserver
```

Navigate to http://127.0.0.1:8000/ in your web browser to view the application. ## Admin Panel To create an admin user, run: 
```
python manage.py createsuperuser
```

Follow the prompts to set up your username and password. You can then log in to the admin panel by navigating to http://127.0.0.1:8000/admin/.
## Contributing
Contributions to this project are welcome. Please feel free to fork the repository, make your changes, and submit a pull request. 
