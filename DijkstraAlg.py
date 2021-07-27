# ALGORITMO DIJKSTRA PROYECTO ERDD 
# Dev by Ernesto Crespo => Follow @techbyer en Instagram 
#Hacer Intro Manana Martes // Cambiar variables // Nombres etc Add comments
class Graph(): 
    # A constructor to iniltialize the values  // Constructor para inicializar los valores
    def __init__(self, nodes):        #Definimos funcion _init_ que tiene parametros self () y nodes () Donde self hace referencia a tomar los atributos del Constructor
        #distance array initialization // Inicializacion del array de distancia
        self.distArray = [0 for i in range(nodes)]   #Creacion del Array DistArray con cantidad maxima igual al num de nodos
        #visited nodes initialization   // Inicializacion de nodos visitados
        self.vistSet = [0 for i in range(nodes)]   #Creacion del Array VisitSet con cantidad maxima igual al num de nodos
        #initializing the number of nodes  // Inicializacion del numero de nodos
        self.V = nodes                 # Self . V Sera igual al numero de nodos
        #initializing the infinity value  // Inicializacion del Valor Infinito
        self.INF = 1000000                 #Valor Infinito igual a 1000000  
        #initializing the graph matrix     #Inicializacion de la Matriz de Adyacencia
        self.graph = [[0 for column in range(nodes)]  #Cantidad de Columnas igual a los nodos
                    for row in range(nodes)]          #Cantidad de Filas igual a los nodos
                    
   
    def dijkstra(self, srcNode):
        for i in range(self.V):
          #initialise the distances to infinity first
          self.distArray[i] = self.INF
          #set the visited nodes set to false for each node
          self.vistSet[i] = False
        #initialise the first distance to 0
        self.distArray[srcNode] = 0
        for i in range(self.V): 
            # Pick the minimum distance node from  
            # the set of nodes not yet processed.  
            # u is always equal to srcNode in first iteration 
            u = self.minDistance(self.distArray, self.vistSet) 
  
            # Put the minimum distance node in the  
            # visited nodes set
            self.vistSet[u] = True
  
            # Update dist[v] only if is not in vistSet, there is an edge from 
            # u to v, and total weight of path from src to  v through u is 
            # smaller than current value of dist[v]
            for v in range(self.V): 
                if self.graph[u][v] > 0 and self.vistSet[v] == False and self.distArray[v] > self.distArray[u] + self.graph[u][v]: 
                        self.distArray[v] = self.distArray[u] + self.graph[u][v] 
  
        self.printSolution(self.distArray)

    #A utility function to find the node with minimum distance value, from 
    # the set of nodes not yet included in shortest path tree 
    def minDistance(self, distArray, vistSet): 
  
        # Initilaize minimum distance for next node
        min = self.INF
  
        # Search not nearest node not in the  
        # unvisited nodes
        for v in range(self.V): 
            if distArray[v] < min and vistSet[v] == False: 
                min = distArray[v] 
                min_index = v 
  
        return min_index

    def printSolution(self, distArray): 
        print ("Node   Distance from 0 o Nodo")
        diccionario = { '0':'C', '1':'G', '2':'D', '3':'E', '4':'A', '5':'F', '6':'H', '7':'K', '8':'B'}
        for i in range(self.V): 
            i=str(i)
            print(" ",i.replace('0','C').replace('1','G').replace('2','D').replace('3','E').replace('4','A').replace('5','F').replace('6','H').replace('7','K').replace('8','B'),"\t\t\t",distArray[int(i)])
           # print (" ", i, "\t\t\t", distArray[i])
#Display our table
ourGraph = Graph(9) 
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
ourGraph.dijkstra(0)