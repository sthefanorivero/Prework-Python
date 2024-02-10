def sumar(x, y):
  return x + y 

def restar(x, y):
  return x - y 

def multiplicar(x, y):
  return x * y 

def dividir(x, y):
  if y != 0:
    return x/y
  else:
    return 'Error matematico'

def potencia (x, y):
  return x ** y 

def raiz_cuadrada(x, y):
  if x >= 0:
    return x ** 0.5 
  else:
    return 'Error matematico'

def calculadora():
  print('¡Bienvenidos a la calculadora!')
  while True: 
    eleccion=input('Seleccione una operacion Sumar(1)/Restar(2)/Multiplicari(3)/Dividir(4)/Raiz Cuadrada(5)/Elevar un numero a otro(6) / Salir (7): ')
    if eleccion == 7:
      break
    elif eleccion in ['1','2','3','4','5']: 
      x = int(input('Introduce el primer numero'))
      y = int(input('Introduce el segundo numero'))
      if eleccion == 1:
       result = sumar (x,y)
      if eleccion == 2:
       result = restar (x,y)
      if eleccion == 3:
       result = multiplicar (x,y)
      if eleccion == 4 :
       result = dividir (x,y)
      if eleccion == 5:
       result = potencia (x,y)
    elif eleccion == 6:
      x = int(input ('Introduce el número sobre el que realizar la raiz cuadrada: '))
      result = raiz_cuadrada(x)
    else:
      print (f'{eleccion}No es una opcion valida')
  
    print(result)
  
  if __name__ == "_main_":
    calculadora()

