import tkinter as tk
from tkinter import ttk
from tkinter import *
from Recorrido import Automata

class Aplicacion:
    def __init__(self):
        auto=Automata()
        self.planeta=auto.salirPlaneta
        self.ventana=tk.Tk()
        self.ventana.title("Autómata nave espacial")
        self.ventana.geometry("950x600")#Establecer tamaño de inicio a la ventana raíz
        self.ventana.resizable(0,0) #Impide que se cambie el tamaño
        self.ventana.config(bg="red")#Fondo a la ventana
        self.interior=ttk.Frame(self.ventana, width=900, height=350)#Crear objeto de clase Frame
        self.interior.pack(pady=100)
        #self.interior.config(bg="blue")
        self.texto=tk.StringVar(value=("Año 2065; el ser humano aprendió a cuidar sus recursos, los autos son 100% eléctricos, "
        "la deforestación se detuvo por completo hace 30 años; y el ser humano al fin pudo aprender a cuidar su hogar."
        "Pero ahora lo que está en la mira de todos es un contacto extraterrestre el cual se hizo hace 10 años con ondas de radio."
        "En México, la Agencia Espacial Mexicana (AEM) fue quien hizo el contacto con esta civilización "
        "un poco mas desarrollada que la raza humana, específicamente los ingenieros Airam Canales y "
        "Alessandra Cruz, las cabezas principales de esta organización."
        "Estos ingenieros se están encargando de un desarrollo en el cual varios astronautas serán "
        "mandados fuera de nuestro sistema solar, específicamente al planeta Kepler-22B. "
        "El descubrimiento de este mundo fue anunciado el día 5 de diciembre del 2011."
        "Tu objetivo es ayudara los ingenieros Airam y Alessandra a llegar a Kepler-22B en esta aventura interestelar."))
        self.etiqueta=ttk.Label(self.interior,textvariable=self.texto, wraplength=870)
        self.etiqueta.place(width=900, height=350)
        self.etiqueta.config(background="pink")
        self.boton=ttk.Button(self.interior, text="Comenzar la aventura", command=(self.planeta))
        self.etiqueta.configure(anchor="center", font=("calibri",14))
        self.boton.place(x=300,y=300, width=200, height=30)
        self.ventana.mainloop()
    

app=Aplicacion()