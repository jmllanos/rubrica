import os

Lab1={"numero":1,
      "titulo":"Compuertas Lógicas en VHDL"}

Lab2={"numero":2,
      "titulo":"Circuitos combinatorios en VHDL"}

Lab3={"numero":3,
      "titulo":"Comparador, MUX/DEMUX, CODE/DECODE"}

Lab4={"numero":4,
      "titulo":"ALU"}

Lab5={"numero":5,
      "titulo":"Circuitos Secuenciales"}
 
Lab6={"numero":6,
      "titulo":"Maquinas de estado"}

Lab7={"numero":7,
      "titulo":"Memorias"}

def writeRubrica(data):

    name=data["name"]
    seccion=data["section"]
    test=data["test"]
    exper1=data["experiment1"]
    exper2=data["experiment2"]
    exper3=data["experiment3"]
    informe=data["informe"]
    actitud=data["actitud"]
    comments=data["comments"]
    total=data["total"]
    laboratorio=data["laboratorio"]

    print(laboratorio)
    if laboratorio=="Laboratorio_1":
        lab=Lab1
    if laboratorio=="Laboratorio_2":
        lab=Lab2
    if laboratorio=="Laboratorio_3":
        lab=Lab3
    if laboratorio=="Laboratorio_4":
        lab=Lab4
    if laboratorio=="Laboratorio_5":
        lab=Lab5
    if laboratorio=="Laboratorio_6":
        lab=Lab6
    if laboratorio=="Laboratorio_7":
        lab=Lab7



    datos=open("datos.tex","w")

    l1="\\alumnonombre{{{}}}".format(name)
    l2="\\alumnoseccion{{{}}}".format(seccion)
    l3="\\puntajetest{{{}}}".format(test)
    l4="\\puntajecriterioi{{{}}}".format(exper1)
    l5="\\puntajecriterioii{{{}}}".format(exper2)
    l6="\\puntajecriterioiii{{{}}}".format(exper3)
    l7="\\puntajeinforme{{{}}}".format(informe)
    l8="\\puntajeactitud{{{}}}".format(actitud)
    l9="\\puntajetotal{{{}}}".format(total)
    l10="\\comentarios{{{}}}".format(comments)

    l11="\\numero{{{}}}".format(lab["numero"])
    l12="\\titulo{{{}}}".format(lab["titulo"])


    datos.writelines(l1)
    datos.write("\n")
    datos.writelines(l2)
    datos.write("\n")
    datos.writelines(l3)
    datos.write("\n")
    datos.writelines(l4)
    datos.write("\n")
    datos.writelines(l5)
    datos.write("\n")
    datos.writelines(l6)
    datos.write("\n")
    datos.writelines(l7)
    datos.write("\n")
    datos.writelines(l8)
    datos.write("\n")
    datos.writelines(l9)
    datos.write("\n")
    datos.writelines(l10)
    datos.write("\n")
    datos.writelines(l11)
    datos.write("\n")
    datos.writelines(l12)
    datos.write("\n")

    datos.close()

    cmd="pdflatex --jobname={}_sec{}_\"{}\" main.tex".format(laboratorio,seccion,name)
    os.system(cmd)

    cmd="rm *.aux"
    os.system(cmd)

    cmd="rm *.log"
    os.system(cmd)

    cmd="mv *.pdf Laboratorio/sec{}/{}".format(seccion,laboratorio)
    print(cmd)
    os.system(cmd)

