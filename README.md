# GradProjectCode

This is my, Matt Niemiec's, repository for CSCI 5448, Object-Oriented Design and Analysis. My project title is "MVC Paradigm of Web Programming: A Look at Django"
Inside there are two identical websites. One is written in Django, and the other in Flask. Neither website is thorough or pretty, because the purpose of my project is not to show that I can write CSS. Rather, each web site is developed just enough to show structural differences between the two frameworks, and how that would affect the site if the site were to become much, much larger. 

The Django project: I used Python 3.4 to run this project, and Django version 2.0.5. However, the code is so generic that almost any version of Python3 and Django would work. In order to start the program, please navigate to demo/ and type the command "python3 manage.py runserver". The settings are not fully configured as that was more of a convenience to the developer than an OOP principle. The database, the default SQLite, should be included in the code and will run automatically as the site boots up. The admin credentials are "matt" and "mypassword" if you'd like to explore the /admin section

The Flask project: Naturally, the Flask side of things is much more bare-bones. Because Flask doesn't give built-in support for models of any language, I went with the less-structured theme of MongoDB. The database information used is in a subdirectory, /database. Feel free to import this code into your local MongoDB instance in a database called "ooad" and the code will then work under MongoDB's localhost exception. In order to run the project, please nagivate to the main directory and enter "flask run".

Once again, these are very simple projects, and it should be very intuitive how they work, even if you aren't familiar with one or both of the frameworks. Thank you for your interest in my code,

    Matt
