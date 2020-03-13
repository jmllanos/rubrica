import os
import tkinter
import mysql.connector

from tkinter import *
from tkinter.ttk import *

mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Juancho.94",
        database="Digitales"
        )

cursor=mydb.cursor()
cursor.execute("select name from students")

for x in cursor:
    print(x[0])

Labs=[lab for lab in range(1,8)]

class Mygui():

   def __init__(self,master):
        self.master=master
        self.master.title("Calificaciones de Leo")

        self.frameData=Frame()
        self.frameData.grid(column=0,row=0)
        self.frameGrades=Frame()
        self.frameGrades.grid(column=0,row=1)
        self.frameButtons=Frame()
        self.frameButtons.grid(column=0,row=2)

        self.Laboratorio=Label(self.frameData,text="Laboratorio: ",anchor="w")
        self.Laboratorio.grid(column=0,row=0)
        self.Laboratorio_number=Combobox(self.frameData,width=10,values=Labs)
        self.Laboratorio_number.grid(column=1,row=0)

        self.seccion=Label(self.frameData,text="Seccion: ",anchor="w")
        self.seccion.grid(column=0,row=2)
        self.section_number=Combobox(self.frameData,width=10,values=("1.01","1.02"))
        self.section_number.grid(column=1,row=2)
        self.section_number.bind("<<ComboboxSelected>>",self.alumnoslist)

        self.MysubmmitButton=Button(self.frameButtons,text="Submmit",command=self.ingresar)
        self.MysubmmitButton.grid(column=0,row=0)
        self.PDFGenerateButton=Button(self.frameButtons,text="Generate PDFs")

   def alumnoslist(self,event):
       query="select name from students where section= %s"
       cursor.execute(query,(self.section_number.get(),))

       print(cursor.statement)

       self.alumnos_list=[]
       self.alumnos_list=[row[0] for row in cursor]


       self.alumno1=Label(self.frameData,text="Alumno1")
       self.alumno1.grid(column=0,row=3)
       self.alumno1_list=Combobox(self.frameData,width=10,values=self.alumnos_list)
       self.alumno1_list.grid(column=1,row=3)

       self.alumno2=Label(self.frameData,text="Alumno2")
       self.alumno2.grid(column=0,row=4)
       self.alumno2_list=Combobox(self.frameData,width=10,values=self.alumnos_list)
       self.alumno2_list.grid(column=1,row=4)

       self.testAlumno1=IntVar()
       self.testAlumno2=IntVar()
       self.p1=IntVar()
       self.p2=IntVar()
       self.p3=IntVar()
       self.p4=IntVar()

       radios=[

       ("Test Alumno 1",self.testAlumno1,(1,2,3,4)),
       ("Test Alumno 2",self.testAlumno2,(1,2,3,4)),
       ("Pregunta 1",self.p1,(1,2,3,4)),
       ("Pregunta 2",self.p2,(1,2,3,4)),
       ("Pregunta 3",self.p3,(1,2,3,4)),
       ("Pregunta 4",self.p4,(1,2,3,4)),
       ]

       self.label=Label(self.frameGrades,text="Calificaciones: ")
       self.label.grid(column=0,row=5)

       c=0
       r=6

       for _label,_variable,_values in radios:
           c=0
           self.L2=Label(self.frameGrades,text=_label)
           self.L2.grid(row=r,column=c)
           for _value in _values:
               c=c+1
               item=Radiobutton(self.frameGrades,text=str(_value),variable=_variable,value=_value)
               item.grid(column=c,row=r)
           r=r+1

   def ingresar(self):
        print(self.p1.get())


top=tkinter.Tk()
my_gui=Mygui(top)

top.geometry("400x300")
top.resizable(0,0)

top.mainloop()


