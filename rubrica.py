import os
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from datos import *
from tkinter.filedialog import askopenfilename

mydb=sqlite3.connect('example.db')

cursor=mydb.cursor()




width=15



class StudentGUI():
    def __init__(self):
        frame=Frame()
        frame.pack(fill=X)
        self.section=Combobox(frame,width=width,values=secciones)
        self.section.bind("<<ComboboxSelected>>",self.setListNames)

        self.name=Combobox(frame,width=30)

        r=0

        label1=Label(frame,text="Seccion",width=10)
        label1.grid(column=0,row=r)
        self.section.grid(column=1,row=r,sticky=W)

        r=r+1

        label2=Label(frame,text="Nombre",width=10)
        label2.grid(column=0,row=r)
        self.name.grid(column=1,row=r,sticky=W)

    def setListNames(self,event):
        query="""SELECT name
                 FROM students
                 WHERE section=?"""

        cursor.execute(query,(self.section.get(),))

        student_name_list=[name for name in cursor]

        self.name["values"]=student_name_list


class LaboratoryGUI():
    def __init__(self):
        frame=Frame()
        frame.pack(fill=X)
        self.laboratoryNumber=Combobox(frame,width=width,values=laboratories)
        r=0

        label1=Label(frame,text="Laboratory",width=10)
        label1.grid(column=0,row=r)
        self.laboratoryNumber.grid(column=1,row=r,sticky=W)

class EvaluationGUI():
    def __init__(self):
        frame=Frame()
        frame.pack(fill=X)

        self.puntajes={}
        self.nota=0

        r=0

        label=Label(frame,text="Calificaciones")
        label.grid(column=0,row=r)
        r=r+1

        index=0
        for _field in criterios:
            c=0
            l=Label(frame,text=_field)
            l.grid(column=c,row=r)

            self.puntajes[_field]=IntVar()

            c=c+1
            for _value in criterios[_field]:
                radio=Radiobutton(frame,text=str(_value),
                                        value=_value,
                                        variable=self.puntajes[_field],
                                        width=4,
                                        command=self.sumarPuntos)
                radio.grid(column=c,row=r)
                c=c+1

            r=r+1
            index=index+1

        self.puntosLabel=Label(frame,text="Puntos Totales")
        self.puntosLabel.grid(column=0,row=r)

        self.puntosTotalesLabel=Label(frame,text="0")
        self.puntosTotalesLabel.grid(column=1,row=r)

        r=r+1
        self.commentLabel=Label(frame,text="Comentaios")
        self.commentLabel.grid(column=0,row=r)

        self.comments=Text(frame,height=4,width=30)
        self.comments.grid(column=1,row=r,columnspan=5)

    def sumarPuntos(self):
        self.nota=0
        for field in self.puntajes:
            self.nota=self.nota+self.puntajes[field].get()

        self.puntosTotalesLabel["text"]=str(self.nota)



class Mygui(StudentGUI,LaboratoryGUI,EvaluationGUI):
    def __init__(self,master):

        self.master=master
        self.master.title("Calificaciones de Ciruitos Digitales")
        LaboratoryGUI.__init__(self)
        StudentGUI.__init__(self)
        EvaluationGUI.__init__(self)
        self.tipo()
        self.showBoton()

    def selectInforme(self):

        FILETYPES= (("pdf files", '*.pdf'),)
        TITLE="Selecionar Informe"

        self.path=askopenfilename(title=TITLE, filetypes=FILETYPES)
        self.pathinforme["text"]=os.path.basename(self.path)


    def tipo(self):
        frame=Frame()
        frame.pack(fill=X)

        l1=Label(frame,text="Tipo de Evidencia")
        l1.grid(column=0,row=0)

        self.tipo=Combobox(frame,width=width,values=("Mejor", "Peor", "Promedio"))
        self.tipo.grid(column=1,row=0)

        l2=Label(frame,text="informe")
        l2.grid(column=0,row=1)

        self.pathinforme=Label(frame,text="")
        self.pathinforme.grid(column=1,row=1)


    def showBoton(self):
        frame=Frame()
        frame.pack(fill=X)

        button=Button(frame,text="Generar PDF",command=self.generatePDF)
        button.pack(side=RIGHT)

        button=Button(frame,text="Select informe",command=self.selectInforme)
        button.pack(side=RIGHT)

    def generatePDF(self):


        rubrica={}

        rubrica["name"]=self.name.get()
        rubrica["section"]=self.section.get()

        for field in self.puntajes:
            rubrica[field]=self.puntajes[field].get()

        rubrica["total"]=self.nota

        rubrica["laboratorio"]=self.laboratoryNumber.get()
        rubrica["comments"]=self.comments.get("1.0","end-1c")

        rubrica["filepath"]=self.path
        rubrica["tipo"]=self.tipo.get()

        writeRubrica(rubrica)



top=Tk()

my_gui=Mygui(top)

top.resizable(0,0)

top.mainloop()


