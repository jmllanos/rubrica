import os

criterios={
            "test":(4,3,2,1,0),
            "criterio1":(4,3,2,1,0),
            "criterio2":(4,3,2,1,0),
            "criterio3":(4,3,2,1,0),
            "informe":(2,1,0),
            "actitud":(2,1,0)
            }


laboratories=("Laboratorio1",
              "Laboratorio2",
              "Laboratorio3",
              "Laboratorio4",
              "Laboratorio5",
              "Laboratorio6",
              "Laboratorio7",
                   )

secciones=("1.01",
           "1.02",
           "2.02")


Lab1={"numero":1,
      "titulo":"Compuertas Lógicas en VHDL",
      "competencia":"Formular, sintetizar e implementar compuertas lógicas básicas usando Vivado y vhdl",
      "criterioi":"Implementa las compuertas lógicas AND, OR, NOT y sus equivalentes con NANDs usando VHDL",
      "criterioii":"Implementa un circuito digital y su versión equivalente con NANDs usando VHDL",
      "criterioiii":"Implementa la función lógica final"}

Lab2={"numero":2,
      "titulo":"Circuitos combinatorios en VHDL",
      "competencia":"Formular, sintetizar e implementar circuitos combinacionales usando Vivado y VHDL",
      "criterioi":"Implementar el sumador completo de 1 bit",
      "criterioii":"Implementar el sumador completo de 4 bits usando arquitectura de flujo de datos",
      "criterioiii":"Implementar el sumador completo de 4 bits usando arquitectura estructurada"}

Lab3={"numero":3,
      "titulo":"Comparador, Multiplexor y Decodificador",
      "competencia":"Formular, sintetizar e implementar circuitos combinacionales usando Vivado y VHDL",
      "criterioi":"Realiza el diseño de los circuitos en VHDL usando Vivado",
      "criterioii":"Realiza la simulación de los circuitos diseñados en VHDL usando Vivado",
      "criterioiii":"Implementar de los diseños en la tarjeta Basys3"}

Lab4={"numero":4,
      "titulo":"Unidad Aritmética Lógica (ALU)",
      "competencia":"Formular, sintetizar e implementar circuitos combinacionales usando Vivado y VHDL",
      "criterioi":"IRealiza el diseño de los circuitos en VHDL usando Vivado",
      "criterioii":"Realiza la simulación de los circuitos diseñados en VHDL usando Vivado",
      "criterioiii":"Realizar el análisis de recursos utilizados (LUTs)"}

Lab5={"numero":5,
      "titulo":"Circuitos Secuenciales",
      "competencia":"Formular, sintetizar e implementar circuitos secuenciales usando Vivado y VHDL",
      "criterioi":"Realiza el dise\~no de los circuitos secuenciales en VHDL usando Vivado",
      "criterioii":"Realiza la simulaci\'on de los circuitos secuenciales en VHDL usando Vivado",
      "criterioiii":"Realizar el análisis de recursos utilizados (LUTs)"}

Lab6={"numero":6,
      "titulo":"Maquinas de estado",
      "competencia":"Formular, sintetizar e implementar m\'aquinas de estados usando Vivado y VHDL",
      "criterioi":"Realiza el dise\~no de m\'aquinas de estados en VHDL usando Vivado",
      "criterioii":"Realiza la simulaci\'on de las m\'aquinas de estados en VHDL usando Vivado",
      "criterioiii":"Realizar el análisis de recursos utilizados (LUTs) y FlipFlops"}

Lab7={"numero":7,
      "titulo":"Memorias",
      "competencia":"Formular, sintetizar e implementar compuertas lógicas básicas usando Vivado y vhdl",
      "criterioi":"Implementa las compuertas l\'ogicas AND, OR, NOT y sus equivalentes con NANDs usando VHDL",
      "criterioii":"Implementa un circuito digital y su versi\'on equivalente con NANDs usando VHDL",
      "criterioiii":"Implementa la función lógica final"}

def writeRubrica(data):


    if data["laboratorio"]==laboratories[0]:
        lab=Lab1
    if data["laboratorio"]==laboratories[1]:
        lab=Lab2
    if data["laboratorio"]==laboratories[2]:
        lab=Lab3
    if data["laboratorio"]==laboratories[3]:
        lab=Lab4
    if data["laboratorio"]==laboratories[4]:
        lab=Lab5
    if data["laboratorio"]==laboratories[5]:
        lab=Lab6
    if data["laboratorio"]==laboratories[6]:
        lab=Lab7



    datos=open("datos.tex","w")

    lines=[]
    lines.append("\\alumnonombre{{{}}}".format(data["name"]))
    lines.append("\\alumnoseccion{{{}}}".format(data["section"]))

    lines.append("\\puntajetest{{{}}}".format(data["test"]))
    lines.append("\\puntajecriterioi{{{}}}".format(data["criterio1"]))
    lines.append("\\puntajecriterioii{{{}}}".format(data["criterio2"]))
    lines.append("\\puntajecriterioiii{{{}}}".format(data["criterio3"]))
    lines.append("\\puntajeinforme{{{}}}".format(data["informe"]))
    lines.append("\\puntajeactitud{{{}}}".format(data["actitud"]))

    lines.append("\\puntajetotal{{{}}}".format(data["total"]))
    lines.append("\\comentarios{{{}}}".format(data["comments"]))

    lines.append("\\numero{{{}}}".format(lab["numero"]))
    lines.append("\\titulo{{{}}}".format(lab["titulo"]))
    lines.append("\\competencia{{{}}}".format(lab["competencia"]))
    lines.append("\\criterioi{{{}}}".format(lab["criterioi"]))
    lines.append("\\criterioii{{{}}}".format(lab["criterioii"]))
    lines.append("\\criterioiii{{{}}}".format(lab["criterioiii"]))

    for line in lines:
        datos.write(line)
        datos.write("\n")

    datos.close()


    #cmd="pdflatex --jobname={}_sec{}_\"{}\" main.tex".format(data["laboratorio"],data["section"],data["name"][1:-2])
    #os.system(cmd)

    cmd="pdflatex --jobname=rubrica main.tex"
    os.system(cmd)

    if data["tipo"]=="Mejor":
        tipo=1
    elif data["tipo"]=="Peor":
        tipo=2
    elif data["tipo"]=="Promedio":
        tipo=3

    seccion=data["section"]
    lab=data["laboratorio"]

    fileName="2020_1_Circuitos_Digitales_{}_{}_{}".format(seccion,lab,tipo)

    cmd="pdfunite \"{}\" rubrica.pdf {}.pdf".format(data["filepath"],fileName)

    os.system(cmd)

    cmd="mv {}.pdf evidencias/{}".format(fileName,seccion)
    os.system(cmd)

    cmd="rm *.aux"
    os.system(cmd)

    cmd="rm *.log"
    os.system(cmd)

    #cmd="mv *.pdf Laboratorio/sec{}/{}".format(seccion,laboratorio)
    #print(cmd)
   # os.system(cmd)

