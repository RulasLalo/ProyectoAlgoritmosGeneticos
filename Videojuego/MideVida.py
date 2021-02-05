import math
import random
from random import sample
import statistics as stats

class Mide_Vida:
    
    def __init__(self):
        self.individuos=0
        self.rango=8
        self.lista_rango=[]
        self.aleatorio=[]
        self.individuo=[]
        self.vida=0
        self.principal()

    def principal(self):
        for i in range(self.rango):
            self.lista_rango.append(i)
        
        #print(self.lista_rango)
        self.aleatorio=sample(range(1,len(self.lista_rango)+1),self.rango)
        #print(self.aleatorio)
        self.funcionFitness()
        #self.escogerIndividuo()
        #self.funcionFitness()

    '''def escogerIndividuo(self):
        
        print("Escoja la nave espacial de su agrado: ")
        for i in self.aleatorio:
            print("Nave ",i)

        nave=0

        nave=int(input("Selecciona la nave: "))

        for i in self.aleatorio:
            if nave==i:
                print("Seleccionaste la nave ",nave)'''
        
        #self.funcionFitness()

    def funcionFitness(self):
        opc=0
        print("Clases de Naves: ") #Funciones fitness disponibles
        print()
        print("1. Conquistadoras") #f(x)=x^2
        print("2. Defensoras") #f(x)=ABS |(x-5)/(2+sen(x)|
        print("3. Valerosas") #f(x)=sen(x)
        print()
        opc=int(input("Escoge una clase y veamos que tan resistente es tu nave: "))

        if opc == 1:
            self.fitness(self.aleatorio,opc)
        if opc == 2:
            self.fitness(self.aleatorio,opc)
        if opc == 3:
            self.fitness(self.aleatorio,opc)
    
    def fitness(self,aleatorio, opc):
        listaBinaria=[]
        tablaAleatorios=[]
        rangoTabla=0
        logaritmo=0
        tablaAleatorio=[]

        logaritmo=int(math.log(self.rango,2)) #We get the logarithm of the range
        #print(logaritmo)
        rangoTabla=(logaritmo+1)*self.rango #Add 1 because it counts from base 0
        tablaAleatorio=sample(range(0,rangoTabla),rangoTabla)
        #print(tablaAleatorio)
        alelo=[]
        #We get the random number between 0 and 1 which are the alleles
        for i in range(len(tablaAleatorio)):
            if tablaAleatorio[i]<=10:
                valor="{0:.2f}".format(tablaAleatorio[i]/10)
                alelo.append(float(valor))
            else:
                valor="{0:.2f}".format(10/tablaAleatorio[i])
                alelo.append(float(valor))
        print()

        #print(alelo)
        lista1=[]
        lista2=[]
        #Here we've created various groups of alleles
        if logaritmo+1>=4:
            for i in range(len(alelo)):
                lista1.append(alelo[i])
                if len(lista1)%(logaritmo+1)==0:
                   #print(lista1)
                   lista2.append(lista1)
                   lista1=[] 
            print()
        
        lista3=[]
        lista4=[]
        cadena=''
        #Here we put 0 if the value is less than 0.5 and 1 if the value is greater than or equal than 0.5
        for i in range(len(lista2)):
            #print(lista2[i])
            for j in lista2[i]:
                if j<0.5:
                    cadena+=str(0)
                if j>=0.5:
                    cadena+=str(1)
            lista4.append(cadena)
            lista3.append(int(cadena,2))
            cadena=''
            if i==self.individuos-1:
               break

        if opc==1:
            self.funcionFitness1(lista3, lista4)
        if opc==2:
            self.funcionFitness2(lista3,lista4)
        if opc==3:
            self.funcionFitness3(lista3,lista4)

    def funcionFitness1(self, lista3, lista4):
        aptitud=0
        suma=0
        probabilidad=0
        print("No.     ","Población Inicial     ","Valor x     ","Aptitud     ","Probabilidad     ")
        for i in range(len(lista3)):
            aptitud=pow(lista3[i],2)
            suma+=aptitud
        for i in range(len(lista3)):
            aptitud=pow(lista3[i],2)
            probabilidad=aptitud/suma
            print(i+1,"          ",lista4[i],"             ", lista3[i],"           ","{0:.2f}".format(aptitud),"            ", "{0:.2f}".format(probabilidad))
            self.individuo.append(lista3[i])

        self.escogerIndividuos(self.individuo)

    def funcionFitness2(self, lista3, lista4):
        aptitud=0
        suma=0
        probabilidad=0
        print("No.     ","Población Inicial     ","Valor x     ","Aptitud     ","Probabilidad     ")
        for i in range(len(lista3)):
            aptitud=abs((lista3[i]-5)/(2+math.sin(lista3[i])))
            suma+=aptitud
        for i in range(len(lista3)):
            aptitud=abs((lista3[i]-5)/(2+math.sin(lista3[i])))
            probabilidad=aptitud/suma
            print(i+1,"          ",lista4[i],"             ", lista3[i],"           ","{0:.2f}".format(aptitud),"            ", "{0:.2f}".format(probabilidad))
            self.individuo.append(lista3[i])

        self.escogerIndividuos(self.individuo)

    def funcionFitness3(self, lista3, lista4):
        aptitud=0
        suma=0
        probabilidad=0
        individuo=[]
        print("No.     ","Población Inicial     ","Valor x     ","Aptitud     ","Probabilidad     ")
        for i in range(len(lista3)):
            aptitud=math.sin(lista3[i])
            suma+=aptitud
        for i in range(len(lista3)):
            aptitud=math.sin(lista3[i])
            probabilidad=aptitud/suma
            print(i+1,"          ",lista4[i],"             ", lista3[i],"           ","{0:.2f}".format(aptitud),"            ", "{0:.2f}".format(probabilidad))
            self.individuo.append(lista3[i])
        self.escogerIndividuos(self.individuo)

    def escogerIndividuos(self, individuo):

        print("Escoja la nave espacial de su agrado: ")
        for i in individuo:
            print("Nave ",i)

        nave=0

        nave=int(input("Selecciona la nave: "))

        for i in individuo:
            if nave==i:
                print("Seleccionaste la nave ",nave)

        mayor=max(individuo)
        menor=min(individuo)
        media=stats.mean(individuo)
        print(mayor," ",menor, " ", media)
        self.vida=0
        if nave == mayor:
            self.vida=3
        if nave<mayor or nave==media:
            self.vida=2
        if nave<media or nave==menor:
            self.vida=1
        #print(self.vida)
       

    def devolverVida(self):
        return self.vida

#obj=Mide_Vida()