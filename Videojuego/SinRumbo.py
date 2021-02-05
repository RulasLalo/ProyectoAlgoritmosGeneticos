
class DestruyeNave:
    def destruirNave(self,recorridoFinal, vida):
        from Recorrido import Automata
        nave=Automata()
        regreso=''
        while True:
            regreso=input(("Tu nave fue destruidas. Presiona S para regresar al punto anterior: ")).lower()
            vida_=nave.ajustarVida(vida)
            if(regreso=='s' and vida_==0):
                print("GAME OVER")
                nave.verRecorrido(recorridoFinal)
                break
            if(regreso=='s'):
                #print(recorridoFinal)
                nave.fijarRumbo(recorridoFinal, vida_)
                break
            else:
                print("Presiona S, por favor.")
                break
            break

    def salirHoyoNegro(self, recorridoFinal):
        from Recorrido import Automata
        nave=Automata()
        print("Desgraciadamente has caído en un pequeño agujero negro dentro de la nube de Ort. "
        "Salir de ahí es imposible. Estás condenado a la eternidad, ¡Oh bueno!, hasta que el oxígeno "
        "se acabe.")
        nave.verRecorrido(recorridoFinal)