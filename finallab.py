import re
import pprint

listdict = [] #create list

def employeeInfo():
    #lists of invalid characters
    invalidEmail = ["'","!",'"',"%","#","^","&","*","(",")","=","+",",","<",">","?",";",":","[","]","{","}"]
    invalidAddress = ["'",'"',"!","@","$","%","^","&","*","_{","=","+","<",">","?",";",":","[","]","{","}"]

    #create dictionary
    employee = {}

    employeeid = int(input("ID: "))
    while employeeid > 9999999: #make sure ID not too long
        employeeid = int(input("ID too long. Try again: "))   
    employee["ID"] = employeeid #add to dictionary

    name = input("Name: ")
    employee["Name"] = name
    
    email = input("Email: ")
    check1 = [element for element in email if(element in invalidEmail)] #check for invalid characters
    while bool(check1) == True:
        email = input("Invalid character in email. Try again: ")
        check1 = [element for element in email if(element in invalidEmail)]
    employee["Email"] = email #add to dictionary
    
    address = input("Address: ")
    check2 = [element for element in address if(element in invalidAddress)] #check for invalid characters
    while bool(check2) == True:
        address = input("Invalid character in address. Try again: ")
        check2 = [element for element in address if(element in invalidAddress)]
    employee["Address"] = address #add to dictionary
    
    salary = float(input("Salary: "))
    while salary < 18 or salary > 27: #make sure salary not too small or large
        if salary < 18:
            salary = float(input("Salary too small. Try again: "))
        if salary > 27:
            salary = float(input("Salary too large. Try again: "))
    employee["Salary"] = salary

    listdict.append(employee) #add dictinary to list


def updatedList():
    
    for i in listdict:
        num = (i["Salary"] * .30)
        total = i["Salary"] + num
        i["Total Salary"] = total
        #employee['IT Department:Name'] = employee.pop('Name')
        
    #pprint.pprint(listdict)

def main():
    
   userchoice = input("To enter employee information enter 'E'. To quit enter 'Q': ")

   while userchoice != "Q": #loop to enter as many employees as user wants
        employeeInfo() #call dictionary making function
        pprint.pprint(listdict) #pretty print
        userchoice = input("To enter employee information enter 'E'. To quit enter 'Q': ") #check loop
   print("\n")
   
   updatedList() #call function to update salaries

   pprint.pprint(listdict)

main()
    
    
