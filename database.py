import sqlite3
conn = sqlite3.connect("student.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INT,
        branch TEXT NOT NULL
);
''')
conn.commit()
conn.close()

def add_student(name, age, branch):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Students(name , age , branch)
    VALUES( ? , ? , ?)
    ''', (name, age, branch))

    conn.commit()
    conn.close()

def view_student():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Students')

    rows = cursor.fetchall()

    conn.close()
    return rows

def update_student(student_id , age , branch):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Students
        Set age = ? , branch = ?
        WHERE student_id = ? ''',
    ( age , branch , student_id))

    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM Students
    WHERE student_id = ?''',
    (student_id,))

    conn.commit()
    conn.close()

def search_student(name):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM Students
    WHERE name LIKE ?''',
    ('%' + name + '%',))

    rows = cursor.fetchall()

    conn.close()
    return rows