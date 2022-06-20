tablero = [['-', '-', '-'],
           ['-', '-', '-'],
           ['-', '-', '-']
           ]

tablero2 = [['-', '-', '-', '-'],

            ['-', '-', '-', '-'],

            ['-', '-', '-', '-'],

            ['-', '-', '-', '-']
            ]

ganador = None

###################################################################


def jugar():
    global ganador
    print("Empieza el juego!")
    global tab
    tam = int(input("¿tablero 3x3 o 4x4?\n"))
    global varmatriz
    if (tam == 3):
        varmatriz = tablero
        tab = True
        ver_tablero(tab)
        for i in range(9):
            print("Turno del jugador 1 - X")
            valor = "X"
            # empiezan a jugar - Jugador1
            jugada(valor)
            data = huboGanador()
            if ganador != "X":
                print("Turno del jugador 2 - O")
                valor = "O"
                jugada(valor)
                huboGanador()
                if ganador == "O":
                    print("Felidades!!! Jugador 2 GANA el juego\n ", data)
                    break

            elif ganador == "X":
                print("Felicidades!!! Jugador 1 GANA el juego\n ", data)
                break
            elif (tam == 4):
                print("Empataron del juego repitanlo euller les dice")
        ganador = None

    elif(tam == 4):

        varmatriz = tablero2

        tab = False

        ver_tablero(tab)

        for i in range(16):
            print("Turno del jugador 1 - X")
            valor = "X"
            # empiezan a jugar - Jugador1
            jugada(valor)
            data = huboGanador()
            if ganador != "X":
                print("Turno del jugador 2 - O")
                valor = "O"
                jugada(valor)
                huboGanador()
                if ganador == "O":
                    print("Felidades!!! Jugador 2 GANA el juego\n ", data)
                    break

            elif ganador == "X":
                print("Felicidades!!! Jugador 1 GANA el juego\n ", data)
                break
            elif (tam == 4):
                print("Empataron del juego repitanlo euller les dice")
        ganador = None

    else:

        print("solo valores : 3 o 4")


###################################################################

def huboGanador():
    global ganador
    gano = controlLinea()
    if gano != None:
        return gano
    gano = controlVertical()
    if gano != None:
        return gano
    gano = controlDiagonal()
    if gano != None:
        return gano

###################################################################


def controlLinea():
    global ganador
    global gano
    if (varmatriz[0][0] == varmatriz[0][1] == varmatriz[0][2] != "-" ) :
        gano = "gano horizontal"
        ganador = varmatriz[1][0]
        return gano
    elif (tablero2[0][1] == tablero2[0][2] == tablero2[0][3] != "-") :
        gano = "gano horizontal"
        ganador = tablero2[0][1]
        return gano
    elif (varmatriz[1][0] == varmatriz[1][1] == varmatriz[1][2] != "-" ) :
        gano = "gano horizontal"
        ganador = varmatriz[1][0]
        return gano
    elif (tablero2[1][1] == tablero2[1][2] == tablero2[1][3] != "-") :
        gano = "gano horizontal"
        ganador = tablero2[1][1]
        return gano
    elif (varmatriz[2][0] == varmatriz[2][1] == varmatriz[2][2] != "-" ) :
        gano = "gano horizontal"
        ganador = varmatriz[2][0]
        return gano
    elif (tablero2[2][1] == tablero2[2][2] == tablero2[2][3] != "-") :
        gano = "gano horizontal"
        ganador = tablero2[2][1]
        return gano
        

###################################################################


def controlVertical():
    global ganador
    if (varmatriz[0][0] == varmatriz[1][0] == varmatriz[2][0] != "-" ):
        gano = "gano vertical"
        ganador = varmatriz[0][0]
        return gano
    elif (tablero2[1][0] == tablero2[2][0] == tablero2[3][0] != "-"):
        gano = "gano vertical"
        ganador = tablero2[1][0]
        return gano
    elif (varmatriz[0][1] == varmatriz[1][1] == varmatriz[2][1] != "-" ) :
        gano = "gano vertical"
        ganador = varmatriz[0][1]
        return gano
    elif (tablero2[1][1] == tablero2[2][1] == tablero2[3][1] != "-"):
        gano = "gano vertical"
        ganador = tablero2[1][1]
        return gano
    elif (varmatriz[0][2] == varmatriz[1][2] == varmatriz[2][2] != "-" ) :
        gano = "gano vertical"
        ganador = varmatriz[0][2]
        return gano
    elif (tablero2[1][2] == tablero2[2][2] == tablero2[3][2] != "-"):
        gano = "gano vertical"
        ganador = tablero2[1][2]
        return gano
    elif (varmatriz[0][3] == varmatriz[1][3] == varmatriz[2][3] != "-" ):
        gano = "gano vertical"
        ganador = varmatriz[0][3]
        return gano
    elif (tablero2[1][3] == tablero2[2][3] == tablero2[3][3] != "-"):
        gano = "gano vertical"
        ganador = tablero2[1][3]
        return gano

###################################################################


def controlDiagonal():
    global ganador
    if (varmatriz[0][0] == varmatriz[1][1] == varmatriz[2][2] != "-" ) :
        gano = "gano diagonal"
        ganador = varmatriz[0][0]
        return gano
    elif (tablero2[1][0] == tablero2[2][1] == tablero2[3][2] != "-") :
        gano = "gano diagonal"
        ganador = tablero2[1][0]
        return gano
    elif (tablero2[0][1] == tablero2[1][2] == tablero2[2][3] != "-") :
        gano = "gano diagonal"
        ganador = tablero2[0][1]
        return gano
    elif (tablero2[1][1] == tablero2[2][2] == tablero2[3][3] != "-") :
        gano = "gano diagonal"
        ganador = tablero2[1][1]
        return gano
    elif (varmatriz[0][2] == varmatriz[1][1] == varmatriz[2][0] != "-" ) :
        gano = "gano diagonal"
        ganador = varmatriz[0][2]
        return gano
    elif (tablero2[0][3] == tablero2[1][2] == tablero2[2][1] != "-") :
        gano = "gano diagonal"
        ganador = tablero2[0][3]
        return gano
    elif (tablero2[1][3] == tablero2[2][2] == tablero2[3][2] != "-") :
        gano = "gano diagonal"
        ganador = tablero2[1][3]
        return gano
    elif (tablero2[1][2] == tablero2[2][1] == tablero2[3][0] != "-") :
        gano = "gano diagonal"
        ganador = tablero2[1][2]
        return gano
        
        
###################################################################


def jugada(valor):
    anoto = False

    while anoto == False:
        posicionF = int(input("Elige una posicion en fila: "))
        posicionC = int(input("Elige una posicion en columna: "))
        posicionF -= 1
        posicionC -= 1
        if varmatriz[posicionF] != "-":
            anoto = True
        else:
            print("Esa posicion ya esta ocupada")

    varmatriz[posicionF][posicionC] = valor

    ver_tablero(tab)

###################################################################


def ver_tablero(tab):

    if (tab):

        print("\n")
        print(tablero[0][0], " | ", tablero[0][1], " | ",  tablero[0][2])
        print(tablero[1][0], " | ", tablero[1][1], " | ",  tablero[1][2])
        print(tablero[2][0], " | ", tablero[2][1], " | ",  tablero[2][2])
        print("\n")

    else:

        print("\n")
        print(tablero2[0][0], " | ", tablero2[0][1], " | ",
              tablero2[0][2], " | ", tablero2[0][3])
        print(tablero2[1][0], " | ", tablero2[1][1], " | ",
              tablero2[1][2], " | ", tablero2[1][3])
        print(tablero2[2][0], " | ", tablero2[2][1], " | ",
              tablero2[2][2], " | ", tablero2[2][3])
        print(tablero2[3][0], " | ", tablero2[3][1], " | ",
              tablero2[3][2], " | ", tablero2[3][3])
        print("\n")


s = "SI"

###################################################################

while s == "SI":
    jugar()
    s = input("desea jugar de nuevo: ").upper()
    tablero = [['-', '-', '-'],
               ['-', '-', '-'],
               ['-', '-', '-']]
