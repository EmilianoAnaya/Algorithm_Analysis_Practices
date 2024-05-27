def sort_nodos(nodos):
    return nodos[0]

def sort_frecuencia(frecuencia):
    return frecuencia[1]

def huffman(nodos):
    if len(nodos) > 1:
        nodos.sort(key=sort_nodos)
        dato_derecho = nodos.pop(0)
        dato_izquierdo = nodos.pop(0)
        frecuencia_suma = dato_derecho[0] + dato_izquierdo[0]
        nuevo_nodo = [frecuencia_suma,"null",dato_izquierdo,dato_derecho]
        nodos.append(nuevo_nodo)
        return huffman(nodos)
    else:
        return nodos

def codificacion(nodo,codigo):
    if nodo[3] != "null":
        codificacion(nodo[3],codigo=codigo+"1")

    if nodo[2] != "null":
        codificacion(nodo[2],codigo=codigo+"0")

    if (nodo[2] == "null" and nodo[3] == "null"):
        letra_codigo.append([nodo[1],codigo])

archivo = open("Example.txt", mode="r",encoding="UTF-8")
archivo_comprimido = open("ArchivoComprimido.bin", mode="wb")
archivo_descomprimido = open("ArchivoDescomprimido.txt", mode="w", encoding="UTF-8")
palabras_archivo = archivo.readlines()

frecuencia = []
for palabra in palabras_archivo:
    for letra in palabra:
        flag_aparicion = 0
        for dato in frecuencia:
            if dato[0] == letra:
                dato[1] = dato[1] + 1
                flag_aparicion = 1
                break
        if flag_aparicion == 0:
            frecuencia.append([letra,1])

frecuencia.sort(key=sort_frecuencia)
nodos = []
for dato in frecuencia:
    nodos.append([dato[1],dato[0],"null","null"])
            #Frecuencia, Letra, dato_izq, dato_der
arbol = huffman(nodos)

letra_codigo = []
arbol_huffman = arbol[0]
codificacion(arbol_huffman,"")
#COMPRIMIR
palabra_codificada = ""
for palabra in palabras_archivo:
    for letra in palabra:
        for dato in letra_codigo:
            if letra == dato[0]:
                palabra_codificada = palabra_codificada + dato[1]
                break

datosBytes = bytes(int(palabra_codificada[i:i+8], 2) for i in range(0, len(palabra_codificada), 8))
archivo_comprimido.write(datosBytes)
archivo_comprimido.close()

archivo_comprimido = open("ArchivoComprimido.bin", mode="rb")

#DESCOMPRIMIR
byte_temp = ''.join(format(byte,'08b') for byte in archivo_comprimido.read())
palabra_decodificada = ""
codigo = ""
for bit in byte_temp:
    codigo = codigo + bit
    for dato in letra_codigo:
        if codigo == dato[1]:
            palabra_decodificada = palabra_decodificada + dato[0]
            codigo = ""
            break

archivo_descomprimido.write(palabra_decodificada)

archivo.close()
archivo_comprimido.close()
archivo_descomprimido.close()