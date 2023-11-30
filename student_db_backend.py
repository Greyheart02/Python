import sqlite3


def studentData(): #this function creates the database ith all the parameters
    con= sqlite3.connect("student.db") #this line creates a connection with the student.db database
    cur= con.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST student(id INTEGER PRIMARY KEY, stdID, Firstname text, Surname text, DoB text, \
    Age text, Gender text, Address text, Mobile, text)")
    con.commit()
    con.close()

def addStdRec(stdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?,?,?,?,?", \
                (stdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()
    return rows

def vieData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()

studentData()
