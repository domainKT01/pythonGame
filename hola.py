tablero4=[['-','--','--','--'],
['--','-','--','--'],
['--','-','--','--'],
['--','--','-','--']]
tablero3=[['-','-','-'],
['-','-','-'],
['-','-','-']]

tTablero= int(input("¿quieres jugar en un tablero 3x3 o 4x4?" ))
if tTablero==4: 
  tablero=tablero4

if tTablero==3:
  tablero=tablero3

def fn_datosUsuario():
  fila= int(input("ingrese valor de la fila: "))
  columna= int(input("ingrese el valor de la columna: "))
  return [fila, columna,ficha]

def fn_imprimir(tablero,tTablero):
  if tTablero ==3:
    print(tablero[0][0], tablero[0][1], tablero[0][2], sep= "  |  ")
    print('_______________')
    print(tablero[1][0], tablero[1][1], tablero[1][2],sep= "  |  ")
    print('_______________')
    print(tablero[2][0], tablero[2][1], tablero[2][2],sep= "  |  ")
    
  if tTablero==4:
    print(tablero[0][0], tablero[0][1], tablero[0][2],tablero[0][3], sep= "  |  ")
    print('_______________')
    print(tablero[1][0], tablero[1][1], tablero[1][2],tablero[1][3], sep= "  |  ")
    print('_______________')
    print(tablero[2][0], tablero[2][1], tablero[2][2],tablero[2][3], sep= "  |  ")
    print('_______________')
    print(tablero[3][0], tablero[3][1], tablero[3][2],tablero[3][3], sep= "  |  ")


def fn_ponerFicha(tablero):
  jugada= fn_datosUsuario()
  tablero[jugada[0]-1][jugada[1]-1]= jugada[2]

  return None
 

def jugadorGanador(tablero):
  ganador=""
  if (tablero[0] == [['X', 'X', 'X']] or tablero[0] == [['O', 'O', 'O']]):
    print("ganó por fila 1 el jugador ", tablero[0][0]  )

  elif (tablero[1] == [['X'], ['X'], ['X']] or tablero[1] == [['O'], ['O'], ['O']]):
    print("ganó por fila 2 el jugador ", tablero[1][0]  )

  elif (tablero[2] == [['X', 'X', 'X']] or tablero[1] == [['O'], ['O'], ['O']]):
    print("ganó por fila 3 el jugador ", tablero[0][0]  )


for turno in range(tTablero**2):
  fn_ponerFicha(tablero)
  fn_imprimir(tablero,tTablero)
  jugadorGanador(tablero)
