# ALGORITMO DIJKSTRA PROYECTO ERDD 
# Dev by Ernesto Crespo => Follow @techbyer en Instagram 

"""En este codigo trabajamos el algoritmo Dijkstra en Python y su Implementacion
   como ejemplo de una empresa de Delivery/Servicio de envios.
   Para este caso los nodos del grafo serian las casas de nuestros clientes, el grafo seria el mapa 
   y las aristas serian los caminos o calles por donde pasamos para hacer la entrega al cliente"""

class Graph(): 
    # Constructor para inicializar los valores
    def __init__(self, nodes): #Definimos funcion _init_ que tiene parametros self y nodes, self permite al usuario especificar 
                               #y acceder a los atributos y metodos de una instancia de una clase y nodes es la cantidad de nodos 9
        #Inicializacion del array de distancia
        self.distArray = [0 for i in range(nodes)]  #Creacion del Array DistArray aqui almacenaremos la distancia entre los nodos visitados
        #Inicializacion de nodos visitados
        self.vistSet = [0 for i in range(nodes)]   #Creacion del Array VisitSet donde almacenaremos el nodo de menor distancia de los nodos visitados
        #Inicializacion del numero de nodos
        self.V = nodes      # Self.V Sera igual al numero de nodos
        # Inicializacion del Valor Infinito
        self.INF = 1000000       #Valor Infinito igual a 1000000  
        #Inicializacion de la Matriz de Adyacencia la cual tomamos como entrada en nuestro programa
        self.graph = [[0 for column in range(nodes)]  #Cantidad de Columnas igual a los nodos
                    for row in range(nodes)]          #Cantidad de Filas igual a los nodos
                    
   
    def dijkstra(self, srcNode): #Funcion Dijkstra donde haremos el algoritmo, parametros self y srcNode que es el Nodo Inicial C o 0
        for i in range(self.V):  #For que va de 0 a 9 donde inicializamos un Array
          #Inicializamos el distArray al valor infinito
          #Esto lo hacemos para que cuando compare siempre tome el valor mas pequeño en la primera comparacion
          self.distArray[i] = self.INF
          #Inicializamos el valor del visitSet a Falso para que cuando este sea visitado tome el valor de True
          self.vistSet[i] = False
        #Inicializamos la distancia del srcNoce (Nodo C) a 0 
        self.distArray[srcNode] = 0
        for i in range(self.V): #For de 0 a 9 (Cantidad de nodos=self.V)
            # Toma el nodo de menor distancia desde
            # el conjunto(array) de nodos no visitados todavia
            # U sera siempre igual al srcNode (C) en la primera iteracion
            u = self.minDistance(self.distArray, self.vistSet) #U toma el valor devuelto por la funcion minDistance
  
            # Coloca el nodo de menor distancia en 
            # el conjunto de nodos visitados (visitSet)
            self.vistSet[u] = True    #Asigna el valor de True al nodo cuando ya ha sido visitado en el Array VisitSet
  
            # Actualizamos distArray[v] solo si no esta en VisitSet, aqui hay una arista desde 
            # u a v, y el peso total del camino desde srcNode a v a traves de u es 
            # mas pequeño que el valor actual de distArray[v] por lo que se toma este nuevo valor
            for v in range(self.V): 
                if self.graph[u][v] > 0 and self.vistSet[v] == False and self.distArray[v] > self.distArray[u] + self.graph[u][v]: 
                        self.distArray[v] = self.distArray[u] + self.graph[u][v] 
  
        self.printSolution(self.distArray)  #Llamamos al metodo printSolution y nos llevamos el distArray como parametro

    # Funcion para encontrar el nodo con valor de distancia minima
    #  desde el conjunto de nodos que no esta incluido en el camino mas corto 
    def minDistance(self, distArray, vistSet): 
        # Inicializando la distancia minima para el siguiente nodo
        min = self.INF
        # Search not nearest node not in the  // Buscamos el nodo mas cercano en los 
        # unvisited nodes                     // nodos no visitados VisitSet
        for v in range(self.V): 
            if distArray[v] < min and vistSet[v] == False: #Si distArray[v]<min y visitSet[v]==False Quiere decir que el nodo no esta visitado
                min = distArray[v]  #min toma el valor de distArray[v]      
                min_index = v       #min_index toma el valor de v
        return min_index            #Retornamos el valor de min_index

    def printSolution(self, distArray):    #Funcion para mostrar la solucion en pantalla 
        print ("Node   Distance from 0 o Nodo")     
        # For para impresion
        for i in range(self.V): 
            #Convertimos la variable i en una string
            i=str(i)
            #Aqui reemplazamos la string i por sus valores numericos, reemplazados respectivamente con su correspondiente Nodo (Letra)
            print(" ",i.replace('0','C').replace('1','G').replace('2','D').replace('3','E').replace('4','A').replace('5','F').replace('6','H').replace('7','K').replace('8','B'),"\t\t\t",distArray[int(i)])
            
#Display our table // Esta es nuestra matriz de adyacencia que tomamos como entrada para el proceso del Dijkstra
ourGraph = Graph(9)  #Aqui el valor 9 representa la cantidad de Nodos de nuestro grafo
               # Matriz 9x9 de los Nodos de nuestro grafo
               #   C   G   D   E   A   F   H   K   B 
ourGraph.graph = [[0,  8,  9,  4,  0,  0,  0,  0,  0], #0 C
                  [8,  0, 16,  0,  7,  2,  0,  0,  0], #1 G
                  [9, 16,  0,  6, 20,  0,  0,  0,  0], #2 D
                  [4,  0,  6,  0,  7,  0,  0,  8,  0], #3 E 
                  [0,  7, 20,  7,  0,  0,  2,  0,  4], #4 A
                  [0,  2,  0,  0,  0,  0,  0,  0, 10], #5 F
                  [0,  0,  0,  0,  2,  0,  0,  6, 17], #6 H 
                  [0,  0,  0,  8,  0,  0,  6,  0,  1], #7 K
                  [0,  0,  0,  0,  4, 10, 17,  1,  0], #8 B
                  ];        
                  #Aqui entramos al dijkstra y nos llevamos el srcNode en este caso 0 representado por la C    
ourGraph.dijkstra(0)