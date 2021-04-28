import mysql.connector
import sys
import time


def displayMenu():
    print()
    print("Employee Database")
    print("**************")
    print("1-Show Employee Count")
    print("2-Show Average Employee Salary")
    print("3-Look up an employee by Employee Number")
    print("4-Show all Employee data by department")
    print("5-Show Employee Count based on gender")
    print("6-Quit")
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
    #cnx = mysql.connector.connect(host='10.211.55.18', user='tareks', password='mypqssword', database='employees')

    cursor = cnx.cursor()
    #choice=False
    #while(not choice):
    displayMenu()
    choice = getChoice()
    while (choice != 6):
        if (choice == 1):
            result = cursor.execute("SELECT count(*) from employees")
            print("There are ", cursor.fetchone()[0], " employees")
            print()
            displayMenu()
            choice = getChoice()
        elif (choice == 2):
            result = cursor.execute("SELECT CONCAT('$', avg(salary)) from salaries")
            print("Avg Salary=", cursor.fetchone()[0])
            print()
            displayMenu()
            choice = getChoice()
        elif (choice==3):
            employeeNumber = eval(input("employee number >> "));
            query = query = ("SELECT e.emp_no,first_name, last_name, hire_date, d.dept_no, dept_name FROM employees e, "
                             "departments d, dept_emp de "
                             "where"
                             " d.dept_no = de.dept_no and "
                             " e.emp_no  = de.emp_no and "
                             " e.emp_no = %s")
            cursor.execute(query,(employeeNumber,));
            for (emp_no, first_name, last_name, dept_no ,dept_name, hire_date ) in cursor:
                print(emp_no, first_name, last_name, dept_no ,dept_name, hire_date )
            #cursor.close();
            print()
            displayMenu()
            choice = getChoice()

        elif(choice==4):
            query = ("SELECT departmentNumber AS \'Department Number\', departName AS \'Department Name\', "
                "FORMAT(empCount, 0) AS \'Employee Count\', CONCAT('$', FORMAT(deptAvg, 2)) AS \'Department Avg Salary\', "
                "CONCAT('$',FORMAT((SELECT AVG(salary) FROM salaries s JOIN dept_emp de ON s.emp_no = de.emp_no JOIN departments d ON de.dept_no = d.dept_no WHERE s.to_date > curdate()), 2)) AS \'Company Avg Salary\', "  
                "CONCAT('$', FORMAT((deptAvg - (SELECT AVG(salary) FROM salaries s JOIN dept_emp de ON s.emp_no = de.emp_no JOIN departments d ON de.dept_no = d.dept_no WHERE s.to_date > curdate()) ), 2)) AS \'Salary Variance\' "
                "FROM ( "
	                "SELECT "
		                #Department Avg (2019)
                        "d.dept_no as 'departmentNumber', "
                        "d.dept_name AS 'departName', "
		                "AVG(salary) AS 'deptAvg', "
                        "COUNT(de.emp_no) AS 'Empcount' "
	                "FROM salaries s "
                    "JOIN dept_emp de ON s.emp_no = de.emp_no "
                    "JOIN departments d ON de.dept_no = d.dept_no "
                    "WHERE s.to_date > curdate() AND de.to_date > curdate() "
                    "GROUP BY dept_name ) a "
                "GROUP BY 1 " )
            print("Working.Please wait...\n")
            cursor.execute(query);
            print("Department Number".ljust(20),"Department Name".ljust(30), "Employee Count".ljust(20),
                  "Department Avg Salary".ljust(30), "Company Avg Salary".ljust(20),"Salary Variance".ljust(10), sep="")
            for i in range(130):
                print("=",end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(20),str(x[1]).ljust(30),str(x[2]).rjust(10),
                      str(x[3]).rjust(23),str(x[4]).rjust(29),str(x[5]).rjust(15),sep="")


            print()
            displayMenu()
            choice = getChoice()

        elif (choice==5):
            query=("SELECT a.dept_name AS \'Department\', a.male AS \'Male Employees\', b.female AS \'Female Employees\' "
                    "FROM ( "
	                    "SELECT "
	                        "dept_name, COUNT(*) AS \'male\' "
	                    "FROM dept_emp de "
	                    "JOIN employees e ON de.emp_no = e.emp_no "
	                    "JOIN departments d ON de.dept_no = d.dept_no "
	                    "WHERE gender = 'M' AND to_date > curdate() "
	                    "GROUP BY 1 ) a" 
                    "JOIN ( "
	                     "SELECT "
	                        "dept_name, "
	                        "COUNT(*) AS \'female\' "
	                    "FROM dept_emp de "
	                    "JOIN employees e ON de.emp_no = e.emp_no "
	                    "JOIN departments d ON de.dept_no = d.dept_no "
	                    "WHERE gender = 'F' AND to_date > curdate() "
	                    "GROUP BY 1 ) b "
	                    "ON a.dept_name = b.dept_name")

            print("Working.Please wait...\n")
            cursor.execute(query);
            print("Department".ljust(30), "Male Employees".ljust(20), "Female Employees".ljust(20))
            for i in range(90):
                print("=", end="")
            print()
            for x in cursor:
                print(str(x[0]).ljust(25), str(x[1]).rjust(15), str(x[2]).rjust(20), str(x[3]).rjust(20), sep="")
            print()
            displayMenu()
            choice = getChoice()
        elif(choice==6):
            cursor.close()
            break;
        else:
            print("Invalid choice..")
            displayMenu()
            choice = getChoice()


if __name__ == "__main__":
    main()