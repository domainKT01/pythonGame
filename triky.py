tablero =[['-','-','-'],
        ['-','-','-'],
        ['-','-','-']
        ]

tablero2 =[['-','-','-','-'],
        ['-','-','-','-'],
        ['-','-','-','-'],
        ['-','-','-','-']
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
            valor="X"
            #empiezan a jugar - Jugador1
            jugada(valor)
            data = huboGanador(varmatriz)
            if ganador != "X":
                print("Turno del jugador 2 - O")
                valor="O"
                jugada(valor)
                huboGanador()
                if ganador == "O":
                    print("Felidades!!! Jugador 2 GANA el juego\n ",data)
                    break
           
            elif ganador=="X":
                print("Felicidades!!! Jugador 1 GANA el juego\n ",data)
                break
            elif (tam == 4):
                print("Empataron del juego repitanlo euller les dice")
        ganador = None
       
    elif(tam==4):
       
        varmatriz = tablero2

        tab = False
       
        ver_tablero(tab)
       
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
   
def controlLinea(matriz):
    global ganador
    global gano
    if (tablero[0][0]== tablero[0][1]==tablero[0][2] !="-" 
        or [0][1] ==  tablero[0][2] == tablero[0][3] ) :
        ganador = tablero[0][0]
        gano = "gano horizontal"
        return gano
    elif (tablero[1][0]== tablero[1][1]==tablero[1][2] !="-" 
        or [1][1] ==  tablero[1][2] == tablero[1][3] ) :
        ganador = tablero[1][0]
        gano = "gano horizontal"
        return gano
    elif (tablero[2][0]== tablero[2][1]==tablero[2][2] !="-" 
        or [2][0] == tablero2[0][1] == tablero2[1][1] == tablero2[2][2] ) :
        ganador = tablero[2][0]
        gano = "gano horizontal"
        return gano
       
###################################################################
       
def controlVertical():
    global ganador
    if (tablero[0][0] ==  tablero[1][0] == tablero[2][0] != "-" or tablero2[0][0] ==  tablero2[1][1] == tablero2[2][2] != "-" ):
        ganador = tablero[0][0]
        gano = "gano vertical"
        return gano
    elif (tablero[0][1] ==  tablero[1][1] == tablero[2][1] != "-" or tablero2[0][0] ==  tablero2[1][1] == tablero2[2][2] != "-" ):
        ganador = tablero[1][1]
        gano = "gano vertical"
        return gano
    elif (tablero[0][2] ==  tablero[1][2] == tablero[2][2] != "-" or tablero[0][0] ==  tablero[1][1] == tablero[2][2] != "-" ) :
        ganador = tablero[2]
        gano = "gano vertical"
        return gano
       
###################################################################
       
def controlDiagonal():
    global ganador
    if (tablero[0][0] ==  tablero[1][1] == tablero[2][2] != "-" ) :
        ganador = tablero[0][0]
        gano = "gano diagonal"
        return gano
    elif tablero[0][2] ==  tablero[1][1] == tablero[2][0] != "-":
        ganador = tablero[2][0]
        gano = "gano diagonal"
        return gano
       
###################################################################
       
def jugada(valor):
    anoto = False
   
    while anoto==False:
        posicionF = int(input("Elige una posicion en fila: "))
        posicionC = int(input("Elige una posicion en columna: "))
        posicionF -= 1
        posicionC -= 1
        if tablero[posicionF] != "-":
            anoto = True
        else:
            print("Esa posicion ya esta ocupada")
           
    tablero[posicionF][posicionC] = valor
    
    ver_tablero(tab)
   
###################################################################
   
def ver_tablero(tab):
   
    if (tab):
       
        print("\n")
        print(tablero[0][0] , " | " , tablero[0][1] , " | " ,  tablero[0][2])
        print(tablero[1][0] , " | " , tablero[1][1] , " | " ,  tablero[1][2])
        print(tablero[2][0] , " | " , tablero[2][1] , " | " ,  tablero[2][2])
        print("\n")
       
    else:
               
        print("\n")
        print(tablero2[0][0] , " | " , tablero2[0][1] , " | " ,  tablero2[0][2] , " | " , tablero2[0][3])
        print(tablero2[1][0] , " | " , tablero2[1][1] , " | " ,  tablero2[1][2] , " | " , tablero2[1][3])
        print(tablero2[2][0] , " | " , tablero2[2][1] , " | " ,  tablero2[2][2] , " | " , tablero2[2][3])
        print(tablero2[3][0] , " | " , tablero2[3][1] , " | " ,  tablero2[3][2] , " | " , tablero2[3][3])
        print("\n")

s="SI"

###################################################################

while s=="SI":
    jugar()
    s=input("desea jugar de nuevo: ").upper()
    tablero =[['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]
