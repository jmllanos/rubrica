\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{utec_lab}[2020/04/08 notes]

\LoadClass[a4paper,12pt]{article}

\RequirePackage{geometry}
\geometry{a4paper,total={170mm,240mm}, left=15mm, top=20mm,headsep=12mm}

\RequirePackage[utf8]{inputenc}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage[spanish]{babel}
\RequirePackage{subcaption}
\RequirePackage{amsmath}
\RequirePackage{color,soul}
\RequirePackage{multirow}
\RequirePackage{makecell}
\RequirePackage{array}
\RequirePackage{tabularx}
\RequirePackage{ifthen}

%%Datos del Laboratorio

\newcommand{\curso}[1]{\def\cursoname{#1}}
\newcommand{\ciclo}[1]{\def\term{#1}}
\newcommand{\coordinador}[1]{\def\coordinatorname{#1}}
\newcommand{\numero}[1]{\def\laboratorynumber{#1}}
\newcommand{\titulo}[1]{\def\title{#1}}
\newcommand{\jefepracticas}[1]{\def\jefedepracticasname{#1}}

\curso{}
\ciclo{}
\coordinador{}
\numero{}
\titulo{}
\jefepracticas{}

\newcounter{count}
\newcommand{\experimento}[1]{
\addtocounter{count}{1}
\subsection*{Experimento \arabic{count}: #1}
}

\newenvironment{preguntas}
{\textbf{Preguntas:}
 \begin{itemize}}
{\end{itemize}}

\newenvironment{evidencias}
{\textbf{Evidencias:}
 \begin{itemize}}
{\end{itemize}}


\newenvironment{instrucciones}
{\textbf{Instrucciones:}
 \begin{enumerate}}
{\end {enumerate}}

\pagestyle{fancy}
\fancyhf{}
\rhead{\cursoname{} \term{}}
\lhead{\includegraphics[width=0.15\linewidth]{logo-utec.png}}
\cfoot{\thepage}

%% Caratula
\renewcommand{\maketitle}{
 \begin{titlepage}
    \begin{center}
       
        \vspace*{1cm}
        
        \huge
 
         \includegraphics[width=0.5\linewidth]{logo-utec.png}
         
         \vspace*{1cm}
  
         \textbf{Ingenier\'ia Electr\'onica \\4to. ciclo}
  
         \vspace{0.5cm}
         \textbf{\cursoname{}}
  
         \vspace{1.5cm}
  
         Gu\'ia de Laboratorio \laboratorynumber\\
  
         \textbf{\title} 
        
         \vspace{1.5cm}
       
     
         Jefe de pr\'acticas: \jefedepracticasname\\
         Coordinador del curso: \coordinatorname
         \vspace{1cm}
        
         \term{} 
         
    \end{center}
 \end{titlepage}
\newpage
}



%Rubrica datos de alumnos
\newcommand*{\alumnonombre}[1]{\def\studentname{#1}}
\newcommand*{\alumnoseccion}[1]{\def\studentsecction{#1}}
\newcommand*{\fecha}[1]{\def\labdate{#1}}

\alumnonombre{}
\alumnoseccion{}
\fecha{}

%grades
\newcommand*{\puntajetest}[1]
{
\def\test{4 & 3 & 2 & 1, 0 }
\ifthenelse{\equal{#1}{0}}{\def\test{4 & 3 & 2 & 1, \hl{0}}}{}
\ifthenelse{\equal{#1}{1}}{\def\test{4 & 3 & 2 & \hl{1}, 0}}{}
\ifthenelse{\equal{#1}{2}}{\def\test{4 & 3 & \hl{2} & 1, 0}}{}
\ifthenelse{\equal{#1}{3}}{\def\test{4 & \hl{3} & 2 & 1, 0}}{}
\ifthenelse{\equal{#1}{4}}{\def\test{\hl{4} & 3 & 2 & 1, 0}}{}
}

\newcommand*{\puntajecriterioi}[1]
{
\def\puntajei{4 & 3 & 2 & 1, 0 }
\ifthenelse{\equal{#1}{0}}{\def\puntajei{4 & 3 & 2 & 1, \hl{0}}}{}
\ifthenelse{\equal{#1}{1}}{\def\puntajei{4 & 3 & 2 & \hl{1}, 0}}{}
\ifthenelse{\equal{#1}{2}}{\def\puntajei{4 & 3 & \hl{2} & 1, 0}}{}
\ifthenelse{\equal{#1}{3}}{\def\puntajei{4 & \hl{3} & 2 & 1, 0}}{}
\ifthenelse{\equal{#1}{4}}{\def\puntajei{\hl{4} & 3 & 2 & 1, 0}}{}
}

\newcommand*{\puntajecriterioii}[1]
{
\def\puntajeii{4 & 3 & 2 & 1, 0 }
\ifthenelse{\equal{#1}{0}}{\def\puntajeii{4 & 3 & 2 & 1, \hl{0}}}{}
\ifthenelse{\equal{#1}{1}}{\def\puntajeii{4 & 3 & 2 & \hl{1}, 0}}{}
\ifthenelse{\equal{#1}{2}}{\def\puntajeii{4 & 3 & \hl{2} & 1, 0}}{}
\ifthenelse{\equal{#1}{3}}{\def\puntajeii{4 & \hl{3} & 2 & 1, 0}}{}
\ifthenelse{\equal{#1}{4}}{\def\puntajeii{\hl{4} & 3 & 2 & 1, 0}}{}
}

\newcommand*{\puntajecriterioiii}[1]
{
\def\puntajeiii{4 & 3 & 2 & 1, 0 }
\ifthenelse{\equal{#1}{0}}{\def\puntajeiii{4 & 3 & 2 & 1, \hl{0}}}{}
\ifthenelse{\equal{#1}{1}}{\def\puntajeiii{4 & 3 & 2 & \hl{1}, 0}}{}
\ifthenelse{\equal{#1}{2}}{\def\puntajeiii{4 & 3 & \hl{2} & 1, 0}}{}
\ifthenelse{\equal{#1}{3}}{\def\puntajeiii{4 & \hl{3} & 2 & 1, 0}}{}
\ifthenelse{\equal{#1}{4}}{\def\puntajeiii{\hl{4} & 3 & 2 & 1, 0}}{}
}

\newcommand*{\puntajeinforme}[1]
{
\def\informe{2 & 1 & 0 & 0 }
\ifthenelse{\equal{#1}{0}}{\def\informe{2 & 1 & 0 & \hl{0}}}{}
\ifthenelse{\equal{#1}{1}}{\def\informe{2 & \hl{1} & 0 & 0}}{}
\ifthenelse{\equal{#1}{2}}{\def\informe{\hl{2} & 1 & 0 & 0}}{}
}
\newcommand*{\puntajeactitud}[1]
{
\def\actitud{2 & 1 & 0 & 0 }
\ifthenelse{\equal{#1}{0}}{\def\actitud{2 & 1 & 0 & \hl{0}}}{}
\ifthenelse{\equal{#1}{1}}{\def\actitud{2 & \hl{1} & 0 & 0}}{}
\ifthenelse{\equal{#1}{2}}{\def\actitud{\hl{2} & 1 & 0 & 0}}{}
}

\newcommand*{\comentarios}[1]{\def\comments{#1}}
\newcommand*{\puntajetotal}[1]{\def\total{#1}}

\puntajetest{}
\puntajecriterioi{}
\puntajecriterioii{}
\puntajecriterioiii{}
\puntajeactitud{}
\puntajeinforme{}
\puntajetotal{}
\comentarios{}

%Rubrica criterios
\newcommand*{\competencia}[1]{\def\competencias{#1}}
\newcommand*{\criterioi}[1]{\def\criterioiname{#1}}
\newcommand*{\criterioii}[1]{\def\criterioiiname{#1}}
\newcommand*{\criterioiii}[1]{\def\criterioiiiname{#1}}

\criterioi{}
\criterioii{}
\criterioiii{}

\newcolumntype{C}{m{0.16\linewidth}}
\def\logo{\includegraphics[width=0.1\textwidth]{logo-utec.png}}

\newcommand{\makerubrica}{
\newpage
\begin{table}[!ht]
    \begin{tabular}{|m{0.22\textwidth} |*{3}{m{0.1\textwidth}|} m{0.2\textwidth}|m{0.15\textwidth}|} 
        \hline 
         \logo               & \multicolumn{5}{c|}{\bfseries R\'ubrica de Evaluaci\'on} \\ \hline 
        \textbf{Competencia} & \multicolumn{5}{p{0.8\textwidth}|}{\competencias}  \\ \hline
        
        \textbf{Curso}       & \multicolumn{3}{l|}{\cursoname{}} 
                             & Ciclo & 4 \\ \hline
        
        \textbf{Actividad}   &\multicolumn{3}{p{0.35\textwidth}|}{\title} 
                             & Sesi\'on & \laboratorynumber \\ \hline
      
        \textbf{Nombre y apellido del Alumno} &\multicolumn{3}{c|}{\studentname{}} 
                                              & Periodo 
                                              & \term \\ \hline
        
        \textbf{Secci\'on:} & \studentsecction{}  & Fecha & \labdate{} 
                                                  & Jefe de pr\'acticas  
                                                  & \jefedepracticasname  \\ \hline

    \end{tabular}
                                                
    \begin{center}
     \begin{tabular}{|*{4}{m{0.144\textwidth}|>{\bfseries}m{0.072\textwidth}|}}
      
      \multicolumn{8}{l}{\textbf{Documentos de evaluaci\'on}} \\ \hline
      Laboratorio &\textbf{X} & Taller & &Proyecto &  &Otros& \\ \hline
     \end{tabular}
    \end{center}

    \begin{center}
     \begin{tabular}{|*{2}{m{0.27\textwidth}|} *{4}{m{0.1\textwidth}|}}
         \hline
         
         \multicolumn{2}{|m{0.5\textwidth}|}{\bfseries CRITERIOS DE EVALUACI\'ON} & \textbf{\small Excelente} 
                                                                                  &\textbf{\small Bueno} 
                                                                                  & \textbf{\small Requiere Mejora} 
                                                                                  & {\bfseries \small No \par aceptable} \\ \hline
         
         \multicolumn{6}{|l|}{\textbf{TEST DE ENTRADA}} \\ \hline
         
         \multicolumn{2}{|m{0.54\textwidth}|}{Grado de conocimiento del tema del laboratorio y del procedimiento} & \test{}  \\ \hline
         
         \multicolumn{6}{|l|}{\textbf{SESI\'ON DE LABORATORIO}} \\ \hline
         
         \multicolumn{2}{|m{0.54\textwidth}|}{\criterioiname}    & \puntajei{} \\ \hline
         \multicolumn{2}{|m{0.54\textwidth}|}{\criterioiiname}   & \puntajeii{} \\ \hline
         \multicolumn{2}{|m{0.54\textwidth}|}{\criterioiiiname}  & \puntajeiii{} \\ \hline
 
         \multicolumn{6}{|l|}{\textbf{INFORME DE TRABAJO DE EQUIPO}} \\ \hline
 
         \multicolumn{2}{|m{0.54\textwidth}|}{Presenta el informe puntualemnte de acuerdo a lo establecido} 
                                                                                  & \informe{}\\ \hline
 
         \multicolumn{6}{|l|}{\textbf{ACTITUDES}} \\ \hline
         \multicolumn{2}{|m{0.54\textwidth}|}{
                                Participa con entusiamos y seguridad (Puntualidad, intervenciones, \'orden, limpieza y redacci\'on.) 
                                Culimna el laboratorio en el tiempo previsto.} & \actitud{}  \\ \hline
 
         \multicolumn{2}{|l|}{\textbf{PUNTAJE TOTAL}} & \multicolumn{4}{c|}{\total{}} \\ \hline
 
         Comentario al alumno & \multicolumn{5}{m{0.74\textwidth}|}{\comments{}} \\ \hline
      \end{tabular}
     \end{center}

     \small
     \begin{center}
     \begin{tabular}{|m{0.12\textwidth}|m{0.90\textwidth}|}
         \multicolumn{2}{l}{\textbf{Descripci\'on de la evaluaci\'on}}  \\ \hline
         
         \textbf{Excelente}       & Completo entendimiento y realizaci\'on de la actividad, cumpliendo todos los requerimientos \\ \hline
         \textbf{Bueno}           & Entiende y realiza la actividad cumpliendo la mayoria de los requerimientos \\ \hline
         \textbf{Requiere Mejora} & Bajo entendimiento de la actividad cumpliendo pocos requerimientos \\ \hline
         {\bfseries No \par aceptable}    & No demuestra entendimiento de la actividad \\ \hline
        
    \end{tabular}
     \end{center}
 \end{table}

}
