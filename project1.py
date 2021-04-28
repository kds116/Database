import mysql.connector
import sys
import time


def displayMenu():
    print()
    print("Airport Information System")
    print("**************")
    print("1-Add a new Employee to the Database")
    print("2-Delete an existing Employee from the Database")
    print("3-Update the expertise of an existing Technician")
    print("4-View full details of the technician who's salary is greater than the average technician salary")
    print("5-View all Technician Numbers")
    print("6-Enter a technician number to see their areas of expertise and details about the model")
    print("7-Enter a model number to see the total number of expert technicians for that model")
    print("8-Display full details of the FAA tests for a given airplane")
    print("9-Show the most recent medical exam & union membership number for each Traffic Controller")
    print("10-Total number of tests done by each technician for a given airplane")
    print("11-Full details of FAA tests completed between August 2020 and December 2020")
    print("12-Quit")
    print()
    # print(">> ",end="")



def getChoice():

    #choice=False
    #while(not choice):
    choice = input(">> ")
    while (not choice.isdigit()):
        print("Invalid choice...")
        displayMenu()
        choice = input(">> ")
    return eval(choice)

def main():
    #CREATE USER  `bte423user` @ `lawtech.law.miami.edu` IDENTIFIED BY 'bteuser';
    cnx = mysql.connector.connect(host='', user='', password='', database='')
    cursor = cnx.cursor()
    #choice=False
    #while(not choice):
    displayMenu()
    choice = getChoice()
    
    while (choice != 12):
        
        if (choice == 1):
            ssn = int(input("Enter SSN (No dashes): "))
            unionNo = int(input("Enter 7 digit Union Membership Number: "))
            cursor.execute("INSERT INTO employees VALUES (%s, %s)", (ssn, unionNo))
            
            query=("SELECT * FROM employees" )
            cursor.execute(query);
            print("SSN".ljust(30),"Union Membership No.".ljust(8), sep="")
            for i in range(50):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(35),str(x[1]).ljust(10), sep="")
            print()
            displayMenu()
            choice = getChoice()
            
        elif (choice == 2):
            ssn = int(input("Enter SSN (No dashes): "))
            query1 = ("DELETE FROM employees WHERE SSN = '%s'")
            cursor.execute(query1,(ssn,));
            
            query=("SELECT * FROM employees" )
            cursor.execute(query);
            print("SSN".ljust(30),"Union Membership No.".ljust(8), sep="")
            for i in range(50):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(35),str(x[1]).ljust(10), sep="")
            print()
            displayMenu()
            choice = getChoice()
            
        elif (choice==3):
            model = int(input("Enter the new Model Number: "))
            expert = int(input("Enter the Expert Number of who you'd like to Update (Ex. Enter '1'): "))
            query1 = "UPDATE tech_expert SET modelNo = '%s' WHERE expertNo = '%s'"
            #inputData = (model, expert)
            cursor.execute(query1,(model, expert, ));
            
            query=("SELECT * FROM tech_expert" )
            cursor.execute(query);
            print("Expert No.".ljust(15),"Technician No.".ljust(20), "Model No.".ljust(10), sep="")
            for i in range(50):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(15),str(x[1]).ljust(20),str(x[2]).ljust(10), sep="")
            print()
            displayMenu()
            choice = getChoice()
            
        elif (choice==4):
            #result=cursor.execute
            query = ("SELECT techNo AS \'Technician Number\', fname AS \'First Name\', lname AS \'Last Name\', "
                                    "address AS \'Address\', phoneNo AS \'Phone Number\', CONCAT('$', FORMAT(salary, 0)) AS \'Salary\', SSN "
                                "FROM technicians "
                                "WHERE salary > " 
                                "ALL(SELECT AVG(salary) FROM technicians GROUP BY techNo);")
            #print("Technician Number".ljust(30), "Name".ljust(20), "Address".ljust(20), "Phone Number".ljust(20), "Salary".ljust(20), "SSN".ljust(20))
            cursor.execute(query);
            print("Technician Number".ljust(20),"Name".ljust(22), "Address".ljust(32),
                  "Phone Number".ljust(30), "Salary".ljust(20), sep="")
            for i in range(130):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(18),str(x[1]).ljust(5), str(x[2]).ljust(7),
                      str(x[3]).ljust(44),str(x[4]).ljust(29), str(x[5]).ljust(20),  sep="")
            print()
            #for (techNo, fname, lname, address, phoneNo, salary, SSN) in cursor:
            #   print(techNo, fname, lname, address, phoneNo, salary, SSN)
            #print()
            displayMenu()
            choice=getChoice()
            
        elif (choice==5):
            query = ("SELECT techNo, fname, lname FROM technicians;")
            cursor.execute(query);
            print("Technician No.".ljust(20),"First Name".ljust(15), "Last Name".ljust(10), sep="")
            for i in range(80):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(20),str(x[1]).ljust(15), str(x[2]).ljust(10), sep="")
            print()
            displayMenu()
            choice = getChoice()
            
            
        elif (choice==6):
            techExpert = eval(input("Enter Technician Number (Enter in-between quotation marks) >> "));
            query = query = ("SELECT techNo AS \'Technician Number\', modelNo, capacity, weight "
                            "FROM model "
                            "WHERE techNo = %s")
            cursor.execute(query,(techExpert,));
            print("Technician Number".ljust(30), "Model Number".ljust(20), "Capacity".ljust(20), "Weight(in tons)".ljust(20))
            for i in range(100):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(25), str(x[1]).rjust(15), str(x[2]).rjust(20), str(x[3]).rjust(20),  sep="")
            print()
            displayMenu()
            choice = getChoice()
            
        elif (choice==7):
            model = eval(input("model number >> "));
            query = query = ("SELECT modelNo AS \'Model Number\', Count(*) AS \'experts\' "
                                "FROM model m "
                                "JOIN technicians t ON m.techNo = t.techNo "
                                "WHERE modelNo = %s "
                                "GROUP BY modelNo ") 
            cursor.execute(query,(model,));
            for (modelNo, experts) in cursor:
                print(experts)
            print()
            displayMenu()
            choice=getChoice()
            
        elif (choice==8):
            query = ("SELECT a.registrationNo, modelNo, test_no, testName, actual_score, max_score "
                                    "FROM test t "
                                    "JOIN test_info ti ON t.test_no = testNo "
                                    "JOIN airplane a ON t.registrationNo = a.registrationNo "
                                    "ORDER BY actual_score DESC;")
            cursor.execute(query);
            print("Registration".ljust(20),"Model".ljust(8), "Test Number".ljust(15),
                  "Test Name".ljust(30), "Actual Score".ljust(20), "Max Score".ljust(20), sep="")
            for i in range(130):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(20),str(x[1]).ljust(10), str(x[2]).ljust(10),
                      str(x[3]).ljust(35),str(x[4]).ljust(20), str(x[5]).ljust(20),  sep="")
            print()
            displayMenu()
            choice = getChoice()
            
        elif (choice==9):
            query = ("SELECT union_mem_no, examDate "
                            "FROM traffic_controllers tc "
                            "JOIN employees e ON tc.SSN = e.SSN;")
            cursor.execute(query);
            print("Union Membership No.".ljust(30),"Most Recent Medical Exam".ljust(8), sep="")
            for i in range(130):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(35),str(x[1]).ljust(10), sep="")
            print()
            displayMenu()
            choice = getChoice()
            
        elif (choice==10):
            query=("SELECT t.techNo, COUNT(*) AS \'Completed\' "
                    "FROM technicians t "
                    "JOIN model m ON t.techNo = m.techNo "
                    "JOIN airplane a ON m.modelNo = a.modelNo "
                    "JOIN test ON a.registrationNo = test.registrationNo "
                    "GROUP BY t.techNo" )
            cursor.execute(query);
            print("Technician No.".ljust(30),"Completed Tests".ljust(8), sep="")
            for i in range(46):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(35),str(x[1]).ljust(10), sep="")
            print()
            displayMenu()
            choice = getChoice()
            
        elif(choice==11):
            query = ("SELECT fname, lname, a.registrationNo, test.test_no "
                    "FROM technicians t "
                    "JOIN model m ON t.techNo = m.techNo "
                    "JOIN airplane a ON m.modelNo = a.modelNo "
                    "JOIN test ON a.registrationNo = test.registrationNo "
                    "JOIN test_info ti ON test.test_no = ti.testNo "
                    "WHERE ti.date BETWEEN \'2020-08-01\' AND \'2020-12-01\'")
            cursor.execute(query);
            print("First Name".ljust(23), "Last Name".ljust(23), "Registration No.".ljust(25), "FAA Test No.".ljust(20))
            for i in range(100):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(5), str(x[1]).rjust(25), str(x[2]).rjust(30), str(x[3]).rjust(20),  sep="")
            print()
            displayMenu()
            choice = getChoice()
            
        elif(choice==12):
            cursor.close()
            break;
        else:
            print("Invalid choice..")
            displayMenu()
            choice = getChoice()


if __name__ == "__main__":
    main()