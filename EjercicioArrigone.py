cant_habitantes = 0
hogar = 0
acu_menores = 0
max_edad = 0
min_edad = -99
cant_vehiculo = 0
vehiculo_existente = 0
acum_total = 0

integrantes_familia = int(input("Ingrese la cantidad de ingreantes (pulse 0 para finalizar): "))

while integrantes_familia != 0 :
    menores = int(input("Ingrese la cantidad de ingreantes menores de edad : "))
    edad_mayor =int(input("Ingrese la edad de la persona de mayor edad : "))
    edad_joven=int(input("Ingrese la edad se la persona de menor edad : "))
    ingreso_familia=float(input("Ingrese el ingreso salarial familiar : "))
    acum_total = acum_total + ingreso_familia
    vehiculo = (input("Posee vehiculo (s/n): "))
    if vehiculo == "s":
        vehiculo_existente = int(input("Cuantos vehiculos posee: "))
        cant_vehiculo = (cant_vehiculo + vehiculo_existente)
    integrantes_familia = int(input("Ingrese la cantidad de ingreantes (pulse 0 para finalizar) : "))    

# calculamos la cantidad de habitantes censados:
cant_habitantes = cant_habitantes + integrantes_familia
hogar = hogar + 1
    
acu_menores = acu_menores + menores
   
#persona mas vieja y mas joven
if edad_mayor > max_edad:
    max_edad = edad_mayor
if edad_joven > min_edad:
    min_edad = edad_joven
        
promedio = (cant_habitantes / hogar)
       
porcentaje_menores = (acu_menores * cant_habitantes / 100)
        
promedio_salario = (acum_total / hogar )
       
porcentaje_vehiculos = (cant_vehiculo * hogar /100)

print("Cantidad de habitantes censados: {}".format(cant_habitantes))
print("El promedio de habitantes por hogar es de: {}".format(promedio))
print("El porcentaje de menores es de: {}% ".format(porcentaje_menores))
print("porcentaje de familia que poseen vehiculo ",porcentaje_vehiculos)
print("La persona mas vieja tiene: {} años y la mas joven {} años.".format(max_edad, min_edad))
print("El promedio del ingreso salarial de todos los hogares censados es de: {} ".format(promedio_salario))
print("Vehiculos censados: {}".format(cant_vehiculo))






