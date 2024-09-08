from re import L
from tkinter import *
from tkinter.font import BOLD
import tkinter.messagebox as tkMessageBox
import sqlite3
from turtle import left
from matplotlib import image
import pyttsx3
from PIL import ImageTk, Image
class mainwindow:
    def  __init__(self,master):
        self.master = master

        #frame= Frame(width=700,height=600)
        #frame.pack()

        self.heading = Label(root, text="        Receptionless Doctor          ", font=('arial 25 bold'), fg='black', bg='grey')
        self.heading.place(x=0, y=0)
        self.heading = Label(root, text="        Appointment system           ", font=('arial 25 bold'), fg='black', bg='grey')
        self.heading.place(x=0, y=40)

        '''
        canvas = Canvas(root,width=100,height=100)
        canvas.pack()
        img = PhotoImage(file='d.ppm')
        canvas.create_image(20,20,anchor =NW,Image=img)
        '''

        # self.submit = Button(root, text="Add Appointment", width=20, height=2, bg='green',command=self.appointments)
        # self.submit.place(x=175, y=200)

        self.submit = Button(root, text="Display ", width=20, height=3, bg='steelblue',command=self.display)
        self.submit.place(x=175, y=120)

        self.submit = Button(root, text="Update", width=20, height=3, bg='red',command=self.update)
        self.submit.place(x=175, y=210)

    def display(self):
        root = Tk()
        self.x = 0
        # connection to database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # empty lists to append later
        number = []
        patients = []

        sql = "SELECT * FROM appointments"
        res = c.execute(sql)
        for r in res:
            ids = r[0]
            name = r[1]
            number.append(ids)
            patients.append(name)


        # function to speak the text and update the text
        def func():
            n.config(text=str(number[self.x]))
            pname.config(text=str(patients[self.x]))
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
            engine.runAndWait()
            self.x += 1


        # heading
        heading = Label(root, text="Appointments", font=('arial 60 bold'), fg='green')
        heading.place(x=350, y=0)

        # button to change patients
        change = Button(root, text="Next Patient", width=25, height=2, bg='steelblue', command=func)
        change.place(x=500, y=600)

        # empty text labels to later config
        n = Label(root, text="", font=('arial 200 bold'))
        n.place(x=500, y=100)

        pname = Label(root, text="", font=('arial 80 bold'))
        pname.place(x=300, y=400)


        root.geometry("1200x720+0+0")
        root.resizable(False, False)
        root.mainloop()

    def update(self):
        root = Tk()
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        """sample1 = StringVar()
        sample3 = StringVar()
        sample2 = StringVar()
        sample4 = StringVar()
        sample5 = StringVar()
        sample6 = StringVar()"""


        def search_db():
            input = namenet.get()
            # creating the update form
            # execute sql

            sql = "SELECT * FROM appointments WHERE name LIKE ?"
            res = c.execute(sql, (input,))
            for row in res:
                name1 = row[1]
                age = row[2]
                gender = row[3]
                location = row[4]
                time = row[6]
                phone = row[5]

            uname = Label(root, text="Patient's Name", font=('arial 18 bold'))
            uname.place(x=0, y=140)

            uage = Label(root, text="Age", font=('arial 18 bold'))
            uage.place(x=0, y=180)

            ugender = Label(root, text="Gender", font=('arial 18 bold'))
            ugender.place(x=0, y=220)

            ulocation = Label(root, text="Location", font=('arial 18 bold'))
            ulocation.place(x=0, y=260)

            utime = Label(root, text="Appointment Time", font=('arial 18 bold'))
            utime.place(x=0, y=300)

            uphone = Label(root, text="Phone Number", font=('arial 18 bold'))
            uphone.place(x=0, y=340)

            # entries for each labels==========================================================
            # ===================filling the search result in the entry box to update
            ent1 = Entry(root, width=30)
            ent1.place(x=300, y=140)
            ent1.insert(END, str(name1))

            ent2 = Entry(root, width=30)
            ent2.place(x=300, y=180)
            ent2.insert(END, str(age))

            ent3 = Entry(root, width=30)
            ent3.place(x=300, y=220)
            ent3.insert(END, str(gender))

            ent4 = Entry(root, width=30)
            ent4.place(x=300, y=260)
            ent4.insert(END, str(location))

            ent5 = Entry(root, width=30)
            ent5.place(x=300, y=300)
            ent5.insert(END, str(time))

            ent6 = Entry(root, width=30)
            ent6.place(x=300, y=340)
            ent6.insert(END, str(phone))

            # button to execute update
            update = Button(root, text="Update", width=20, height=2, bg='lightblue', command= lambda :update_db(ent1,ent2,ent3,ent4,ent5,ent6))
            update.place(x=400, y=380)

            # button to delete
            delete = Button(root, text="Delete", width=20, height=2, bg='red', command=lambda :delete_db(ent1,ent2,ent3,ent4,ent5,ent6))
            delete.place(x=150, y=380)

        heading = Label(root, text="Update Appointments", fg='steelblue', font=('arial 40 bold'))
        heading.place(x=150, y=0)

        # search criteria -->name
        name = Label(root, text="Enter Patient's Name", font=('arial 18 bold'))
        name.place(x=0, y=60)

        # entry for  the name
        namenet = Entry(root, width=30)
        namenet.place(x=280, y=62)

        # search button
        search = Button(root, text="Search", width=12, height=1, bg='steelblue', command=search_db)
        search.place(x=350, y=102)
        def update_db(ent1,ent2,ent3,ent4,ent5,ent6):
            # declaring the variables to update
            var1 = ent1.get()  # updated name
            var2 = ent2.get()  # updated age
            var3 = ent3.get()  # updated gender
            var4 = ent4.get()  # updated location
            var5 = ent5.get()  # updated phone
            var6 = ent6.get()  # updated time
            #  print(var1,var2,var3,var4,var5,var6)

            query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
            c.execute(query, (var1, var2, var3, var4, var5, var6, namenet.get(),))
            conn.commit()
            tkMessageBox.showinfo("Updated", "Successfully Updated.")

        def delete_db(ent1,ent2,ent3,ent4,ent5,ent6):
            # delete the appointment
            sql2 = "DELETE FROM appointments WHERE name LIKE ?"
            c.execute(sql2, (namenet.get(),))
            conn.commit()
            tkMessageBox.showinfo("Success", "Deleted Successfully")
            ent1.destroy()
            ent2.destroy()
            ent3.destroy()
            ent4.destroy()
            ent5.destroy()
            ent6.destroy()

        root.geometry("1200x720+0+0")
        root.resizable(False, False)
        root.mainloop()

root = Tk()
mainwindow(root)
root.geometry("500x500")

root.title("Doctors Side")

img=ImageTk.PhotoImage(Image.open("doctor.jpg"))
l=Label(image=img)
l.pack(side=BOTTOM,anchor="center")

root.resizable(False, False)
root.mainloop()
