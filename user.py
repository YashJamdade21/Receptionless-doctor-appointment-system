from re import L
from tkinter import *
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

        self.submit = Button(root, text="Add Appointment", width=20, height=3, bg='green',command=self.appointments)
        self.submit.place(x=175, y=120)

        # self.submit = Button(root, text="Display ", width=20, height=2, bg='steelblue',command=self.display)
        # self.submit.place(x=175, y=300)

        self.submit = Button(root, text="Update", width=20, height=3, bg='red',command=self.update)
        self.submit.place(x=175, y=210)


    def appointments(self):

        def add_appointment():
            # getting the user inputs
            val1 = name_ent.get()
            val2 = age_ent.get()
            val3 = gender_ent.get()
            val4 = location_ent.get()
            val5 = drop_ent.get()
            val6 = phone_ent.get()
            # print(val1,val2,val3)

            # checking if the user input is empty
            if val1 == '' or val2 == '' or val3 == '' or val4 == '' or val5 == '':
                tkMessageBox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                # now we add to the database
                sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
                c.execute(sql, (val1, val2, val3, val4, val5, val6))
                conn.commit()
                tkMessageBox.showinfo("Success", "Appointment for " + str(val1) + " has been created")

                box.insert(END, 'Appointment fixed for ' + str(val1) + ' at ' + str(val5))

        root = Tk()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        ids = []
#add appointment- ----------
        # creating the frames in the master
        left = Frame(root, width=800, height=720, bg='steelblue')
        left.pack(side=LEFT)

        right = Frame(root, width=400, height=720, bg='pink')
        right.pack(side=RIGHT)
        #img= ImageTk.PhotoImage(Image.open('doctor.jpg'))
        #img.pack(side=RIGHT)

        # labels for the window
        heading = Label(left, text="Hospital Appointments", font=('arial 40 bold'), fg='black', bg='lightgreen')
        heading.place(x=0, y=0)
        # patients name
        name = Label(left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='steelblue')
        name.place(x=0, y=100)

        # age
        age = Label(left, text="Age", font=('arial 18 bold'), fg='black', bg='steelblue')
        age.place(x=0, y=140)

        # gender
        gender = Label(left, text="Gender", font=('arial 18 bold'), fg='black', bg='steelblue')
        gender.place(x=0, y=180)

        # location
        location = Label(left, text="Location", font=('arial 18 bold'), fg='black', bg='steelblue')
        location.place(x=0, y=220)

        # appointment time
        clicked = StringVar()
        clicked.set("9pm-10pm")

        drop = Label(left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='steelblue')
        drop.place(x=0, y=260)
        drop = OptionMenu(root,clicked,"10pm-1pm","2pm-3pm","5pm-6pm")
        drop.pack()

        # phone
        phone = Label(left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='steelblue')
        phone.place(x=0, y=300)

        # Entries for all labels============================================================
        name_ent = Entry(left, width=30)
        name_ent.place(x=250, y=100)

        age_ent = Entry(left, width=30)
        age_ent.place(x=250, y=140)

        gender_ent = Entry(left, width=30)
        gender_ent.place(x=250, y=180)

        location_ent = Entry(left, width=30)
        location_ent.place(x=250, y=220)

        drop_ent = Entry(left, width=30)
        drop_ent.place(x=250, y=260)

        phone_ent = Entry(left, width=30)
        phone_ent.place(x=250, y=300)

        # button to perform a command
        submit = Button(left, text="Add Appointment", width=20, height=2, bg='green',command=add_appointment)
        submit.place(x=300, y=340)

        # getting number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        result = c.execute(sql2)
        for row in result:
            id = row[0]
            ids.append(id)
           # ids.append(id)

        # ordering the ids
        new = sorted(ids)
        # final_id = new[len(ids)-1]
        # displaying the logs in our right frame
        logs = Label(right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        logs.place(x=0, y=0)

        box = Text(right, width=50, height=40)
        box.place(x=20, y=60)
        # box.insert(END, "Total Appointments till now :  " + str(final_id))
        # funtion to call when the submit button is clicked


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

root.title("Users Side")

img=ImageTk.PhotoImage(Image.open("doctor.jpg"))
l=Label(image=img)
l.pack(side=BOTTOM,anchor="center")

root.resizable(False, False)
root.mainloop()
