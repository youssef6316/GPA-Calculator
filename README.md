Overview
This Python script provides a comprehensive GPA calculator with three main functionalities:

Semester GPA calculation

Cumulative GPA calculation

Target GPA calculation (what grades you need to reach a desired GPA)

Features
1. Semester GPA Calculator
Calculates GPA for a single semester

Handles any number of courses

Accounts for different credit hours per course

Provides motivational feedback based on your GPA

2. Cumulative GPA Calculator
Combines previous cumulative GPA with current semester GPA

Calculates new overall GPA

Gives encouraging messages based on your performance

3. Target GPA Calculator
Determines what GPA you need in upcoming semester(s) to reach your goal

Takes into account your current GPA and credit hours

Calculates the required performance for your target

How to Use
Run the program:

bash
Copy
python gpa_f.py
Main Menu Options:

Press 1 for Semester GPA calculation

Press 2 for Cumulative GPA calculation

Press 3 for Target GPA calculation

Follow the prompts:

Enter your grades and credit hours when requested

The program will guide you through each calculation

Try again:

After each calculation, you'll be asked if you want to perform another calculation

Requirements
Python 3.x

No additional libraries required

Example Usage
Copy
Welcome,
Main Menu :
        1. semester gpa
        2. cummulative gpa
        3. target gpa
choose one of the previous options:    1

please, enter the number of courses    3

please enter the grade you scored      3.5
please enter the credit hours of that course   3

please enter the grade you scored      4.0
please enter the credit hours of that course   2

please enter the grade you scored      2.7
please enter the credit hours of that course   4

this semster you scored 3.2555555555555557 ,
what an effort you did!
congratulations!

do you want to calculate anything again
 for 'yes' press 1
 for 'no' press any number     2
we were happy to help you
Notes
All grade inputs should be on a 4.0 scale (or your institution's equivalent)

Credit hours should be entered as numbers (e.g., 3 for a standard course)

The program handles decimal values for both grades and credit hours
