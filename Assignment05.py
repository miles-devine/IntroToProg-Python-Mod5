# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
#   Miles Devine, 7/31/2024, Created script
# ------------------------------------------------------------------------------------------ #
import json
from json import JSONDecodeError

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students = []  #Holds a two-dimensional table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file) #Puts the contents of the file into the students variable
    file.close()
except FileNotFoundError as e: #Error handling in the event that the user does not have a file with the requirements outlined
    print('The JSON file was not found \n')
    print('----------Technical Error----------')
    print(e, e.__doc__, type(e), sep='\n')
    print('Creating missing file. ')
    file = open(FILE_NAME, 'w')
    json.dump(students, file)
except JSONDecodeError:
    print('Data in file is invalid...\nResetting it.')#Error handling in the event that the contents of the defined file are not valid
    file = open(FILE_NAME, 'w')
    json.dump(students, file)
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: \n")

    # Input user data
    if menu_choice == '1':
        try:
            student_first_name = input("What is the student's first name? ") #Gathers student first name from user
            if not student_first_name.isalpha():
                raise ValueError("\nThe first name should only contain letters.\n") #Displays custom error message
        except ValueError as e:
            print(e)
            print('----------Technical Error----------')
            print(e.__doc__, type(e), sep='\n') #Displays the technical error message
            if not student_first_name.isalpha():
                student_first_name = input("\nWhat is the student's first name? ") #Prompts the user to enter their input again
        try:
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("\nThe last name should only contain letters.\n") #Displays custom error message
        except  ValueError as e:
            print(e)
            print('---------Technical Error---------')
            print(e.__doc__, type(e), sep='\n') #Displays the technical error message
            if not student_last_name.isalpha():
                student_last_name = input("What is the student's last name? ") #Prompts the user to enter their input again

        course_name = input("What is the course name? ") #Gathers the course name from the user

        student_data = {"firstname": student_first_name,
                        "lastname": student_last_name,
                        "coursename": course_name}
        students.append(student_data)
        continue
    # Present the current data
    elif menu_choice == '2':

        # Process the data to create and display a custom message
        print("-" * 50)
        print('Here is the current data: \n')
        for student_data in students:
            message = '{},{},{}'
            print(message.format(student_data["firstname"], student_data["lastname"], student_data["coursename"]))
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
        except Exception as e:
            print('Error saving data...')
            print(e)
        finally:
            if file and not file.closed:
                file.close()
            print('The following data was saved: \n')
            for student_data in students:
                message = '{},{},{}'
                print(message.format(student_data["firstname"], student_data["lastname"], student_data["coursename"]))

    # Stop the loop
    elif menu_choice == "4":
        input('Waiting for you to press enter... ')
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")
