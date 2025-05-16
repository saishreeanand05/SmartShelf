import mysql.connector as a
con=a.connect(host='localhost', user='root', passwd='Omsairam', database='proj12');

def addbook():
    bn=input("Enter Book Name: ")
    ba=input("Enter Author's Name: ")
    c=input("Enter Book Code:")
    t=int(input("Total Books:"))
    s=input("Enter Subject:")
    data=(bn,ba,c,t,s)
    sql="insert into books values(%s,%s,%s,%s,%s);"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("\n\n\n\nBook Added Successfully .......")
    wait = input('\n\n\nPress enter to continue ..... \n\n\n\n\n\n')
    main()

def issueb():
    n=input("Enter Student Name: ")
    r=int(input("Enter Reg No .: "))
    co=int(input("Enter Book Code:"))
    d=input("Enter Date (yyyy/mm/dd):")
    data=(n,r,co,d)
    a="insert into issue values(%s,%s,%s,%s);"
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("\n\n\n\nBook issued successfully to: ",n)
    t=(co,)
    b="update books set total= total-1 where bcode=(%s);"
    c=con.cursor()
    c.execute(b,t)
    con.commit()
    wait = input('\n\n\nPress enter to continue ..... \n\n\n\n\n\n')
    main()

def returnb():
    n=input("Enter Student Name: ")
    r=int(input("Enter Reg No .: "))
    co=int(input("Enter Book Code:"))
    d=input("Enter Date (yyyy/mm/dd): ")
    data=(n,r,co,d)
    a="select name, regno, bcode from issue;"
    c=con.cursor()
    c.execute(a)
    z=c.fetchall()
    print(z)
    sr=str(r)
    sco=str(co)
    p=(n,sr,sco)
    if p in z:
        a="insert into return_ values(%s,%s,%s,%s);"
        c=con.cursor()
        c.execute(a,data)
        con.commit()
        print("Book returned by: ",n)
        t=(co,)
        b="update books set total= total+1 where bcode=(%s);"
        c=con.cursor()
        c.execute(b,t)
        con.commit()
        wait = input('\n\n\nPress enter to continue ..... \n\n\n\n\n\n')
        main()
    else:
        print('\n\n\nBook was not issued by ', n)
        print('Sending back to main menu...\n\n\n')
        main()

def dbook():
    ac=int(input("Enter book code: "))
    a="delete from books where bcode=%s;"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("book deleted successfully")
    wait=input('\n\n\nPress enter to continue...........\n\n\n\n\n\n\n\n')
    main()

def dispbook():
    a="select*from books;"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
         print("Book name: ",i[0])
         print("Author: ",i[1])
         print("Book code: ",i[2])
         print("Total: ",i[3])
         print("Subject: ",i[4])
         print("\n\n ") 

    wait=input('\n\n\nPress enter to continue.....\n\n\n\n\n\n')
    main()

def report_issued_books():
    a="select * from issue;"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print(i)
    wait = input('\n\n\nPress enter to continue ..... \n\n\n\n\n\n\n\n')
    main()
    
def report_return_books():
    a="select * from return_;"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print(i)
    wait = input("\n\n\nPress enter to continue ..... \n\n\n\n\n\n\n\n\n\n\n\n")
    main()

def main():
    print("""LIBRARY MANAGEMENT APPLICATION
            1. ADD BOOK
            2. ISSUE OF BOOK
            3. RETURN OF BOOK
            4. DELETE BOOK
            5. DISPLAY BOOKS
            6. REPORT MENU
            7. EXIT PROGRAM
            """)

    print('LIST OF BOOKS WITH THEIR BOOK CODES:')
    a="select bname, bcode from books;"
    c=con.cursor()
    c.execute(a)
    z=c.fetchall()
    for i in z:
        print(i)
    print("\n\n\n")
    choice=input("Enter Task No :...... ")
    print("\n\n\n\n\n\n\n")
    if(choice == '1'):
        addbook()
    elif(choice == '2'):
        issueb()
    elif(choice == '3'):
        returnb()
    elif(choice == '4'):
        dbook()
    elif(choice == '5'):
        dispbook()
    elif(choice == '6'):
        print("""REPORT MENU
            1. CUSTOMER RECORDS OF ISSUED BOOKS
            2. CUSTOMER RECORDS OF RETURNED BOOKS
            3. GO BACK TO MAIN MENU
            \n\n\n""")
     
        choice=input("Enter Task No :...... ")
        print('\n\n\n\n\n\n\n')
        if choice == '1':
            report_issued_books()
        elif choice == '2':
            report_return_books()
        elif choice == '3':
            main()
        else:
            print("Please try again ........ \n\n\n\n\n\n\n\n\n")
            main()
    elif(choice == '7'):
        print('\n\n\n\n\n\n\n\n\n\n\n\nThank you and have a great day ahead.')
        con.close()
    else:
        print("Please try again ........ \n\n\n\n\n\n\n\n\n\n\n\n")
        main()
    
main()

