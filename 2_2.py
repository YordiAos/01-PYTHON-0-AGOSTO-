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

#igual igual igual en python
if dato_1==dato_2==dato_3:
    print('todos son iguales')
    
#tenemos 3 casos
#1 caso
elif dato_1==dato_2:
    print('Existe 2 valores que son iguales')
    if dato_1>dato_3:
        print ('Los mayores son: ',dato_1,dato_2)#podria poner cualquiera
    else:
        print ('el mayor es: ',dato_3)
#2 caso
elif dato_2==dato_3:
    print('Existe 2 valores que son iguales')
    if dato_2>dato_1:
        print ('Los mayores son: ',dato_2,dato_2)#podria poner cualquiera
    else:
        print ('el mayor es: ',dato_1)
# 3 caso    
elif dato_1==dato_3:
    print('Existe 2 valores que son iguales')
    if dato_1>dato_2:
        print ('Los mayores son: ',dato_1,dato_1)#podria poner cualquiera
    else:
        print ('el mayor es: ',dato_2)
        
elif dato_1>dato_2 and dato_1>dato_3 and True:#pude haber puesto un booleano
    print('El mayor es: ',dato_1)
elif dato_2>dato_1 and dato_2>dato_3:
    print('El mayor es: ',dato_2)
else:
    print('El mayor es: ',dato_3)
#else:
 #   print('Existen valores q no son iguales')
