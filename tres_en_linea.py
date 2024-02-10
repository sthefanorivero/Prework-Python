def crear_tablero():
  tablero = [['' for interador in range (3)] for interador in range (3)]
  return(tablero)

def imprimir_tablero():
  tablero = crear_tablero()
  print("-" * 9 )
  for fila in tablero:
    print("  | ".join(fila))
    print("-" * 9 )

def is_tablero_lleno(tablero):
  return all(all(casilla != "" for casilla in fila ) for fila in tablero)

def comprobar_ganadro(tablero, jugador):
  for i in range (3):
    for j in range(3):
     if all (tablero [i][j] == jugador) or all(tablero [j][i]):
       return True 
     if all (tablero [i][i] == jugador) or all(tablero [i][2-i]):
       return True 
  return False 

def tres_en_linea():
  tablero = crear_tablero()
  jugador_actual = 'x'
  
  print('Bienvenido/a!! Estas jugando al tres en linea')
  imprimir_tablero (tablero)
  while True:
    
   print(f'Turno de jugador{jugador_actual}')
   fila = int(input('Elige fila 0, 1, 2: '))
   columna = int(input('Elige columna 0, 1, 2: '))
   if tablero [fila][columna] == ' ':
       tablero[fila][columna] = jugador_actual
       
       if comprobar_ganadro (tablero, jugador_actual):
        print(f'EL jugador {jugador_actual} ha ganado')
        break
       if is_tablero_lleno(tablero):
        print('Empate')
        break
       jugador_actual = 'O' if jugador_actual == 'x' else  'x'  
       
        

   else: 
     print ('Casilla ocupada')

if __name__ == "_main_":
 tres_en_linea()