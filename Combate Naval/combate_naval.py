def crear_tablero(d):
    for a in range(d+1):
        vacio = []
        for b in range(d+1):
            vacio.append(0)
        tablero.append(vacio)
def mostrar_tablero(tablero):
    for c in range(len(tablero)):
        for d in range(len(tablero[c])):
            if c == 0 and d == 0:
                tablero[c][d] = " "
            elif c == 0:
                tablero[c][d] = (str(d) + " ")
            elif d == 0:
                tablero[c][d] = c
            elif tablero[c][d] == 0:
                tablero[c][d] = "  "
            elif tablero[c][d] == 1:
                tablero[c][d] = "X "
    for x in range(len(tablero)):
        z = int(len(tablero[x]))
        for y in range(z-1):
            print(tablero[x][y],end=' ')
        print(tablero[x][y+1])
def ingresar_barco(tipo, orientacion, i, j, tablero):
    leng = 0
    for f in range(len(tipos)):
        for g in range(len(tipos[f])):
            if tipos[f][g] == tipo:
                leng = tipos[f][g+1]
    if orientacion == "h":
        for e in range(leng): #horizontal
            tablero[i][j+e] = 1
    if orientacion == "v":
        for e in range(leng): #vertical
            tablero[i+e][j] = 1
def cabe_barco(tipo, orientacion, i, j, tablero):
    leng = 0
    for f in range(len(tipos)):
        for g in range(len(tipos[f])):
            if tipos[f][g] == tipo:
                leng = tipos[f][g+1]
    if orientacion == "h":
        if j+leng <= len(tablero[i]):
            return True
        else:
            return False
    if orientacion == "v":
        if j+leng <= len(tablero):
            return True
        else:
            return False
def colisiona(tipo, orientacion, i, j, tablero):
    leng = 0
    for f in range(len(tipos)):
        for g in range(len(tipos[f])):
            if tipos[f][g] == tipo:
                leng = tipos[f][g+1]
    if orientacion == "h":
        for e in range(leng): #horizontal
            if tablero[i][j+e] == 1:
                return True
    if orientacion == "v":
        for e in range(leng): #vertical
            if tablero[i+e][j] == 1:
                return True
tablero = []
tipos = [["portaaviones" ,5],["acorazado" ,4],["crucero" ,3],["submarino" ,3],["destructor" ,2]]
d = int(input("Ingrese el tamaño del tablero:"))
n = int(input("Ingrese cantidad de barcos:"))
t = crear_tablero(d)
k = 1
while k <= n:
    flag = True
    while flag:
        print("----------------------")
        print("Datos barco Nro " + str(k))
        print("----------------------")
        tipo = input("Ingrese tipo del barco:")
        orientacion = input("Ingrese orientación [h/v]:")
        i = int(input("Ingrese fila:"))
        j = int(input("Ingrese columna:"))
        if cabe_barco(tipo, orientacion, i, j, tablero) and not colisiona(tipo, orientacion, i, j, tablero):
            t = ingresar_barco(tipo, orientacion, i, j, tablero)
            flag = False
            mostrar_tablero(tablero)
            print()
        else:
            print("No se ha podido ingresar el barco")
    k += 1
input()
