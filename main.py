import tkinter as tk
import mysql.connector
from tkinter import ttk

def store(Name, Regno, Rollno, DOB, BloodGroup, Gender):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="keerthivasan"
        )
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                Regno BIGINT PRIMARY KEY,
                Rollno VARCHAR(20),
                Name VARCHAR(20),
                Gender VARCHAR(20),
                DOB VARCHAR(20),
                BloodGroup VARCHAR(20)
            )
        ''')
        query = '''
            INSERT INTO students (Name, Rollno, Regno, DOB, BloodGroup, Gender)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (Name.get(), Rollno.get(), Regno.get(), DOB.get(), BloodGroup.get(), Gender.get()))
        print("Details stored into table")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        connection.commit()
        connection.close()

def database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2004",
        database="keerthivasan"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print(rows)

    root = tk.Tk()
    root.title("Database")

    title=("Regno ", "Rollno", "Name", "Gender", "DOB","Blood Group")
    tree = ttk.Treeview(root, columns=title,show="headings") 

    for item in tree.get_children():
        tree.delete(item)

    for row in rows:
        tree.insert("", "end", values=row)

    for col in title:
        tree.heading(col, text=col)
        tree.column(col, anchor="w", width=150)

    tree.pack()

    root.mainloop()

    connection.close()

def mainwindow():
    win = tk.Tk()
    win.geometry("550x350")

    style = ttk.Style()
    style.configure("TButton")

    Name = tk.StringVar()
    Regno = tk.IntVar()
    Rollno = tk.StringVar()
    DOB = tk.StringVar()
    BloodGroup = tk.StringVar(value="Select blood group")
    Gender = tk.StringVar(value="Select gender")

    def cleare():
        nameE.delete(0,tk.END)
        rollnoE.delete(0,tk.END)
        dobE.delete(0,tk.END)
        regnoE.delete(0,tk.END)

    heading = tk.Label(win, text="STUDENT REGISTRATION", font=('calibri', 16, 'bold'))

    name = tk.Label(win, text="Name ")
    nameE = tk.Entry(win, textvariable=Name, width=30, relief="groove", bd=2)

    regno = tk.Label(win, text="Reg no ")
    regnoE = tk.Entry(win, textvariable=Regno, width=30, relief="groove", bd=2)

    rollno = tk.Label(win, text="Roll no ")
    rollnoE = tk.Entry(win, textvariable=Rollno, width=30, relief="groove", bd=2)

    blood = tk.Label(win, text="Blood group ")
    bloodE = ttk.Combobox(win, textvariable=BloodGroup, values=["Select blood group",'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], width=27)

    dob = tk.Label(win, text="DOB (DD-MM-YYYY)")
    dobE = tk.Entry(win, textvariable=DOB, width=30, relief='groove', bd=2)

    genderL = tk.Label(win, text="Gender")
    genderI = ttk.Combobox(win, textvariable=Gender, values=["Select gender", "Male", "Female", "Others"], width=27)

    submit = ttk.Button(win, text="Submit", state="normal", width=15, command=lambda: store(Name, Regno, Rollno, DOB, BloodGroup, Gender))
    empty = tk.Label(win, text="")
    show = ttk.Button(win, text="Show database", state="normal", width=15, command=database)

    cleareB=ttk.Button(win,state="TButton",width=15,command=cleare,text="Clear")

    heading.grid(row=0, column=1, padx=5, pady=10)
    name.grid(row=1, column=0, padx=30, pady=5, sticky="w")
    nameE.grid(row=1, column=1, padx=5, pady=5)
    empty.grid(row=0, column=3)

    regno.grid(row=2, column=0, padx=30, pady=5, sticky="w")
    regnoE.grid(row=2, column=1, padx=5, pady=5)
    rollno.grid(row=3, column=0, padx=30, pady=5, sticky="w")
    rollnoE.grid(row=3, column=1, padx=5, pady=5)
    blood.grid(row=4, column=0, padx=30, pady=5, sticky="w")
    bloodE.grid(row=4, column=1, padx=5, pady=5)
    dob.grid(row=5, column=0, padx=30, pady=5, sticky="w")
    dobE.grid(row=5, column=1, padx=5, pady=5)
    genderL.grid(row=6, column=0, padx=30, pady=5, sticky="w")
    genderI.grid(row=6, column=1, padx=5, pady=5)
    submit.grid(row=7, column=1, padx=10, pady=10,sticky='se')
    cleareB.grid(row=7,column=1,padx=10,pady=10,sticky='w')
    show.grid(row=8,column=1,padx=10,pady=10,sticky='s')

    win.mainloop()

mainwindow()
