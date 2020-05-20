import sqlite3

def createtable():
    conn = sqlite3.connect('db1.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()

# createtable()

def insert(roll,name,mark):
    conn = sqlite3.connect('db1.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)", (roll, name, mark))
    conn.commit()
    conn.close()

# insert(1,'pugg',200)


def view():
    conn = sqlite3.connect('db1.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

print(view())

def delete(roll):
    conn = sqlite3.connect('db1.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=?",(roll,))
    conn.commit()
    conn.close()

# delete(4)

print(view())
