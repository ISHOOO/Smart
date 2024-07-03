import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

def subjectchoose(text_to_speech):
 

    subject = CTk()
    # windo.iconbitmap("AMS.ico")
    subject.title("Student Info")
    subject.geometry("580x400")
    subject.resizable(0, 0)
    subject.configure(background="black")
    # subject_logo = Image.open("UI_Image/0004.png")
    # subject_logo = subject_logo.resize((50, 47), resample=PIL.Image.Resampling.LANCZOS)
    # subject_logo1 = ImageTk.PhotoImage(subject_logo)

    titl = tk.Label(subject, bg="#42aaf5", relief=RIDGE, bd=10, font=("arial", 35))
    titl.pack(fill=X)
    # l1 = tk.Label(subject, image=subject_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = tk.Label(
        subject,
        bg="#42aaf5", 
        fg="White",
        font=("Helvetica", 30,'bold'),
        text="View Student Info.",
    )
    titl.place(x=200, y=12)

    sub = tk.Label(
        subject,
        text="Enter Enrollment No: ",
        bg="#242424",
        fg="yellow",
        font=("Helvetica", 22,'bold'),
    )
    sub.place(x=70, y=140)

    tx = CTkEntry(
        subject,
        width=200,
        height=40,
        fg_color="black",
        text_color= 'White',
        corner_radius = 90,
        font=("Helvetica", 22, "bold"),
    )
    tx.place(x=310, y=110)

    clab = tk.Label(
        subject,
        text="Enter Class :",
        bg="#242424",
        fg="yellow",
        font=("Helvetica", 22,'bold'),
    )
    clab.place(x=70, y=206)

    cla = CTkEntry(
        subject,
        width=200,
        height=40,
        fg_color="black",
        text_color= 'White',
        corner_radius = 90,
        font=("Helvetica", 22, "bold"),
    )
    cla.place(x=310, y=160)
    

    def fethEn():

        ImageUI = CTkToplevel()
        ImageUI.title("Student Card")
        ImageUI.geometry("840x550")
        ImageUI.configure(background="#242424")
        ImageUI.resizable(0, 0)
        canvasCard = Canvas(ImageUI,border = 0,height=800,width=1200, background='#282424')
        canvasCard.pack()

        def round_rectangle(x1, y1, x2, y2, radius=80, **kwargs):
        
            points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

            return canvasCard.create_polygon(points, **kwargs, smooth=True)

        round_rectangle(50, 50, 1000, 650, radius=80, fill="White")

        enrollment_check = int(tx.get())
        clas = cla.get()

        with open(f'Attendance\{clas}\studentdetails.csv', mode ='r') as df:
            csvFile = csv.DictReader(df)
            for lines in csvFile:
                data = lines

        df = pd.read_csv(f'Attendance\{clas}\studentdetails.csv')  
        
        matching_rows = df[df['Enrollment'] ==  enrollment_check]

        


        if not matching_rows.empty:
            enroll, Name, classF, dob, fatherName, courseS, ph  =  (matching_rows.to_string(index=False,header=False)).split(' ', 6)

            enroll = data["Enrollment"]
            Name = data["Name"]
            classF = data["Class"]
            dob = data["Dob"]
            fatherName = data["FatherName"]
            courseS = data["Course"]
            ph = data["Phone"]  
            
            name = tk.Label(
            canvasCard,
            text='Name :',
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            name.place(x=400, y=230)
            
            naam = tk.Label(
            canvasCard,
            text=Name,
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            naam.place(x=670, y=230)

            enrollF = tk.Label(
            canvasCard,
            text='Roll No. : ',
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            enrollF.place(x=400, y=470)

            en = tk.Label(
            canvasCard,
            text='0'+enroll+'14902021',
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            en.place(x=670, y=470)

            claaa = tk.Label(
            canvasCard,
            text='Class : ',
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            claaa.place(x=400, y=350)

            claL = tk.Label(
            canvasCard,
            text=classF,
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            claL.place(x=670, y=350)

            dobb = tk.Label(
            canvasCard,
            text='DOB : ',
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            dobb.place(x=400, y=410)

            Dob = tk.Label(
            canvasCard,
            text=dob,
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            Dob.place(x=670, y=410)

            Fn = tk.Label(
            canvasCard,
            text="Father's Name : ",
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            Fn.place(x=400, y=290)

            FatNA = tk.Label(
            canvasCard,
            text=fatherName,
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            FatNA.place(x=670, y=290)

            cor = tk.Label(
            canvasCard,
            text="Course : ",
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            cor.place(x=400, y=530)
            
            course = tk.Label(
            canvasCard,
            text=courseS,
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            course.place(x=670, y=530)

            pHONE = tk.Label(
            canvasCard,
            text="Phone : ",
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            pHONE.place(x=400, y=590)
            
            pho = tk.Label(
            canvasCard,
            text=ph,
            fg="Black",
            bg='White',
            font=("Helvetica", 23,'bold'),
            )
            pho.place(x=670, y=590)

            logHead = tk.Label(
            canvasCard,
            text="MAHARAJA SURAJMAL INSTITUTE",
            fg="Blue",
            bg='White',
            font=("Times New Roman", 32,'bold'),
            )
            logHead.place(x=200, y=60)

            aff = tk.Label(
            canvasCard,
            text="(Affiliated to GGS Indraprastha University, Delhi)",
            fg="green",
            bg='white',
            font=("Helvetica", 23,'bold'),
            )
            aff.place(x=220, y=110)

            add = tk.Label(
            canvasCard,
            text="C-4, Janak Puri, New Delhi-110015\nTel: 25528116/7,25552667, Telfax: 25528116",
            fg="red",
            bg='white',
            font=("Helvetica", 18,'bold'),
            )
            add.place(x=290, y=150)

            def exit_btn():

                ImageUI.destroy()
                ImageUI.update()    

            exi = CTkButton(
            ImageUI,
            fg_color="#42aaf5",
            bg_color="white",
            height = 40,
            width= 90,
            font=("Helvetica", 19,'bold'),
            hover_color="red",
            corner_radius= 90,
            command= exit_btn,
            text="EXIT",
            )
            exi.place(x=140, y=420)
            try:
                ri = Image.open(f'StudentImages\{enroll}{Name}.jpg')
            except:
                ri = Image.open(f'TrainingImage\{enroll}_{Name}\{Name}_{enroll}_50.jpg')
            
            new_size = (220, 220)
            ri = ri.resize(new_size, Image.Resampling.LANCZOS)
            r = ImageTk.PhotoImage(ri)
            label1 = Label(canvasCard, image=r)
            label1.image = r 
            label1 = tk.Label(canvasCard, text = 'Submit', fg = 'black', image= r,bg = '#282424',borderwidth=6) 
            label1.place(x=110, y=260)

            log = Image.open(f'UI_Image\IdLogo.png')
            new_size = (120, 120)
            log = log.resize(new_size, Image.Resampling.LANCZOS)
            l = ImageTk.PhotoImage(log)
            label2 = Label(canvasCard, image=l)
            label2.image = l 
            label2 = tk.Label(canvasCard, text = 'Submit', fg = 'black', image= l,bg = 'White',borderwidth=6) 
            label2.place(x=70, y=62)

            canvasCard.create_line(50, 220,1000, 220, width=8, fill='green')


        else:
            nod = tk.Label(
            canvasCard,
            text='No Enrollment Number found!!',
            bg="#242424",
            fg="yellow",
            font=("Helvetica", 23,'bold'),
            )
            nod.place(x=300, y=300)

    fill_a = CTkButton(
        subject,
        fg_color="#42aaf5",
        height = 40,
        width= 90,
        font=("Helvetica", 19,'bold'),
        hover_color="#27638f",
        corner_radius= 90,
        command= fethEn,
        text="Show Student ID Card",
        )
    fill_a.place(x=170, y=250)

    viewS = CTkButton(
        subject,
        fg_color="#42aaf5",
        height = 0,
        width= 0,
        font=("Helvetica", 19,'bold'),
        hover_color="#27638f",
        corner_radius= 50,
        #command= Attf,
        text="",
        )
    viewS.place(x=800, y=250)

    def exit_btn():

        subject.destroy()
        subject.update()

    tre = CTkButton(
        master=subject,
        text="EXIT",
        command=exit_btn,
        fg_color="#42aaf5",
        height = 40,
        width= 100,
        font=("Helvetica", 18,'bold'),
        hover_color="#e04141",
        corner_radius= 90,
    )   
    tre.place(x=250, y=310)
    
    
    subject.mainloop()
