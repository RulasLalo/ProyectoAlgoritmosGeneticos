import tkinter as tk
from tkinter import ttk
from tkinter import *
from Recorrido import Automata

class Aplicacion:
    def __init__(self):
        auto=Automata()
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"Año 2065; el ser humano aprendió a cuidar sus recursos, los autos son {1:.02%} eléctricos, "
        "la deforestación se detuvo por completo hace 30 años; y el ser humano al fin pudo aprender a cuidar su hogar."
        "Pero ahora lo que está en la mira de todos es un contacto extraterrestre el cual se hizo hace 10 años con ondas de radio."
        "En México, la Agencia Espacial Mexicana (AEM) fue quien hizo el contacto con esta civilización "
        "un poco mas desarrollada que la raza humana, específicamente los ingenieros Airam Canales y "
        "Alessandra Cruz, las cabezas principales de esta organización."
        "Estos ingenieros se están encargando de un desarrollo en el cual varios astronautas serán "
        "mandados fuera de nuestro sistema solar, específicamente al planeta Kepler-22B. "
        "El descubrimiento de este mundo fue anunciado el día 5 de diciembre del 2011."
        "Tu objetivo es ayudara los ingenieros Airam y Alessandra a llegar a Kepler-22B en esta aventura interestelar.")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        auto.escogerNave()

app=Aplicacion()