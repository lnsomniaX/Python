import sqlite3 as dbms
from tkinter import *

root = Tk()
root.title('Python Grades')
root.iconbitmap()

conn = dbms.connect("Python Grades.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS programs (
            grade integer not null,
            name varchar(100)
           )""")


def update():
    c = dbms.connect("Python Grades.db")
    cur = c.cursor()

    grade_id = delete_box.get()
    cur.execute("""UPDATE programs SET
        grade = :grade,
        name = :name
    
        WHERE oid = :oid""",
                {
                    'grade': grade_editor.get(),
                    'name': name_editor.get(),

                    'oid': grade_id
                }
                )

    c.commit()
    c.close()


def edit():
    global editor
    editor = Tk()
    editor.title('Edit grades')
    editor.iconbitmap()

    con = dbms.connect("Python Grades.db")
    curs = con.cursor()

    grade_id = delete_box.get()
    grades = curs.fetchall()

    curs.execute("SELECT * FROM programs WHERE oid = " + grade_id)
    grades = curs.fetchall()

    global grade_editor
    global name_editor

    grade_editor = Entry(editor, width=30)
    grade_editor.grid(row=0, column=1, padx=20)
    name_editor = Entry(editor, width=30)
    name_editor.grid(row=1, column=1)

    grade_label_editor = Label(editor, text='Оценка')
    grade_label_editor.grid(row=0, column=0)
    name_label_editor = Label(editor, text='Имя')
    name_label_editor.grid(row=1, column=0)

    edit_button = Button(editor, text='Сохранить', command=update)
    edit_button.grid(row=2, column=0, columnspan=2)

    for grade in grades:
        grade_editor.insert(0, grade[0])
        name_editor.insert(0, grade[1])


def delete():
    connect = dbms.connect("Python Grades.db")
    curs = connect.cursor()

    curs.execute("DELETE from programs WHERE oid= " + delete_box.get())
    delete_box.delete(0, END)

    connect.commit()
    connect.close()


def submit():
    conn = dbms.connect("Python Grades.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO programs VALUES (:grade, :name)",
                   {
                       'grade': grade.get(),
                       'name': name.get()
                   })

    conn.commit()
    conn.close()

    grade.delete(0, END)
    name.delete(0, END)


def query():
    conn = dbms.connect("Python Grades.db")
    cursor = conn.cursor()

    cursor.execute("SELECT *, oid FROM programs")
    grades = cursor.fetchall()
    print(grades)

    student_grade = ''
    student_name = ''
    student_ID = ''
    for i in grades:
        student_grade += str(i[0]) + "\n"

    for i in grades:
        student_name += str(i[1]) + "\n"

    for i in grades:
        student_ID += str(i[2]) + "\n"

    q1_label = Label(root, text='Оценка')
    q2_label = Label(root, text='Имя')
    q3_label = Label(root, text='ID')
    q1_label.grid(row=9, column=0)
    q2_label.grid(row=9, column=1)
    q3_label.grid(row=9, column=2)
    query_label = Label(root, text=student_grade)
    query_label.grid(row=10, column=0)
    query_label = Label(root, text=student_name)
    query_label.grid(row=10, column=1)
    query_label = Label(root, text=student_ID)
    query_label.grid(row=10, column=2)
    conn.commit()
    conn.close()


grade = Entry(root, width=30)
grade.grid(row=0, column=1, padx=20)
name = Entry(root, width=30)
name.grid(row=1, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=5, column=1)

grade_label = Label(root, text='Оценка')
grade_label.grid(row=0, column=0)
name_label = Label(root, text='Имя')
name_label.grid(row=1, column=0)
delete_box_label = Label(root, text='Введите ID' + "\n" +'для редактирования')
delete_box_label.grid(row=5, column=0)

submit_button = Button(root, text='Внести оценку в базу', command=submit)
submit_button.grid(row=2, column=0, columnspan=3, pady=10, padx=10, ipadx=100)
query_btn = Button(root, text='Показать все оценки', command=query)
query_btn.grid(row=3, column=0, columnspan=3, pady=10, padx=10, ipadx=137)
dlt_btn = Button(root, text='Удалить оценку', command=delete)
dlt_btn.grid(row=6, column=0, columnspan=3, pady=10, padx=10, ipadx=136)
edit_btn = Button(root, text='Изменить оценки', command=edit)
edit_btn.grid(row=7, column=0, columnspan=3, pady=10, padx=10, ipadx=143)

conn.commit()
conn.close()

root.mainloop()
