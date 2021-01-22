from SinRumbo import DestruyeNave
#import SinRumbo
class Automata:

    def __init__(self):
        Q=['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11']
        Sigma=[1,2,3,4,5]
        self.s='q1'
        self.F=['q10']
        self.recorridoFinal=[]
        self.delta={('q1',1):'q2',
               ('q2',2):'q4',
               ('q3',1):'q2',
               ('q4',1):'q2',
               ('q4',3):'q6',
               ('q6',1):'q7',
               ('q6',2):'q8',
               ('q8',1):'q9',
               ('q9',1):'q10'}
    

    def salirPlaneta(self):
        opc=0
        print()
        opc=int(input("Te encuentras en el inicio. Presiona 1 para enceder nave y salir del planeta: "))
        self.recorridoFinal.append(opc)        
        try:
            if(opc==1):
                #transicion=self.delta[(estado,opc)]
                #print(transicion)
                #self.recorridoFinal.append(opc)
                #self.fijarRumbo(transicion)
                self.fijarRumbo(self.recorridoFinal)
        except ValueError:
            print("Cuidado, debes ingresar un número entero.")
            
    def fijarRumbo(self,recorridoFinal):
        recorrido=recorridoFinal
        #print(recorrido)
        print()
        print("Ahora están fuera del planeta tierra, debes escoger un rumbo:")
        print("1)Ir a Marte")
        print("2)Ir a Kepler-22B")
        print("3)Ir al centro de la galaxia")
        print("4)Regresar a la tierra")
        print("5)Ir a la próxima estrella mas cercana")

        opc=0
        while True:
            opc=int(input("Ingresa una opción (Fijar Rumbo): "))
            recorrido.append(opc)
            #print(recorrido)
            self.recorridoFinal=recorrido
            try:
                if(opc==2):
                    #transicion=self.delta[(estado,opc)]
                    self.cruzarCinturon()
                    break
                if(opc==1 or opc==3 or opc==4 or opc==5):
                    obj.destruirNave(self.recorridoFinal)
                    #transicion=self.delta[(estado,opc)]
                    break
            except ValueError:
                print("Cuidado, debes ingresar un número entero.")
            break

    def cruzarCinturon(self):
        print()
        print("Estás a punto de cruzar el cinturón de asteroides entre Marte y Júpiter: ")
        print("Selecciona una opción:")
        print("1)Regresar y tomar otra ruta.")
        print("2)Abortar Misión.")
        print("3)Adentrarse hasta llegar a Júpiter.")
        opc=0
        while True:
            opc=int(input("Ingrese una opción (Cruzar Cinturón): "))
            self.recorridoFinal.append(opc)
            try:
                if(opc==1):
                    self.fijarRumbo(self.recorridoFinal)
                    break
                if(opc==2):
                    print("Has dedicido abortar la misión.")
                    self.verRecorrido(self.recorridoFinal)
                    break
                if(opc==3):
                    #transicion=self.delta[(estado,opc)]
                    #self.irAJupiter(transicion)
                    self.irAJupiter()
                    break
            except ValueError:
                print("Cuidado, debes ingresar un número entero.")
            #print(self.recorridoFinal)    
            break
    
    def irAJupiter(self):
        opc=0
        print()
        print("Muy bien, ahora estás cerca de Júpiter, para seguir adelante tienes 2 caminos posibles: ")
        print("1) Usar la gravedad de Júpiter para impulsarse y ahorrar combustible.")
        print("2) Seguir adelante y descubrir que pasa.")
    
        while True:
            opc=int(input("Ingrese una opción: "))
            self.recorridoFinal.append(opc)
            try:
                if(opc==1):
                    self.salirDelSistemaSolar()
                    #transicion=self.delta[(estado,opc)]
                    #self.recorridoFinal.append(opc)
                    break
                else:
                    if(opc==2):
                        #transicion=self.delta[(estado,opc)]
                        #print("final")
                        self.descubrirVida()
                        break
                        #self.recorridoFinal.append(opc)     
            except ValueError:
                pass
            #print(self.recorridoFinal)
            break
    def salirDelSistemaSolar(self):
        opc=0
        print()
        print("Muy bien te estás acercando a la nube de Ort, eso signfica que estás saliendo del sistema "
        "solar y que vas muy bien.")
        print()
        print("1) Seguir adelante.")
        while True:
           opc=int(input("Favor de avanzar: "))
           self.recorridoFinal.append(opc)
           try:
               if(opc==1):
                   obj.salirHoyoNegro(self.recorridoFinal)
                   break
               else:
                   print("Favor de ingresar la opción correcta.")
                   break
           except ValueError:
               print("Cuidado, debes ingresar un número entero: ")
               pass
           break

    
    def descubrirVida(self):
        opc=0

        print("Te has encontrado con un satélite que la AEM mandó hace 10 años. Ya no puede enviar" 
                "información, pero aún la sigue recibiendo. El satélite tiene información en la que"
                "Titán, una de las lunas de Júpiter alberga vida. Tú y los ingeniero Airam y Alessandra"
                "están ante un descubrimientos sin precendentes. Han descubierto vida en el Sistema Solar.")
        print()
        print("1)Ver información del satélite.")
        
        while True:
            opc=int(input("Favor de avanzar: "))
            self.recorridoFinal.append(opc)
            try:
                if(opc==1):
                    self.leyendoInformacion()
                    break
                else:
                    print("Favor de ingresar la opción correcta.")
                    break
            except ValueError:
                print("Cuidado, debes ingresar un número entero: ")
                pass
            break
    
    def leyendoInformacion(self):
        opc=0
        print("LA información del satélite indica que la vida en Titán si existe, desde microorganismos,"
        "hasta diferentes tipos de especies desconocidas que se encuentran en las profundidades del los"
        "océanos congelados de dicho satélite natural. Al parece el rumbo de tu travesía tomará un camino"
        "diferente.")
        print()
        print("1)Bajar a Titán y buscar vida.")
        print("2)Anunciarlo a la AEM y seguir ruta a Kepler-22B")
        while True:
            opc=int(input("Ingrese alguna opción: "))
            self.recorridoFinal.append(opc)
            try:
                if(opc==1):
                    self.bajarATitan(self.recorridoFinal)
                    break
                else:
                    if(opc==2):
                        print("La AEM ya está enviando varias tripulaciones a Titán para plantar una base. "
                        "Gracias por tu apoyo. Continúa con tu larga travesía.")
                        print(self.recorridoFinal)
                        break
                    else:
                        print("Favor de ingresar la opción correcta.")
                        break
            except ValueError:
                print("Cuidado, debes ingresar un número.")
                pass
            break
    
    def bajarATitan(self, recorridoFinal):
        print("De ahora en adelante la misión se dedicará a la investigación en Titán. 3 naves tripuladas"
        "van a hacia ustedes en este momento con la teconología necesaria para plantar una base ahí. En 2 "
        "meses, una tripulación mas grande partirá hacia Kepler-22B." )
        self.verRecorrido(self.recorridoFinal)
    
    def verRecorrido(self, recorridoFinal):
        self.recorridoFinal=recorridoFinal
        w=self.recorridoFinal

        estado=self.s
        for i in w:
            estado=self.transicion(estado,i)
        if estado in (self.F):
            print(w," La nave espacial siguió la ruta adecuada.")
        else:
            print(w," La nave espacial tuvo problemas de ubicación.")
            
    def transicion(self,estado, sigma):
        STATUS=True
        if (estado, sigma) not in (self.delta.keys()):
            STATUS=False
            return STATUS
        estado_siguiente=self.delta[(estado, sigma)]
        return estado_siguiente

obj=DestruyeNave()
