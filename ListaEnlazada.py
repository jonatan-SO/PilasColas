class node:
    def __init__(self, data=None, data2=None, next=None):
        self.data = data
        self.next = next
        self.data2 = data2


# Creamos la clase linked_list
class linked_list:
    __lista1 = []
    __lista2 = []
    def __init__(self):
        self.head = None

    # Método para agregar elementos en el frente de la linked list
    def add_at_front(self, data,data2):
        self.__lista1 = data
        self.__lista1 = set(self.__lista1)
        self.__lista2 = data2
        self.__lista2 = set(self.__lista2)
        print(self.__lista2,self.__lista1)

        self.head = node(data=data, data2=data2, next=self.head)

    def InterseccionConjuntos(self):
        # la funcion & muestra los elementos repetidos de los
        # conjuntos y los alamacena
        self.__interseccion = self.__lista1 & self.__lista2
        print(f'la interseccion es  {self.__interseccion}')

    def UnionConjuntos(self):
        # como los elemtos no estan repetidos se pueeden unir lla los dos conjuntos
        self.__union = self.__lista1 | self.__lista2
        print(f'la union de los conjuntos es {self.__union}')

    def DiferenciaConjuntos(self):
        # esta  parte '-' permite sacar los elementos que sean diferentes
        self.__diferencia = self.__lista1 - self.__lista2
        print(f'la direfencia de los conjuntos es {self.__diferencia}')

    def InclusionConjuntos(self):
        if self.__lista1 <= self.__lista2:
            return print(f'el conjunto numero 1 si tiene inclusion en el conjunto 2 {self.__lista1}')
        else:
            return print(f'el conjunto numero 1 no tiene inclusion en el conjunto 2 {self.__lista1}')



    # Método para imprimir la lista de nodos
    def print_list(self):
        node = self.head
        while node != None:
            #print(node.data, end=" => ")
            print(node.data)
            node = node.next



s = linked_list() # Instancia de la clase
lista = [1,2,3,5,6]
lista2 = [4,5,6,7,2]
s.add_at_front(lista,lista2) # Agregamos un elemento al frente del nodo
s.InterseccionConjuntos()
s.UnionConjuntos()
s.DiferenciaConjuntos()
s.InclusionConjuntos()


s.print_list() # Imprimimos la lista de nodos