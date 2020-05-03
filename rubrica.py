import os
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from datos import *

mydb=sqlite3.connect('example.db')

cursor=mydb.cursor()

individual=[
            ("test"   ,(4,3,2,1,0)),
            ("actitud",(2,1,0))
           ]


grupal=[
         ("experiment1",(4,3,2,1,0)),
         ("experiment2",(4,3,2,1,0)),
         ("experiment3",(4,3,2,1,0)),
         ("informe"    ,(2,1,0)    )
         ]

laboratory_tables=("Laboratorio_1",
                   "Laboratorio_2",
                   "Laboratorio_3",
                   "Laboratorio_4",
                   "Laboratorio_5",
                   "Laboratorio_6",
                   "Laboratorio_7",
                   )

secciones=("1.01",
           "1.02",
           "2.01",
           "2.02")

width=15

class Student():
    def __init__(self,frame,alumno,table):
        self.table=table
        self.label=Label(frame,text=alumno)

        self.section=Combobox(frame,width=width,values=secciones,state="disable")
        self.section.bind("<<ComboboxSelected>>",self.setListNames)

        self.name=Combobox(frame,width=30,state="disable")
        self.name.bind("<<ComboboxSelected>>", lambda event: self.showGrades())

        self.buttons=[]
        self.grades=[]

    def enable(self):
        self.section["state"]="normal"
        self.name["state"]="normal"

        for button in self.buttons:
            button["state"]="normal"

    def disable(self):
        self.section["state"]="disable"
        self.name["state"]="disable"

        for button in self.buttons:
            button["state"]="disable"

    def show(self,row):
        self.label.grid(column=0,row=row)
        self.section.grid(column=1,row=row)
        self.name.grid(column=2,row=row)

    def setListNames(self,event):
        query="""SELECT name
                 FROM students
                 WHERE section=?"""

        cursor.execute(query,(self.section.get(),))

        student_name_list=[name for name in cursor]

        self.name["values"]=student_name_list

    def getPK(self):

        query="""SELECT student_id
                 FROM students
                 WHERE name=?"""

        cursor.execute(query,(self.name.get()[1:-1],))
        [pk]=cursor.fetchone()

        return pk

    def calificarField(self,field,value):
        query="""UPDATE {}
                 SET {}=?
                 WHERE student_id=?""".format(self.table.get(),field)
        pk=self.getPK()

        values=(value.get(),pk)
        cursor.execute(query,values)
        mydb.commit()

        self.showGrades()

    def selectField(self,field):
        query="""SELECT {}
                 FROM   {}
                 WHERE student_id= ?""".format(field,self.table.get())
        pk=self.getPK()
        cursor.execute(query,(pk,))

        [value]=cursor.fetchone()
        return value

    def showGrades(self):

        index=0
        for _field,values in individual:
            grade=self.selectField(_field)
            self.grades[index]["text"]=grade
            index=index+1

    def sumarPuntaje(self):
        suma = "nota ="

        for field in individual:
            suma=suma + "+" + field[0]

        for field in grupal:
            suma=suma + "+"+ field[0]

        query="""UPDATE {}
                 SET {}
                 where student_id = ?""".format(self.table.get(),suma)
        pk=self.getPK()

        cursor.execute(query,(pk,))
        mydb.commit()


    def showCriterios(self,frame,row):

        _variables=[]
        _commands=[]

        r=row
        label=Label(frame,text=self.label["text"])
        label.grid(column=0,row=row)
        r=r+1

        index=0
        for _field, _values in individual:
            c=0
            l=Label(frame,text=_field,width=width)
            l.grid(column=c,row=r)

            _variables.append(IntVar())

            _command=lambda field=_field, i=index: self.calificarField(field,_variables[i])
            _commands.append(_command)

            c=c+1
            for _value in _values:
                radio=Radiobutton(frame,text=str(_value),
                                        value=_value,
                                        variable=_variables[index],
                                        width=4)
                radio.grid(column=c,row=r)
                c=c+1

            c=6
            button=Button(frame,text="calificar",
                                command=_commands[index])
            button.grid(column=c,row=r)
            self.buttons.append(button)

            c=7
            grade=Label(frame,text="",width=4,anchor=CENTER)
            grade.grid(column=c,row=r)
            self.grades.append(grade)

            r=r+1
            index=index+1

    def commentar(self,ent):
            pk=self.getPK()
            values=(ent.get("1.0","end-1c"),pk)
            query="""UPDATE {}
                     SET Comments = ?
                     WHERE student_id = ?""".format(self.table.get())

            cursor.execute(query,values)
            mydb.commit()



    def generatePDF(self):
            pk=self.getPK()

            data={}

            data["laboratorio"]=self.table.get()

            for _field,_values in individual:
                h=self.selectField(_field)
                data[_field]=h

            for _field,_values in grupal:
                h=self.selectField(_field)
                data[_field]=h

            data["total"]=self.selectField("nota")
            data["comments"]=self.selectField("comments")

            query="select name,section from students where student_id=?"

            cursor.execute(query,(pk,))

            [name,section]=cursor.fetchone()
            data["name"]=name
            data["section"]=section

            writeRubrica(data)


class Grupo():
    def __init__(self,frame,table):
        self.table=table
        self.frame=frame
        self.numberOfStudents=IntVar()

        self.student1=Student(frame,"Alumno1",self.table)
        self.student2=Student(frame,"Alumno2",self.table)
        self.student3=Student(frame,"Alumno3",self.table)


    def showStudents(self,row):
        seccion=Label(self.frame,text="Seccion")
        seccion.grid(column=1,row=row)
        nombre=Label(self.frame,text="Nombre")
        nombre.grid(column=2,row=row)
        self.student1.show(row+1)
        self.student2.show(row+2)
        self.student3.show(row+3)

    def setNumberOfStudents(self,r):
        c=0
        label=Label(self.frame,text="Integrantes")
        label.grid(column=c,row=r)
        c=c+1
        for _value  in range(2,4):
            radio=Radiobutton(self.frame,
                              text=str(_value),
                              value=_value,
                              variable=self.numberOfStudents,
                              command=self.enableStudents)
            radio.grid(column=c,row=r)
            c=c+1

    def enableStudents(self):
        n=self.numberOfStudents.get()

        if n==2:
            self.student1.enable()
            self.student2.enable()
            self.student3.disable()
        elif n==3:
            self.student1.enable()
            self.student2.enable()
            self.student3.enable()

    def calificarField(self,field,value):
        n=self.numberOfStudents.get()

        if n==2:
            self.student1.calificarField(field,value)
            self.student2.calificarField(field,value)

        elif n==3:
            self.student1.calificarField(field,value)
            self.student2.calificarField(field,value)
            self.student3.calificarField(field,value)

        self.sumarPuntaje()

    def showCriterios(self):

        frame=Frame()
        frame.pack(fill=X)

        r=0
        label=Label(frame,text="Individuales")
        label.grid(column=0,row=r)

        r=r+1
        self.student1.showCriterios(frame,r)
        r=r+len(individual) + 1

        self.student2.showCriterios(frame,r)
        r=r+len(individual) + 1

        self.student3.showCriterios(frame,r)
        r=r+len(individual) + 1

        label=Label(frame,text="Grupales")
        label.grid(column=0,row=r)

        r=r+1

        _variables=[]
        _commands=[]
        index=0
        for _field, _values in grupal:
            c=0
            l=Label(frame,text=_field,width=width)
            l.grid(column=c,row=r)
            _variables.append( IntVar() )

            _command=lambda field=_field, i=index: self.calificarField(field, _variables[i])
            _commands.append(_command)

            c=c+1
            for _value in _values:
                radio=Radiobutton(frame,
                                  text=str(_value),
                                  value=_value,
                                  variable=_variables[index],
                                  width=4)
                radio.grid(column=c,row=r)
                c=c+1

            c=6
            button=Button(frame,text="Calificar",command=_commands[index])
            button.grid(column=c,row=r)

            index=index+1
            r=r+1

        l2=Label(frame,text="comentar",width=width)
        l2.grid(column=0,row=r)

        self.comments=Text(frame,height=4,width=40)
        self.comments.grid(column=1,row=r,columnspan=5)

        button=Button(frame,text="Comentar",command=self.comentarGrupo)
        button.grid(column=6,row=r)

        r=r+1
        l3=Label(frame,text="Alumno1 nota")
        l3.grid(column=0,row=r)
        self.nota1=Label(frame,text="0")
        self.nota1.grid(column=1,row=r)
        r=r+1
        l4=Label(frame,text="Alumno2 nota")
        l4.grid(column=0,row=r)
        self.nota2=Label(frame,text="0")
        self.nota2.grid(column=1,row=r)

    def comentarGrupo(self):
       n=self.numberOfStudents.get()
       if n==2:
           self.student1.commentar(self.comments)
           self.student2.commentar(self.comments)
       elif n==3:
           self.student1.commentar(self.comments)
           self.student2.commentar(self.comments)
           self.student3.commentar(self.comments)


    def sumarPuntaje(self):
        n=self.numberOfStudents.get()

        if n==2:
            self.student1.sumarPuntaje()
            self.student2.sumarPuntaje()

            self.nota1["text"]=self.student1.selectField("nota")
            self.nota2["text"]=self.student2.selectField("nota")
        elif n==3:
            self.student1.sumarPuntaje()
            self.student2.sumarPuntaje()
            self.student3.sumarPuntaje()



    def generatePDFs(self):
        n=self.numberOfStudents.get()

        if n==2:
            self.student1.generatePDF()
            self.student2.generatePDF()
        elif n==3:
            self.student1.generatePDF()
            self.student2.generatePDF()
            self.student3.generatePDF()


    def showSumarBoton(self):
        frame=Frame()
        frame.pack(fill=X)
        button=Button(frame,text="sumar",command=self.sumarPuntaje)
        button.pack(side=RIGHT)

        button=Button(frame,text="Generar PDF",command=self.generatePDFs)
        button.pack(side=RIGHT)




class Mygui():
    def __init__(self,master):
        self.master=master
        self.master.title("Calificaciones de Ciruitos Digitales")
        self.datos()

    def datos(self):
        frameDatos=Frame()
        frameDatos.pack(fill=X)
        frameCriterios=Frame()
        frameCriterios.pack(fill=X)

        r=0
        self.LaboratorioLabel=Label(frameDatos,text="Sesion: ",anchor="w")
        self.LaboratorioLabel.grid(column=0,row=r)
        self.Laboratorio=Combobox(frameDatos,width=15,values=laboratory_tables)
        self.Laboratorio.grid(column=1,row=r)

        self.grupo=Grupo(frameDatos,self.Laboratorio)
        r=r+1
        self.grupo.setNumberOfStudents(r)
        r=r+1
        self.grupo.showStudents(r)

        self.grupo.showCriterios()

        self.grupo.showSumarBoton()


top=Tk()
my_gui=Mygui(top)

top.resizable(0,0)

top.mainloop()


