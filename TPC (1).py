
f = open("Transito Marzo 2024.csv", "r", encoding="utf-8")
f.readline()
contador = 0
for _ in range(0,260000):
    linea = f.readline() #GUARDAS LA LINEAS EN UNA VARIABLE, DESPUES PODES HACER LO QUE QUIERAS
    array = linea.split(";") #CONVERTIS LA VARIABLE EN UNA ARRAY Y ACLARAS CON QUE SIMBOLO ESTA SEPARADA CADA COLUMNA
    hora = array[1]
    categoria = array[2]
    sentido = array[5]
    if hora == "0" or hora == "1" or hora == "2" or hora == "3" or hora == "4" or hora == "5" or hora == "6" or hora == "7" or hora == "8":
        if categoria =="Pesados 3 Ejes":
            if sentido == "Provincia":
                contador = contador + 1
print (contador)   
def ejericio6 ():
    f = open("Transito Abril 2024.csv", "r", encoding="utf-8")
    f.readline()
    provincia = 0
    centro = 0
    motos = 0
    promedio = ""
    for _ in range(0,260000):
        linea = f.readline()
        array = linea.split(";")
        categoria = array[2]
        sentido = array[5]
        if categoria =="Moto":
            motos = motos +1
            if sentido == "Provincia":
                provincia = provincia + 1
            if sentido == "Centro":
                centro = centro + 1
    provincia = provincia/motos
    centro = centro/motos
    print(centro)
    print(provincia)
    if provincia > centro:
        promedio="Provincia"
    elif provincia < centro:
        promedio="Centro"
    else:
        promedio="Iguales"
    return promedio
