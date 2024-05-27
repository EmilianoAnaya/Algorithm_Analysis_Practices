import os
import time
#---------------------------------------MERGESORT--------------------------------------------------------------------------#

def unir_listas(lista_derecha,lista_izquierda):
    rango_permitido = set(range(65, 91)) | set(range(97, 123)) | set(range(128, 160)) | set(range(192,500))
    lista_resultado = []
    letra = 0
    while len(lista_derecha) > 0 and len(lista_izquierda) > 0:
        palabra_derecha = lista_derecha[0]
        palabra_izquierda = lista_izquierda[0]
        palabra_derecha_limpia = ''.join(letra for letra in palabra_derecha if ord(letra) in rango_permitido)
        palabra_izquierda_limpia = ''.join(letra for letra in palabra_izquierda if ord(letra) in rango_permitido)
        lista_derecha.pop(0), lista_derecha.insert(0,palabra_derecha_limpia)
        lista_izquierda.pop(0), lista_izquierda.insert(0,palabra_izquierda_limpia)
        lista_izquierda[0] = lista_izquierda[0].lower()
        lista_derecha[0] = lista_derecha[0].lower()
        max_derecha = len(lista_derecha[0])
        max_izquierda = len(lista_izquierda[0])
        if letra == max_derecha:
            lista_resultado.append(lista_derecha[0])
            lista_derecha.pop(0)
            letra = 0
        elif letra == max_izquierda:
            lista_resultado.append(lista_izquierda[0])
            lista_izquierda.pop(0)
            letra = 0
        else:
            if ord(lista_derecha[0][letra]) != ord(lista_izquierda[0][letra]):
                if ord(lista_derecha[0][letra]) > ord(lista_izquierda[0][letra]):
                    lista_resultado.append(lista_izquierda[0])
                    lista_izquierda.pop(0)
                    letra = 0
                else:
                    lista_resultado.append(lista_derecha[0])
                    lista_derecha.pop(0)
                    letra = 0
            else:
                letra+=1
    while len(lista_izquierda) > 0:
        lista_resultado.append(lista_izquierda[0])
        lista_izquierda.pop(0)
    
    while len(lista_derecha) > 0:
        lista_resultado.append(lista_derecha[0])
        lista_derecha.pop(0)
    
    return lista_resultado

def merge_sort(lista):
    if len(lista) == 1:
        return lista
    mitad = len(lista) // 2
    lista_derecha = lista[:mitad]
    lista_izquierda = lista[mitad:]

    lista_derecha_ordenada = merge_sort(lista_derecha)
    lista_izquierda_ordenada = merge_sort(lista_izquierda)

    return unir_listas(lista_derecha_ordenada,lista_izquierda_ordenada)

palabras_unicas = []
archivo2 = open("archivoNuevo.txt", mode='w', encoding='UTF-8' )
archivo = open("Example.txt", mode='r', encoding='UTF-8')
lista = archivo.read().split()
lista_ordenada = merge_sort(lista)

for palabra in lista_ordenada:
    if palabra not in palabras_unicas:
        palabras_unicas.append(palabra)

palabras_parrafo = 0
for i in range(len(palabras_unicas)):
    palabras_parrafo = palabras_parrafo + 1
    archivo2.write(palabras_unicas[i])
    archivo2.write(' ')
    if palabras_parrafo == 12:
        archivo2.write('\n')
        palabras_parrafo = 0

archivo.close()
archivo2.close()

#----------------------------------- BUSQUEDA BINARIA ------------------------------------------------------------#

def busqueda_binaria(lista, palabra):
    inicio = 0
    final = len(lista)-1
    while (inicio <= final):
        mitad = (inicio + final) // 2
        valido = palabra == lista[mitad]
        if valido:
            return mitad
        if palabra > lista[mitad]:
            inicio = mitad + 1
        else:
            final = mitad - 1
    return -1


print("ARCHIVO CREADO - BUSQUEDA BINARIA")
while True:
    archivo2 = open("archivoNuevo.txt", mode='r', encoding='UTF-8' )
    palabra = input("Palabra a buscar: ")
    palabra = palabra.lower()
    renglon = 1
    palabra_posicion = ""
    start_time = time.time()
    for fila in archivo2:
        lista = fila.split()
        palabra_posicion = busqueda_binaria(lista, palabra)
        if palabra_posicion == -1:
            renglon = renglon + 1
            palabra_posicion = ""
            time.sleep(0.001)
        else:
            print("Palabra encontrada en la posición:",palabra_posicion+1,"Fila:",renglon)
            break
    final_time = time.time() - start_time
    print("Tiempo de busqueda:",final_time)
    if palabra_posicion == "":
        print("Palabra no encontrada en el texto.")
    de_nuevo = input("\nBuscar otra palabra? (S/N): ")
    if de_nuevo.lower() == "n":
        break
    else:
        os.system('cls')

archivo2.close()