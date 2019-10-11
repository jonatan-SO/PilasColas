class colaEstatica:
    __tamCola = int(0)
    __listaCola = []
    def __init__(self,tamCola):
        self.__tamCola = tamCola

    def Insertar(self,elemento):
        if self.Colallena():
            return False
        else:
            self.__listaCola.append(elemento)
            return True

    def quitar(self):
        if self.colaBasia():
            return False
        else:
            return self.__listaCola.pop(0)


    def colaBasia(self):
        if len(self.__listaCola) == 0:
            return True
        else:
            return False

    def Colallena(self):
        if self.__tamCola == len(self.__listaCola):
            return True
        else:
            return False

    def LimpiarCola(self):
        self.__listaCola.clear()

    def mostarFrente(self):
        return self.__listaCola[0]

    def MostrarTamCola(self):
        return len(self.__listaCola)



class ColaDinamica:
    __tamCola = int(0)
    __listaCola = []

    def Insertar(self, elemento):

            self.__listaCola.append(elemento)
            return True

    def quitar(self):
        if self.colaBasia():
            return False
        else:
            return self.__listaCola.pop(0)

    def colaBasia(self):
        if len(self.__listaCola) == 0:
            return True
        else:
            return False


