CMSC 447- SOFTWARE ENGINEERING INDIVIDUAL ASSIGNEMNT
----------------------CRUD APPLICATION----------------------

This program was coded in and executed with the Pycharm IDE. It can be run on any IDE that supports python and flask
backend development as well as html/css/js frontend development. For a more seamless guide on how to run program, Pycharm
should be your IDE of choice

---FILES INCLUDED---
    App.py
    templates folder, where our html files are held
    static folder, that holds our css and js folders that each hold our bootstrap references

---BACKGROUND INFO------
 This application is a CRUD (Create Read Update Delete) application using Flask, sqlalchemy, mysql database, and html
 frontend development. This application will allow the user to interact with instructor,student,course, and enrollment
 data stored on a local server

------NECESSARY TOOLS AND LIBRARIES----
The database will be hosted locally on a database server. To hose this local database, install the XAMPP application
from the following website: https://www.apachefriends.org/

From there go through the installation process. Start the app up and then press the start button for apache under the
action column. Then do the same for MySQl. Then press the 'Admin' button next to it. It should open up a tab in your
browser with phpMyAdmin open. From there, create a new database named 'crud'. You can name your database something else
you'd like but be sure to change the name in line 9 of the App.py file.

Also be sure to install the following packages:
    mySQL
    flask
    sqlalchemy
    flasksqlalchemy
If you are to follow my method for creating the database, make sure you have the latest version of python installed onto
your device

-----CREATING DATABASE-----

This step may be different as there are other ways to do this. However, my method of creating the database was to open
up the terminal and head to the directory that this project folder is being stored in. From there, type 'python' to
open up the python shell and then type:
    $from App import db
    $db.create_all()
( the $ indicates a new line)

Assuming there are no errors, you should head to your phpMyAdmin tab and see 4 tables in your database have been created

        **SUCCESS**
-----USING THE APPLICATION-----

Now we can run our code. Start the application and then head to the local hose link that the program gives you. From
there, you should be able to add,edit,and delete courses, students, and instructors
