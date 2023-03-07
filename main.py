
def imprimir_A(arreglo):
  tamanio=len(arreglo)
  for i in range(tamanio):
    print(f'[{arreglo[i]}]', end="")
#busqueda lineal
def busqueda_Lineal(arreglo,sueldo):
  resultado=False
  tamanio=len(arreglo)-1
  for i in range(tamanio):
    if (arreglo[i]==sueldo):
      resultado=True
      return resultado
    return resultado

lista_sueldo=[20.8,150.5,170.5,180.8,190,30,75.6,200]
imprimir_A(lista_sueldo)
print("\n")
sueldo=float(input("Ingrese el sueldo a encontrar: "))
respuesta= busqueda_Lineal(lista_sueldo,sueldo)
if respuesta:
  print("El sueldo fue encontrado en nuestro sistema")
else:
  print("El sueldo no fue encontrado en nuestro sistema")
  