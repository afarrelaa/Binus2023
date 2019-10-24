# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:12:25 2019

@author: Afarrel

1.
    a)  Parent class :Spell
        Child class  :Confundo,Accio
    
    b)  Accio
        Summoning CharmAccio
        No description
        Confundus CharmConfundo
        Causes the victim to become confused and befuddled.

    c)  the result is : "Causes the victim to become confused and befuddled."
    

    d)  we need to create a new function inside the class of Accio that should contain the code:
        return ‘This charm summons an object to the caster, potentially over a significant distance’

2.
"""

import csv
textsource= 'data.txt'
csvfile = 'data.csv'

def choice():
    while True:
        print("1.To add a new employee")
        print("2.Remove existing employee data")
        print("3.Print summary data")
        print("4.Save & Exit")
        option = input('Please Input your choice:  ')
        if option == '1':
            addEmplo()
        elif option == '2':
            remove()
        elif option == '3':
            statistics()
        elif option == '4':
            saveandquit()
            break
        else:
            pass

class employee():
    __fullname = ''
    __jobposition = ''
    __salary = 0

    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def getName(self):
        return self.__name

    def getPosition(self):
        return self.__position

    def getSalary(self):
        return self.__salary

class ID():
    __identity = ''
    __listOfEmp = []

    def __init__(self, identity):
        self.__identity = identity

    def getIdentity(self):
        return self.__identity

    def newStaff(self, name, position, salary):
        self.__listOfEmp.append(employee(name, position, salary))

        fields = [self.__identity, name, position, salary]

        with open(csvfile, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

#  Add employee
def addEmplo():
    with open(csvfile) as f:
        reader = csv.reader(f)
        headerRow = next(reader)
        ayden = input('Your id here >>> ')

        for row in reader:
            if ayden == row[0]:
                print("ID is already registered!")
                quit()
            else:
                iname = input('name > ')
                iposition = input('position > ')
                isalary = str(input('salary > '))

                ID(ayden).newStaff(iname, iposition, isalary)
                print("Thank you for registering!")
                break
        f.close()

# Remove employee
def remove():
    tbr = []
    with open(csvfile) as f:
        reader = csv.reader(f)
        headerRow = next(reader)
        ayden = input('Your ID here >>> ')

        for row in reader:
            if ayden == row[0]:
                pass
            else:
                tbr.append(row)

        g = open(csvfile, "w+")
        g.close()

        header = ['ID','Name','Position','SalaryAmount']
        with open(csvfile, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(header)

        for row in tbr:
            iname = row[1]
            iposition = row[2]
            isalary = row[3]

            ID(ayden).newStaff(iname, iposition, isalary)

        f.close()


#  To take average

def statistics():
    id_staff = []
    id_officer = []
    id_manager = []

    with open(csvfile) as f:
        reader = csv.reader(f)
        headerRow = next(reader)
        for row in reader:
            if row[2] == 'Staff':
                id_staff.append(row[3])
            elif row[2] == 'Officer':
                id_officer.append(row[3])
            elif row[2] == 'Manager':
                id_manager.append(row[3])

        print('\n')
        print('Staff')
        print('Minimum Salary:', min(id_staff))
        print('Maximum Salary:', max(id_staff))
        for i in range(0, len(id_staff)):
            id_staff[i] = int(id_staff[i])
        print('Average Salary:', sum(id_staff)//len(id_staff))

        print('\n')

        print('Officer')
        print('Minimum Salary:', min(id_officer))
        print('Maximum Salary:', max(id_officer))
        for i in range(0, len(id_officer)):
            id_officer[i] = int(id_officer[i])
        print('Average Salary:', sum(id_officer) // len(id_officer))

        print('\n')

        print('Manager')
        print('Minimum Salary:', min(id_manager))
        print('Maximum Salary:', max(id_manager))
        for i in range(0, len(id_manager)):
            id_manager[i] = int(id_manager[i])
        print('Average Salary:', sum(id_manager) // len(id_manager))

        print('\n')


# To save and quit
def saveandquit():
    csv_file = 'data.csv'
    txt_file = 'data.txt'
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write("#".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()


        
     
 
    
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        