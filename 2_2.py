#2.2 condicional if
#2.3 IDENTACION
#2.4 Condicional if anidado
dato_1=int(input('Ingresa  numero 1:'))
dato_2=int(input('Ingresa  numero 2: '))
dato_3=int(input('Ingresa  numero 3: '))
cadena='holassss'
#print(dato_1+dato_2,cadena)
#print(dato_1,dato_2,cadena)
"""comment multilinea"""
'''
if dato_1>dato_2:
    if dato_1>dato_3:
        print('El mayor es: ',dato_1)
    else:
        print('el mayor es: ',dato_3)
else:
    if dato_2>dato_3:
        print('El mayor es: ',dato_2)
    else:
        print('El mayor es:',dato_3)
'''
#REALIZANDO LO MISMO con menos lineas
if dato_1>dato_2 and dato_1>dato_3 and True:#pude haber puesto un booleano
    print('El mayor es: ',dato_1)
elif dato_2>dato_1 and dato_2>dato_3:
    print('El mayor es: ',dato_2)
else:
    print('El mayor es: ',dato_3)
#igual igual igual en python
if dato_1==dato_2==dato_3:
    print('todos son iguales')
else:
    print('Existen valores q no son iguales')
