#!/bin/bash

echo "\def\nombre{$1}" > param.tex
echo "\newcounter{nota1} \setcounter{nota1}{$2}" >> param.tex
echo "\newcounter{nota2} \setcounter{nota2}{$3}" >> param.tex
echo "\newcounter{nota3} \setcounter{nota3}{$4}" >> param.tex
echo "\newcounter{nota4} \setcounter{nota4}{$5}" >> param.tex
echo "\newcounter{resultado} \setcounter{resultado}{$6}" >> param.tex

pdflatex -jobname="$1" "\input{param.tex} \input{juan.tex}"

rm *.aux
rm *.log


echo $resultado
