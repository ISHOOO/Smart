import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *
from customtkinter import *

def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get()
        if Subject=="":
            t='Please enter the class name.'
            text_to_speech(t)
        os.chdir(
            f"Attendance\{Subject}"
        )
        filenames = glob(
            f"Attendance\{Subject}\{Subject}*.csv"
        )
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
            #newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv("attendance.csv", index=False)

        root = CTk()
        root.title("Attendance of "+Subject)
        root.configure(background="black")
        cs = f"Attendance\{Subject}\attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:

                    label = tkinter.Label(
                        root,
                        width=10,
                        height=1,
                        fg="yellow",
                        font=("Helvetica", 25,'bold'),
                        bg="black",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

    subject = CTk()
    # windo.iconbitmap("AMS.ico")
    subject.title("Subject...")
    subject.geometry("580x320")
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
        text="Enter the Class for Attendance",
    )
    titl.place(x=90, y=12)

    def Attf():
        sub = tx.get()
        if sub == "":
            t="Please enter the class name!!!"
            text_to_speech(t)
        else:
            os.startfile(f"Attendance\\{sub}")

    attf = CTkButton(
        subject,
        fg_color="#42aaf5",
        height = 40,
        width= 90,
        font=("Helvetica", 19,'bold'),
        hover_color="#27638f",
        corner_radius= 90,
        command=Attf,
        text="Check Sheets",
    )
    attf.place(x=310, y=170)

    sub = tk.Label(
        subject,
        text="Enter Class: ",
        bg="#242424",
        fg="yellow",
        font=("Helvetica", 22,'bold'),
    )
    sub.place(x=120, y=120)

    tx = CTkEntry(
        subject,
        width=200,
        height=40,
        fg_color="Black",
        text_color= 'White',
        corner_radius = 90,
        font=("Helvetica", 22, "bold"),
    )
    tx.place(x=260, y=93)

    fill_a = CTkButton(
        subject,
        fg_color="#42aaf5",
        height = 40,
        width= 90,
        font=("Helvetica", 19,'bold'),
        hover_color="#27638f",
        corner_radius= 90,
        command=calculate_attendance,
        text="View Attendance",

    )
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
    tre.place(x=236, y=235)
    
    fill_a.place(x=70, y=170)
    subject.mainloop()
