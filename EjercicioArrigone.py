
from pickle import TRUE


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






