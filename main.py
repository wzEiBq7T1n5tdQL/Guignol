import mysql.connector
 
con = mysql.connector.connect(
                             host='localhost',
                             user='root',
                             password='ZilogZ80',                             
                             database='test',) 

def Add_Employ():
 
    Id = input("Enter Employee Id : ")
     
    if(check_employee(Id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()
         
    else:
        fName = input("Enter Employee First Name : ")
        lName = input("Enter Employee Last Name : ")
        patronymic = input("Enter Employee Patronymic : ")
        pnumber = input("Enter Employee Phone number : ")
        email = input("Enter Employee email : ")
        country = input("Enter Employee country : ")
        city = input("Enter Employee city : ")
        data = (Id, fName, lName, patronymic, pnumber, email, country, city)
     
        sql = 'insert into clients values(%s,%s,%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
         
        c.execute(sql, data)
         
        con.commit()
        print("Employee Added Successfully ")
        menu()

def Remove_Employ():
    Id = input("Enter Employee Id : ")
     
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
         
        sql = 'delete from clients where id=%s'
        data = (Id,)
        c = con.cursor()
         
        c.execute(sql, data)
         
        con.commit()
        print("Employee Removed")
        menu()
 
 
def check_employee(employee_id):
     
    sql = 'select * from clients where id=%s'
     
    c = con.cursor(buffered=True)
    data = (employee_id,)
     
    c.execute(sql, data)
     
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
 
def Display_Employees():
     
    sql = 'select * from clients'
    c = con.cursor()
     
    c.execute(sql)
     
    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee First Name : ", i[1])
        print("Employee Last Name : ", i[2])
        print("Employee patronymic : ", i[3])
        print("Employee phone number : ", i[4])
        print("Employee email : ", i[5])
        print("Employee country : ", i[6])
        print("Employee city : ", i[7])
        print("---------------------\
        -----------------------------\
        ------------------------------\
        ---------------------")
         
    menu()
 
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Display Employees")
    print("4 to Exit")
 
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Remove_Employ()
    elif ch == 3:
        Display_Employees()
    elif ch == 4:
        exit(0)
    else:
        print("Invalid Choice")
        menu()
 

menu()
