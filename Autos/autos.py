file = open("precios_modelos.txt")

lista_autos = []
autos = []
auto_seleccionado = []
precio_modelo = []
intervalos = []

for linea in file:
    a = linea.split()
    if a == []:
        continue
    elif not a[0] in autos:
        autos.append(a[0])
    lista_autos.extend(a)
autos.sort()
file.close()

for i in range(len(autos)):
    print("(" + str(i+1) + ")" + autos[i])
x = int(input("seleccione un modelo: "))
for j in range(len(lista_autos)):
    if autos[x-1] == lista_autos[j]:
        precio_modelo.append(int(lista_autos[j+1]))
precio_modelo.sort()
f = float(precio_modelo[0])
g = float(precio_modelo[-1])
h = (g - f)/5
for t in range(6):
    intervalo = int(f + h*(t))
    intervalos.append(intervalo)
int1 = 0
int2 = 0
int3 = 0
int4 = 0
int5 = 0
for r in range(len(precio_modelo)):
    if intervalos[0] <= int(precio_modelo[r]) and int(precio_modelo[r]) <= intervalos[1]:
        int1 += 1
    elif intervalos[1] < int(precio_modelo[r]) and int(precio_modelo[r]) <= intervalos[2]:
        int2 += 1
    elif intervalos[2] < int(precio_modelo[r]) and int(precio_modelo[r]) <= intervalos[3]:
        int3 += 1
    elif intervalos[3] < int(precio_modelo[r]) and int(precio_modelo[r]) <= intervalos[4]:
        int4 += 1
    elif intervalos[4] < int(precio_modelo[r]) and int(precio_modelo[r]) <= intervalos[5]:
        int5 += 1
print()
print(str(autos[x-1]) + "\n")
print(str(intervalos[0]) + " " + "-" + " " + str(intervalos[1]) + " " + "|" + " " + "X"*int1)
print(str(intervalos[1]) + " " + "-" + " " + str(intervalos[2]) + " " + "|" + " " + "X"*int2)
print(str(intervalos[2]) + " " + "-" + " " + str(intervalos[3]) + " " + "|" + " " + "X"*int3)
print(str(intervalos[3]) + " " + "-" + " " + str(intervalos[4]) + " " + "|" + " " + "X"*int4)
print(str(intervalos[4]) + " " + "-" + " " + str(intervalos[5]) + " " + "|" + " " + "X"*int5)
salida = open("histograma.txt", "w")
salida.write(str(autos[x-1]) + "\n")
salida.write(str(intervalos[0]) + " " + "-" + " " + str(intervalos[1]) + " " + "|" + " " + "X"*int1 + "\n")
salida.write(str(intervalos[1]) + " " + "-" + " " + str(intervalos[2]) + " " + "|" + " " + "X"*int2 + "\n")
salida.write(str(intervalos[2]) + " " + "-" + " " + str(intervalos[3]) + " " + "|" + " " + "X"*int3 + "\n")
salida.write(str(intervalos[3]) + " " + "-" + " " + str(intervalos[4]) + " " + "|" + " " + "X"*int4 + "\n")
salida.write(str(intervalos[4]) + " " + "-" + " " + str(intervalos[5]) + " " + "|" + " " + "X"*int5 + "\n")
salida.close()
input()
