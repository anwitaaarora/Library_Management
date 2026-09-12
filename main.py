import getpass as p
import mysql.connector as mc

# Connect to MySQL Database
# IMPORTANT: Replace placeholders with your environment variables or local credentials
con = mc.connect(
    host="localhost",
    user="root",
    passwd="YOUR_MYSQL_PASSWORD",  # Put your local password here
    database="Library",
)
cur = con.cursor()


# -------------------- BOOK FUNCTIONS -------------------- #
def AddBook():
    a = "yes"
    while a.lower() == "yes":
        print(" ")
        BookID = int(input("Enter book ID: "))
        cur.execute("SELECT * FROM Books WHERE BookID={}".format(BookID))
        t = cur.fetchone()
        if t is None:
            Name = input("Enter Book name: ")
            Price = int(input("Enter price: "))
            Genre = input("Enter genre: ")
            Author = input("Enter author: ")
            Quantity = int(input("Enter quantity: "))
            q = "INSERT INTO Books (BookID, Name, Author, Genre, Price, Quantity) VALUES ({},'{}','{}','{}',{},{})".format(
                BookID, Name, Author, Genre, Price, Quantity
            )
            cur.execute(q)
            con.commit()
            print("Book Added.")
        else:
            print("Book ID is already in the library.")
        a = input("Type yes if you want to continue: ")


def DisplayrecB():
    cur.execute("SELECT Name FROM Books")
    for row in cur.fetchall():
        print(row)


def SearchBook():
    while True:
        print("----- Search Book ---------- ")
        print("1. By Name")
        print("2. By Author")
        print("3. By Genre")
        print("4. Exit")
        c = int(input("Enter your choice: "))

        if c == 1:
            name = input("Enter Book Name: ")
            cur.execute("SELECT * FROM Books WHERE Name='{}'".format(name))
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    print(r)
            else:
                print("No book found with this name.")
        elif c == 2:
            author = input("Enter Author: ")
            cur.execute("SELECT * FROM Books WHERE Author='{}'".format(author))
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    print(r)
            else:
                print("No book found for this author.")
        elif c == 3:
            genre = input("Enter Genre: ")
            cur.execute("SELECT * FROM Books WHERE Genre='{}'".format(genre))
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    print(r)
            else:
                print("No book found in this genre.")
        elif c == 4:
            break
        else:
            print("Invalid choice.")


def UpdateBook():
    while True:
        print("----- Update Book ---------- ")
        print("1. Update Price")
        print("2. Update Quantity")
        print("3. Exit")
        c = int(input("Enter your choice: "))

        if c == 1:
            bookid = int(input("Enter Book ID: "))
            newprice = int(input("Enter new Price: "))
            cur.execute(
                "UPDATE Books SET Price={} WHERE BookID={}".format(
                    newprice, bookid
                )
            )
            con.commit()
            print("Price updated.")
        elif c == 2:
            bookid = int(input("Enter Book ID: "))
            newqty = int(input("Enter new Quantity: "))
            cur.execute(
                "UPDATE Books SET Quantity={} WHERE BookID={}".format(
                    newqty, bookid
                )
            )
            con.commit()
            print("Quantity updated.")
        elif c == 3:
            break
        else:
            print("Invalid choice.")


def DeleteBook():
    bookid = int(input("Enter Book ID to delete: "))
    cur.execute("DELETE FROM Books WHERE BookID={}".format(bookid))
    con.commit()
    print("Book deleted successfully.")


def BookMenu():
    while True:
        print("\n----- BOOK MENU ---------- ")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit ")
        ch = int(input("Enter choice: "))

        if ch == 1:
            AddBook()
        elif ch == 2:
            DisplayrecB()
        elif ch == 3:
            SearchBook()
        elif ch == 4:
            UpdateBook()
        elif ch == 5:
            DeleteBook()
        elif ch == 6:
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid choice!")


# ------------------ ACCOUNT FUNCTIONS ------------------ #
def AddAcc():
    a = "yes"
    while a.lower() == "yes":
        print(" ")
        ID = int(input("Enter account ID:"))
        cur.execute("SELECT * FROM Accounts WHERE AccID={}".format(ID))
        t = cur.fetchone()
        if t is None:
            Name = input("Enter name:")
            Role = input("Enter role:")
            Status = input("Enter status:")
            Email = input("Enter email:")
            q = "INSERT INTO Accounts(AccID, Name, Role, Status, Email) VALUES({},'{}','{}','{}','{}')".format(
                ID, Name, Role, Status, Email
            )
            cur.execute(q)
            con.commit()
            print("Account Added.")
        else:
            print("Account already exists.")
        a = input("Type yes if you want to continue: ")


def DisplayrecA():
    cur.execute("SELECT Name FROM Accounts")
    for row in cur.fetchall():
        print(row)


def SearchAccount():
    while True:
        print("\n----- Search Account --------- ")
        print("1. By ID")
        print("2. By Name")
        print("3. By Role")
        print("4. By Status")
        print("5. Exit")
        c = int(input("Enter your choice: "))

        if c == 1:
            accid = int(input("Enter Account ID: "))
            cur.execute("SELECT * FROM Accounts WHERE AccID={}".format(accid))
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    print(r)
            else:
                print("No account found with this ID.")
        elif c == 2:
            name = input("Enter Name: ")
            cur.execute(
                "SELECT * FROM Accounts WHERE Name='{}'".format(name)
            )
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    print(r)
            else:
                print("No account found with this name.")
        elif c == 3:
            role = input("Enter Role: ")
            cur.execute(
                "SELECT * FROM Accounts WHERE Role='{}'".format(role)
            )
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    print(r)
            else:
                print("No account found for this role.")
        elif c == 4:
            status = input("Enter Status: ")
            cur.execute(
                "SELECT * FROM Accounts WHERE Status='{}'".format(status)
            )
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    print(r)
            else:
                print("No account found with this status.")
        elif c == 5:
            break
        else:
            print("Invalid choice.")


def UpdateAccount():
    while True:
        print("\n----- Update Account --------- ")
        print("1. Update Role")
        print("2. Update Status")
        print("3. Update Email")
        print("4. Exit")
        c = int(input("Enter your choice: "))

        if c == 1:
            accid = int(input("Enter Account ID: "))
            newrole = input("Enter new role: ")
            cur.execute(
                "UPDATE Accounts SET Role='{}' WHERE AccID={}".format(
                    newrole, accid
                )
            )
            con.commit()
            print("Role updated.")
        elif c == 2:
            accid = int(input("Enter Account ID: "))
            newstatus = input("Enter new status: ")
            cur.execute(
                "UPDATE Accounts SET Status='{}' WHERE AccID={}".format(
                    newstatus, accid
                )
            )
            con.commit()
            print("Status updated.")
        elif c == 3:
            accid = int(input("Enter Account ID: "))
            newemail = input("Enter new email: ")
            cur.execute(
                "UPDATE Accounts SET Email='{}' WHERE AccID={}".format(
                    newemail, accid
                )
            )
            con.commit()
            print("Email updated.")
        elif c == 4:
            break
        else:
            print("Invalid choice.")


def DeleteAccount():
    accid = int(input("Enter Account ID to delete: "))
    cur.execute("DELETE FROM Accounts WHERE AccID={}".format(accid))
    con.commit()
    print("Account deleted successfully.")


def IssueBook():
    nm = input("Enter Book Name to Issue: ")
    cur.execute("SELECT BookID, Status FROM Books WHERE Name='{}'".format(nm))
    bk = cur.fetchone()
    if bk is None:
        print("Book not found.")
    elif bk[1] and bk[1].lower() == "issued":
        print("This book is already issued.")
    elif bk is not None:
        accid = int(input("Enter Account ID of the person issuing: "))
        cur.execute("SELECT * FROM Accounts WHERE AccID={}".format(accid))
        acc = cur.fetchone()
        if acc is None:
            print("Account not found.")
        else:
            cur.execute(
                "UPDATE Books SET Status='Issued', IssuedTo={} WHERE BookID={}".format(
                    accid, bk[0]
                )
            )
            con.commit()
            print("Book Issued Successfully.")


def ReturnBook():
    name = input("Enter Book Name to Return: ")
    cur.execute("SELECT BookID, Status FROM Books WHERE Name='{}'".format(name))
    book = cur.fetchone()
    if book is None:
        print("Book not found.")
    elif book[1] and book[1].lower() == "available":
        print("This book is not issued.")
    else:
        cur.execute(
            "UPDATE Books SET Status='Available', IssuedTo=NULL WHERE BookID={}".format(
                book[0]
            )
        )
        con.commit()
        print("Book Returned Successfully.")


def AccountMenu():
    while True:
        print("\n----- ACCOUNT MENU ---------- ")
        print("1. Add Account")
        print("2. Display Accounts")
        print("3. Search Account")
        print("4. Update Account")
        print("5. Delete Account")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Exit ")
        ch = int(input("Enter choice: "))
        if ch == 1:
            AddAcc()
        elif ch == 2:
            DisplayrecA()
        elif ch == 3:
            SearchAccount()
        elif ch == 4:
            UpdateAccount()
        elif ch == 5:
            DeleteAccount()
        elif ch == 6:
            IssueBook()
        elif ch == 7:
            ReturnBook()
        elif ch == 8:
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid choice!")


# -------------------- MAIN MENU -------------------- #
if __name__ == "__main__":
    i = 1
    access_granted = False
    while i <= 3:
        pword = p.getpass("Enter password: ")
        if pword == "123@novelnestlibrary":
            print("Correct password, Access granted.")
            access_granted = True
            break
        else:
            print("Incorrect password, Access not granted.")
            i += 1

    if not access_granted:
        print("Maximum attempts reached!")
    else:
        while True:
            print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
            print("1. Book Records")
            print("2. Account Records")
            print("3. Exit")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                BookMenu()
            elif ch == 2:
                AccountMenu()
            elif ch == 3:
                print("Exiting application.")
                break
            else:
                print("Invalid choice.")
