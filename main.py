import sqlite3

def print_tables():
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row [1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

def init_commit():

    # create table
    conn.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY NOT NULL,
        NAME    TEXT    NOT NULL,
        AGE     INT NOT NULL,
        ADDRESS  CHAR(50),
        SALARY  REAL);''')
    print("Table created succcessfully")

    # create commits
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (1, 'Paul', 32, 'California', 20000.00 )");
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (2, 'Marry', 43, 'Washington', 12000.00 )");
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (3, 'John', 25, 'Michigan', 30050.00 )");
    conn.commit()
    print("Records created successfully")

#init_commit()

# create database
conn = sqlite3.connect('database.db')
print("Opened database succcessfully")

id_try = 1
add_suc = 0
add_name = input("Name: ")
add_age = input("Age: ")
add_address = input("Address: ")
add_salary = input("Salary: ")

while add_suc == 0:
    try:
        conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (?, ?, ?, ?, ?)",(id_try, add_name, add_age, add_address, add_salary));
        conn.commit
        print("Add was successful")
        add_suc = 1

    except sqlite3.IntegrityError:
        print("Add encountered an error - trying next ID")
        id_try = id_try + 1

# read and write from tables
print_tables()
print("Tables read and wrote successfully \n")

# print ID Names
cursor = conn.execute("SELECT id, name from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row [1], "\n")

# update tables
change_ID = input("ID to change: ")
change_salary = input("New salary: ")

conn.execute("UPDATE COMPANY set SALARY = ? WHERE id=?", (change_salary, change_ID))
conn.commit
print("Total number of rows updated: ", conn.total_changes)

print_tables()

# close database
conn.close()
