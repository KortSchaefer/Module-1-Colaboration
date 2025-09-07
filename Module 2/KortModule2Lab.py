'''
Author: Kort Schaefer
Date: 2022-10-25
Module: 2
Lab: Kort Module 2 Lab
Description: GPA and Qualifications for a student in a dictionary structure to determine qualifications
Version: 1.0
'''


print('Enter the First name of the student')
fName = input('[]:')
print('Enter the Last name of the student or ZZZ to quit')
lName = input('[]:')

if lName.upper() == 'ZZZ':
    # Quit condition
    print('Exiting...')
else:
    print('Enter the GPA of the student')
    gpa = float(input('[]:'))

    # Use clear, fixed keys and store the entered values
    student = {
        'First Name': fName,
        'Last Name': lName,
        'GPA': gpa,
        'Qualifications': []
    }

    # Determine qualifications
    if gpa >= 3.5:
        student['Qualifications'].append("Dean's List")
    elif gpa >= 3.25:
        student['Qualifications'].append('Honor Roll')

    # Output
    print('Name:', student['First Name'], student['Last Name'])
    print('GPA:', student['GPA'])
    print('Qualifications:', ', '.join(student['Qualifications']) if student['Qualifications'] else 'None')
