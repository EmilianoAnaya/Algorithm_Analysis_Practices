def busqueda(lista_raices,nodo):
    if lista_raices[nodo] == -1:
        return nodo
    else:
        return busqueda(lista_raices,lista_raices[nodo])

def particion(lista_aristas,inicio,final):
    pivote = lista_aristas[final][2]
    i = inicio - 1
    for j in range(inicio,final):
        if lista_aristas[j][2] <= pivote:
            i = i+1
            (lista_aristas[i],lista_aristas[j]) = (lista_aristas[j],lista_aristas[i])
    (lista_aristas[i+1],lista_aristas[final]) = (lista_aristas[final],lista_aristas[i+1])
    return i+1

def quicksort(lista_aristas, inicio, final):
    if inicio < final:
        pivote = particion(lista_aristas,inicio,final)
        quicksort(lista_aristas,inicio,pivote-1)
        quicksort(lista_aristas,pivote+1,final)

grafo = [
            #Matriz 1
            #A B C D E F G
		    [0,3,4,5,0,0,0], #A
            [3,0,0,5,2,0,0], #B
            [4,0,0,4,0,1,0], #C
            [5,5,4,0,4,5,4], #D
            [0,2,0,4,0,0,7], #E
            [0,0,1,5,0,0,3], #F
            [0,0,0,4,7,3,0]  #G

            #Matriz 2
            #[0,2,4,0,0], #A
            #[2,0,3,0,0], #B
            #[4,3,0,2,3], #C
            #[0,0,2,0,4], #D
            #[0,0,3,4,0]  #E
		]
costo_grafo = 0
lista_aristas = []
MST = []
for fila in range(len(grafo)):
    for columna in range(len(grafo)):
        if fila == columna:
            break
        elif grafo[fila][columna] == 0:
            continue
        else:
            lista_aristas.append([fila,columna,grafo[fila][columna]])
            costo_grafo = costo_grafo + grafo[fila][columna]
						#VERTICE DE ORIGEN, VERTICE DE FIN, PESO DE ARISTA

print("Matriz de Adyacencia del Grafo")
for fila in grafo:
    print(fila)
print("Costo de Grafo:",costo_grafo)

lazos_maximos = len(grafo)-1
tamanio_lista = len(lista_aristas)
quicksort(lista_aristas, 0, tamanio_lista-1)
lista_raices = []
for i in range(len(grafo)):
    lista_raices.append(-1)

for arista in lista_aristas:
    if len(MST) == lazos_maximos:
        break
    origen = busqueda(lista_raices,arista[0])
    destino = busqueda(lista_raices,arista[1])
    if origen != destino:
        MST.append(arista)
        lista_raices[origen] = destino

grafo_MST = []
for fila in range(len(grafo)):
    grafo_MST.append([])
    for columna in range(len(grafo)):
        grafo_MST[fila].append(0)

costo_arista = 0
for arista in MST:
    grafo_MST[arista[0]][arista[1]] = arista[2]
    costo_arista = costo_arista + arista[2]

for fila in range(len(grafo_MST)):
    for columna in range(len(grafo_MST)):
        grafo_MST[fila][columna] = grafo_MST[columna][fila]

print("\nMatriz de Adyacencia de MST")
for fila in grafo_MST:
    print(fila)

print("Costo de MST:",costo_arista)