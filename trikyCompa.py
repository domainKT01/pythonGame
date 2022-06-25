# tablero
tablero = [["-", "-", "-", "-"], ["-", "-", "-", "-"],
    ["-", "-", "-", "-"], ["-", "-", "-", "-"]]

# tamaño del tablero
tTablero = int(input(
    "Si quieres jugar en un tablero 3x3 escribe 3 o Si quieres jugar en un tablero 4x4? escribe 4 "))

# datos del usuario


def fn_datosUsuario():
    anoto = False
    while anoto == False:
        fila = int(input("ingrese valor de la fila: "))-1
        columna = int(input("ingrese el valor de la columna: "))-1
        if tablero[fila][columna] != "-":
            print("Esa posicion ya esta ocupada")
            anoto = False
        else:
            anoto = True
    return fila, columna

# imprime tablero 3x3 o 4x4 
def fn_imprimir(tablero,tTablero):
  if tTablero ==3:
    print(tablero[0][0], tablero[0][1], tablero[0][2],sep= "   | ")
    print("________________")
    print(tablero[1][0], tablero[1][1], tablero[1][2],sep= "   | ")
    print("________________")
    print(tablero[2][0], tablero[2][1], tablero[2][2],sep= "   | ")
  
  if tTablero==4:
    print(tablero[0][0], tablero[0][1], tablero[0][2],tablero[0][3], sep= "  |  ")
    print("________________________")
    print(tablero[1][0], tablero[1][1], tablero[1][2],tablero[1][3], sep= "  |  ")
    print("________________________")
    print(tablero[2][0], tablero[2][1], tablero[2][2],tablero[2][3], sep= "  |  ")
    print("________________________")
    print(tablero[3][0], tablero[3][1], tablero[3][2],tablero[3][3], sep= "  |  ")

 
# ganador 
def ganador(tablero):
  cont=1
  ganador=""
  while cont<3:
    for i in range(4):
      if tablero[i][0]==tablero[i][1]==tablero[i][2]!="-":
        cont+=2
        print("ganó por fila ",i," el jugador ", tablero[i][0]  )
        ganador=tablero[i][0]
      if tablero[i][1]==tablero[i][2]==tablero[i][3]!="-":
        cont+=2
        print("ganó por fila ",i, " el jugador ", tablero[i][0]  )
        ganador=tablero[i][0]
      if tablero[0][i]==tablero[1][i]==tablero[2][i]!="-":
        cont+=2
        print("ganó por columna ", i, " el jugador ", tablero[0][i]  )
        ganador=tablero[0][i]  
      if tablero[1][i]==tablero[2][i]==tablero[3][i]!="-":
        cont+=2
        print("ganó por columna",i, " el jugador ", tablero[1][i]  )
        ganador=tablero[1][i]    
    if tablero[0][0]==tablero[1][1]==tablero[2][2] != "-":
      print("ganó por diagonal  el jugador ", tablero[0][0]  )
      ganador=tablero[0][0]
      cont+=2
    if tablero[2][0]==tablero[1][1]==tablero[0][2] != "-":
      print("ganó por diqgonal  el jugador ", tablero[2][0]  )
      ganador=tablero[2][0]
      cont+=2 
    if tablero[1][2]==tablero[2][1]==tablero[3][0]!="-":
      print("ganó por diagonal  el jugador ", tablero[1][2] )
      ganador=tablero[1][2]
      cont+=2
    if tablero[1][1]==tablero[2][2]==tablero[3][3]!="-":
      print("ganó por diagonal el jugador ", tablero[1][1] )
      ganador=tablero[1][1]
      cont+=2
    if tablero[1][0]==tablero[2][1]==tablero[3][2]!="-":
      print("ganó por diagonal el jugador ", tablero[1][0] )
      ganador=tablero[1][0]
      cont+=2
    if tablero[0][1]==tablero[1][2]==tablero[2][3]!="-":
      print("ganó por diagonal el jugador ", tablero[0][1] )
      ganador=tablero[0][1]
      cont+=2
    if tablero[0][2]==tablero[1][1]==tablero[2][0]!="-":   
      print("ganó por diagonal el jugador ", tablero[0][2] )
      ganador=tablero[0][2]
      cont+=2
    if tablero[1][3]==tablero[2][2]==tablero[3][1]!="-":
      print("ganó por diagonal el jugador ", tablero[1][3] )
      ganador=tablero[1][3]
      cont+=2
    else:
      break
  return ganador 

for turno in range(tTablero**2):

  if turno %2 == 0:
    print("juega la X ")
    f , c =fn_datosUsuario()
    tablero[f][c] = "X"
    fn_imprimir(tablero,tTablero)
    g=ganador(tablero)
    if g == "X" or g == "O":
      break
  if turno %2 == 1:
    print("juega la O ")
    f , c =fn_datosUsuario()
    tablero[f][c] = "O"
    fn_imprimir(tablero,tTablero)
    g =ganador(tablero)
    if g == "X" or g == "O":
      break