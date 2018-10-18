from numpy import random
def crear_edificio():
    for a in range(H):
        vacio = []
        for a in range(W):
            vacio.append(0)
        tablero.append(vacio)
def estetica_tablero():
    for a in range(len(tablero)):
        for b in range(len(tablero[a])):
            if a == 0 or b == 0:
                tablero[a][b] = "*"
            else:
                tablero[a][b] = " "
        tablero[a][-1] = "*"
    for a in range(len(tablero[-1])):
        tablero[-1][a] = "*"
    q = random.randint(-1,1)
    h = random.randint(1, len(tablero)-1)
    tablero[h][q] = "|"
def mostrar_tablero():
    for a in range(len(tablero)):
        for b in range(len(tablero[a])-1):
            print(tablero[a][b], end="")
        print(tablero[a][b+1])
def generar_personajes():
    #cantidad_guardia = int(input("Cantidad máxima de guardias: "))
    cantidad_guardia = int(gwh[0][0]) #toma el primer elemento de edificio.txt, el cual debería ser el valor de G
    G = random.randint(1, cantidad_guardia)
    for a in range(G):
        z = 1
        while z != 0:
            x = random.randint(1,H-1)
            y = random.randint(1,W-1)
            if tablero[x][y] == "*":
                continue
            else:
                tablero[x][y] = "G"
                posicion_guardias.append([x,y])
                z = 0
    z = 1
    while z != 0:
        x = random.randint(1,H-1)
        y = random.randint(1,W-1)
        if tablero[x][y] == "G" or tablero[x][y] == "*":
            continue
        else:
            tablero[x][y] = "L"
            posicion_ladron.append([x,y])
            z = 0
def mover_guardias():
    for a in range(len(posicion_guardias)):
        move = random.randint(0,4)
        x = posicion_guardias[a][0]
        y = posicion_guardias[a][1]
        if NOSE[move] == "N":
            if tablero[x-1][y] == "*" or tablero[x-1][y] == "G" or tablero[x-1][y] == "|":
                continue
            elif tablero[x-1][y] == "L":
                print("Se acabaron tus días de robo")
                tablero[x-1][y] = "+"
                return False
            else:
                tablero[x][y] = " "
                posicion_guardias[a][0] = x-1
                tablero[x-1][y] = "G"
        elif NOSE[move] == "S":
            if tablero[x+1][y] == "*" or tablero[x+1][y] == "G" or tablero[x+1][y] == "|":
                continue
            elif tablero[x+1][y] == "L":
                print("Tras las rejas")
                tablero[x+1][y] = "+"
                return False
            else:
                tablero[x][y] = " "
                posicion_guardias[a][0] = x+1
                tablero[x+1][y] = "G"
        elif NOSE[move] == "E":
            if tablero[x][y-1] == "*" or tablero[x][y-1] == "G" or tablero[x][y-1] == "|":
                continue
            elif tablero[x][y-1] == "L":
                print("Ladron muere")
                tablero[x][y-1] = "+"
                return False
            else:
                tablero[x][y] = " "
                posicion_guardias[a][1] = y-1
                tablero[x][y-1] = "G"
        elif NOSE[move] == "O":
            if tablero[x][y+1] == "*" or tablero[x][y+1] == "G" or tablero[x][y+1] == "|":
                continue
            elif tablero[x][y+1] == "L":
                print("Ladron atrapado")
                tablero[x][y+1] = "+"
                return False
            else:
                tablero[x][y] = " "
                posicion_guardias[a][1] = y+1
                tablero[x][y+1] = "G"
def mover_ladron():
    z = 1
    x = posicion_ladron[0][0]
    y = posicion_ladron[0][1]
    while z != 0:
        ladron = input("  N" + "\n"+ "E   O" + "\n"+ "  S" + "\n" + "-->")
        if ladron == "N":
            if tablero[x-1][y] == "*" or tablero[x-1][y] == "G":
                print("error")
            else:
                tablero[x][y] = " "
                posicion_ladron[0][0] = x-1
                tablero[x-1][y] = "L"
                z = 0
        elif ladron == "S":
            if tablero[x+1][y] == "*" or tablero[x+1][y] == "G":
                print("error")
            else:
                tablero[x][y] = " "
                posicion_ladron[0][0] = x+1
                tablero[x+1][y] = "L"
                z = 0
        elif ladron == "E":
            if tablero[x][y-1] == "*" or tablero[x][y-1] == "G":
                print("error")
            elif tablero[x][y-1] == "|":
                tablero[x][y] = " "
                tablero[x][y-1] = "_"
                return False
            else:
                tablero[x][y] = " "
                posicion_ladron[0][1] = y-1
                tablero[x][y-1] = "L"
                z = 0
        elif ladron == "O":
            if tablero[x][y+1] == "*" or tablero[x][y+1] == "G":
                print("error")
            elif tablero[x][y+1] == "|":
                tablero[x][y] = " "
                tablero[x][y+1] = "_"
                return False
            else:
                tablero[x][y] = " "
                posicion_ladron[0][1] = y+1
                tablero[x][y+1] = "L"
                z = 0
def escribir_tablero():
    file = open("final.txt", "w")
    for a in range(len(tablero)):
        for b in range(len(tablero[a])-1):
            file.write(str(tablero[a][b]))
        file.write(str(tablero[a][b+1]) + "\n")
    file.close()
def abrir_edificio():
    archivo = open("edificio.txt")
    linea = archivo.readline().split()
    gwh.append(linea) #suponiendo que los valores de G, W y h estan dentro de edificio.txt expresados como "10 6 8"
    archivo.close()
NOSE = ["N", "S", "E", "O"]
gwh = []
posicion_ladron = []
posicion_guardias = []
tablero = []
abrir_edificio()

flag = True
while flag:
    #W = int(input("With: "))
    W = int(gwh[0][1]) #toma el segundo valor de edificio.txt suponiendo que es el valor de width
    if 5 <= W:
        #H = int(input("Height: "))
        H = int(gwh[0][2]) #toma el tercer valor de edificio.txt suponiendo que es el valor de height
        if 3 <= H:
            crear_edificio()
            estetica_tablero()
            generar_personajes()
            mostrar_tablero()
            flag = False
        else:
            print("error")
    else:
        print("error")

f = 1
while f != 0:
    if mover_ladron() == False:
        mostrar_tablero()
        print("ganaste")
        escribir_tablero()
        break
    if mover_guardias() == False:
        mostrar_tablero()
        print("perdiste")
        escribir_tablero()
        break
    mostrar_tablero()
input()
