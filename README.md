Student Database Management Application Overview
This script creates a graphical user interface (GUI) for managing a student database using PyQt6, integrated with an SQLite database. Users can add, view, search, update, and delete student records, as well as check their academic status based on GPA.

Key Components:
Imports:

The script imports essential modules from PyQt6 for GUI components, layouts, and event handling.
It also imports sqlite3 to manage the database operations.
Main Application Class: Students

Inherits from QMainWindow, serving as the main window of the application.
The __init__ method sets up the window title, dimensions, and initializes the user interface elements.
User Interface Setup:

The application uses a vertical box layout (QVBoxLayout) to arrange input fields and buttons.
Input fields are provided for student information (first name, last name, term, GPA) and an ID for operations like deletion and updating.
Styling: apply_stylesheet()

Defines a custom stylesheet to enhance the visual appearance, including background colors, font sizes, and button styles.
Database Connection: connect()

Establishes a connection to the SQLite database (students.db), creating a table for student records if it does not exist.
CRUD Operations:

Insert: The insert() method adds a new student record to the database and displays a confirmation message.
View: The view() method retrieves all student records from the database.
Search: The search() method allows searching for student records based on various criteria (first name, last name, term, GPA, ID).
Delete: The delete() method removes a student record based on the provided ID and confirms the action with a message.
Update: The update() method modifies an existing student record based on the provided ID and updated information.
Academic Status Check: successorfail()

Checks a student’s GPA and term to determine if they have passed or failed, providing feedback through a message box.
Display Functions:

vpop() displays all student records in a message box.
spop() shows the results of a search operation in a message box.
Clear Input Fields: clear()

Resets all input fields to empty, allowing users to start fresh.
Application Execution:

Initializes a QApplication, creates an instance of the Students class, and sets a theme and custom font for the application.
Finally, it starts the application event loop.
Conclusion
This script effectively demonstrates the integration of a GUI application with a relational database using SQLite. It covers essential operations for managing student records and provides a user-friendly interface for interacting with the database. The structured approach and modular design make it a suitable reference for developing database-driven applications in Python.
![alt text](https://github.com/MazenNassar/Student-Management-System/blob/main/image.png?raw=true)
