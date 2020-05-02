#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020 João Paulo Paiva Lima <joao.lima1@estudante.ufla.br>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import numpy as np
import random as rd
import matplotlib.pyplot as plt 
import turtle as trl

def getposi(t):
    return [-t.xcor(), -t.ycor()] 

def getGrd():
    return [0, 10]

def plotar(x, y, legenda = "linha1", xt = "x", yt ="y", titulo = "") :
    
    plt.plot(x, y, label = legenda) 
    
    plt.xlabel(xt) 
     
    plt.ylabel(yt) 
    
    plt.title(titulo) 
      
    plt.legend() 

def anguloEntrVet(a, b):
    c = (a[0]*b[0] + a[1]*b[1])/(np.linalg.norm(a) * np.linalg.norm(b))
    if(c  < -1):
        c = -1
    elif(c > 1):
        c = 1
    return np.arccos(c)

def iteracao(aluno0, aluno1):
        vRes = aluno0 + aluno1
        vRes = vRes / np.linalg.norm(vRes)
        vRes[1] = vRes[1]
        return vRes


#MAIN
def main() :
    rd.seed()
    numAlunos = 50#int(input("Numero de alunos:"))
    numIteracoes = 1000#int(input("Numero de interçoes totais:"))
    pctIteracoes = 30#int(input("Porcentagem de interçoes com professores:"))

    professor =  [20, 13]

    alunos = []

    for i in range(numAlunos):
        alunoVet =  np.array([rd.randint(-100, 100), rd.randint(-100, 100)])
        alunoVet = alunoVet/np.linalg.norm(alunoVet)
        alunos.append(alunoVet)
        
    medAngulos= []
        
    soman = np.math.factorial(numAlunos)/(2*np.math.factorial(numAlunos - 2))


    for i in range(numIteracoes):
        
        prf = rd.randint(-1,99)
        if( prf < pctIteracoes):
            k = rd.randint(0, numAlunos - 1)
            res = iteracao(professor, alunos[k])
            alunos[k] = res
            
        else:
            k = rd.randint(0, numAlunos - 1)
            j = rd.randint(0, numAlunos - 1)
            res = iteracao(alunos[j], alunos[k])
            
            alunos[j], alunos[k]= res, res

        soma = 0.0

        for i0 in range(numAlunos):
            for i1 in range(i0 + 1, numAlunos):
                soma = soma + anguloEntrVet(alunos[i0], alunos[i1])
        medAngulos.append(soma/soman)
    plotar(range(numIteracoes), medAngulos)
    plt.show()

main()
