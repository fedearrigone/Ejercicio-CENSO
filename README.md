# Ejercicio-CENSO
#1) Usted fue seleccionado para realizar el programa del CENSO Argentina. Como primera prueba, el 
#programa simula el ingreso de los integrantes de una familia en toda una cuadra. El programa 
#deber registrar lo siguiente:
#a. Cantidad de integrantes en la familia. 
#b. Cantidad de menores de 18 años.
#c. Edad de la persona más vieja y edad de la persona más joven.
#. Ingreso salarial de la familia.
#. Informar si tiene vehículos (s/n) y si tiene, cuantos.
#. El fin de ingreso se indica con cantidad de integrantes = 0
#Se pide calcular e informar lo siguiente: 
# Cantidad de habitantes censados. 
# Promedio de habitantes por hogar censados. 
# Porcentaje de menores. 
#Informar cuantos #años tiene la persona mas vieja y la más joven. 
# Informar el promedio de ingreso familiar de todos los hogares censados. 
# Informar cuantos vehículos fueron censados. 
# Porcentaje de vehículos por familia censados

vehiculo_existente = 0
cant_habitantes = 0
hogar = 0
acu_menores = 0
max_edad = 0
min_edad = -99
cant_vehiculo = 0
acum_total = 0

integrantes_familia = int(input("Ingrese la cantidad de ingreantes : "))

while integrantes_familia != 0 :
    menores = int(input("Ingrese la cantidad de ingreantes menores : "))
    edad_mayor =int(input("Ingrese la edad e la persona mas vieja : "))
    edad_joven=int(input("Ingrese la edad e la persona mas joven : "))
    ingreso_familia=float(input("Ingrese ingreso salarial familiar : "))
    acum_total = acum_total + ingreso_familia
    vehiculo = (input("Posee vehiculo (s/n): "))
    if vehiculo == "s":
        vehiculo_existente = int(input("Cuantos vehiculos: "))
        cant_vehiculo = (cant_vehiculo + vehiculo_existente)
    #cantidad de habitantes censados
    cant_habitantes = cant_habitantes + integrantes_familia
    hogar = hogar + 1
    acu_menores = acu_menores + menores
    #persona mas vieja y mas joven
    if edad_mayor > max_edad:
        max_edad = edad_mayor

    integrantes_familia = int(input("Ingrese la cantidad de ingreantes : "))

#promedio
promedio = (cant_habitantes * hogar /100)
#porcentaje menores
porcentaje_menores = (acu_menores * cant_habitantes / 100)
#persona mas vieja y mas joven
promedio_salario = (acum_total / hogar )
#porcentaje de vehiculos
porcentaje_vehiculos = (cant_vehiculo * 100/ hogar)

if integrantes_familia == 0:
    print("porcentaje de familia que poseen vehiculo ",porcentaje_vehiculos)
    print("salario",promedio_salario)
    print("acum total", acum_total)
    print("cant_vehiculo",cant_vehiculo)
    print("max edad",max_edad)
    print(porcentaje_menores)
    print(promedio)
    print(cant_habitantes)
    exit("Gracias por usar Censito")
