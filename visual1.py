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

def setposi(t, pos):
    t.ht()
    t.setpos(pos[0], pos[1])
    t.st()

def getGrd():
    return [0, 10]

def plotar(x, y, legenda = "linha1", xt = "x", yt ="y", titulo = "") :
    
    plt.plot(x, y, label = legenda) 
    
    plt.xlabel(xt) 
     
    plt.ylabel(yt) 
    
    plt.title(titulo) 
      
    plt.legend() 
    
def plotLinha(x, y, legenda = "linha1") :
    
    plt.plot(x, y, label = legenda) 
      
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
        
class Tartaruga:
    
    def __init__(self, t, v):
        self.vetor = v
        self.tartaruga = t


#MAIN
def main() :
    rd.seed()
    numAlunos = int(input("Numero de alunos(recomendado menos de 60):"))
    numIteracoes = int(input("Numero de interçoes totais(recomendado mais de 500):"))
    pctIteracoes = int(input("Porcentagem de interçoes com professores(0 a 100):"))
    limIteracoes = int(input("Limite de interçoes com professores:"))

    professor =  [rd.randint(-100, 100), rd.randint(-100, 100)]
    tartProf = trl.Turtle()
    tartProf.radians()
    tartProf.color('yellow')
    tartProf.penup()
    tartProf.right(np.arctan(professor[0]/professor[1]))
    tartProf.setpos([rd.randint(-256, 256), rd.randint(-256, 256)])
    
    alunos = []
    
    s = trl.Screen()
    s.screensize(650, 550, 'black')
    s.delay(0)

    for i in range(numAlunos):
        alunoVet =  np.array([rd.randint(-100, 100), rd.randint(-100, 100)])
        alunoVet = alunoVet/np.linalg.norm(alunoVet)
        
        tart = trl.Turtle()
        tart.radians()
        tart.color('white')
        tart.penup()
        tart.setpos([rd.randint(-256, 256), rd.randint(-256, 256)])
        tart.right(np.arctan(alunoVet[0]/alunoVet[1]))
        
        alunos.append(Tartaruga(tart, alunoVet))
        
        
    medAngulos= []
    medAlPro = []
        
    soman = np.math.factorial(numAlunos)/(2*np.math.factorial(numAlunos - 2))

    k = 0
    j = 0
        

    for i in range(numIteracoes):
        
        for j in  range(numAlunos):
            
            if(alunos[j].tartaruga.xcor() < -s.screensize()[0]/2 or alunos[j].tartaruga.ycor() < -s.screensize()[1]/2):
                if(alunos[j].tartaruga.xcor() < - s.screensize()[0]/2 and alunos[j].tartaruga.ycor() < - s.screensize()[1]/2):
                    setposi(alunos[j].tartaruga, [alunos[j].tartaruga.xcor() + s.screensize()[0], alunos[j].tartaruga.ycor() + s.screensize()[1]])
                elif(alunos[j].tartaruga.ycor() < -s.screensize()[1]/2):
                    setposi(alunos[j].tartaruga, [alunos[j].tartaruga.xcor(), alunos[j].tartaruga.ycor() + s.screensize()[1]])
                else:
                    setposi(alunos[j].tartaruga, [alunos[j].tartaruga.xcor() + s.screensize()[0], alunos[j].tartaruga.ycor()])
            
            if(alunos[j].tartaruga.xcor() > s.screensize()[0]/2 or alunos[j].tartaruga.ycor() > s.screensize()[1]/2):
                if(alunos[j].tartaruga.xcor() > s.screensize()[0]/2 and alunos[j].tartaruga.ycor() > s.screensize()[1]/2):
                    setposi(alunos[j].tartaruga, [alunos[j].tartaruga.xcor() - s.screensize()[0], alunos[j].tartaruga.ycor() - s.screensize()[1]])
                elif(alunos[j].tartaruga.ycor() > s.screensize()[1]/2):
                    setposi(alunos[j].tartaruga, [alunos[j].tartaruga.xcor(), alunos[j].tartaruga.ycor() - s.screensize()[1]])
                else:
                    setposi(alunos[j].tartaruga, [alunos[j].tartaruga.xcor() - s.screensize()[0], alunos[j].tartaruga.ycor()])
            alunos[j].tartaruga.fd(10)
            
        if(tartProf.xcor() < -s.screensize()[0]/2 or tartProf.ycor() < -s.screensize()[1]/2):
            if(tartProf.xcor() < - s.screensize()[0]/2 and tartProf.ycor() < - s.screensize()[1]/2):
                setposi(tartProf, [tartProf.xcor() + s.screensize()[0], tartProf.ycor() + s.screensize()[1]])
            elif(tartProf.ycor() < -s.screensize()[1]/2):
                setposi(tartProf, [tartProf.xcor(), tartProf.ycor() + s.screensize()[1]])
            else:
                setposi(tartProf, [tartProf.xcor() + s.screensize()[0], tartProf.ycor()])
        
        if(tartProf.xcor() > s.screensize()[0]/2 or tartProf.ycor() > s.screensize()[1]/2):
            if(tartProf.xcor() > s.screensize()[0]/2 and tartProf.ycor() > s.screensize()[1]/2):
                setposi(tartProf, [tartProf.xcor() - s.screensize()[0], tartProf.ycor() - s.screensize()[1]])
            elif(tartProf.ycor() > s.screensize()[1]/2):
                setposi(tartProf, [tartProf.xcor(), tartProf.ycor() - s.screensize()[1]])
            else:
                setposi(tartProf, [tartProf.xcor() - s.screensize()[0], tartProf.ycor()])
        tartProf.fd(10)
        
        
        prf = rd.randint(-1,99)
        
        if(prf < pctIteracoes and limIteracoes > 0):
            k = rd.randint(0, numAlunos - 1)
            alunos[k].tartaruga.color('pink')
            res = iteracao(professor, alunos[k].vetor)
            alunos[k].vetor = res
            alunos[k].tartaruga.right(alunos[k].tartaruga.heading() + np.arctan(res[0]/res[1]))
            limIteracoes -= 1
            
        else:
            k = rd.randint(0, numAlunos - 1)
            j = rd.randint(0, numAlunos - 1)
            
            res = iteracao(alunos[j].vetor, alunos[k].vetor)
            
            alunos[j].vetor, alunos[k].vetor = res, res

            alunos[k].tartaruga.right(alunos[k].tartaruga.heading() + np.arctan(res[0]/res[1]))
            alunos[j].tartaruga.right(alunos[j].tartaruga.heading() + np.arctan(res[0]/res[1]))

        soma = 0.0

        for i0 in range(numAlunos):
            for i1 in range(i0 + 1, numAlunos):
                soma = soma + abs(anguloEntrVet(alunos[i0].vetor, alunos[i1].vetor))
        medAngulos.append(soma/soman)
        
        soma = 0.0
        for i0 in range(numAlunos):
            soma = soma + abs(anguloEntrVet(alunos[i0].vetor, professor))
            
        medAlPro.append(soma/numAlunos)
        
    plotar(range(numIteracoes), medAngulos, 'diferença entre alunos', 'iteraçoes', 'diferença(rad)')
    plotLinha(range(numIteracoes), medAlPro, 'diferença entre alunos e professor')
    plt.show()

main()
