salariomensual = int(input("Salario base mensual $:"))
cargoempleado = input("Cargo empleado: ")
niveldesempeño = input("Nivel de desempeño: ")

#Los condicionales donde vamos a calcular la vonificacion y los niveles desempeño y cargo

if cargoempleado == "directivo":
    if niveldesempeño == "alto":
        bonificacion = salariomensual * 0.2
    elif niveldesempeño == "medio":
        bonificacion = salariomensual * 0.1
    else :
        bonificacion = 0
elif cargoempleado == "operativo":
    if niveldesempeño == "alto":
        bonificacion = salariomensual * 0.15
    elif niveldesempeño == "medio":
        bonificacion = salariomensual * 0.05
    else:
        bonificacion = 0
else:
    bonificacion = 0

    #Donde se imprime el mensaje
print("----------Resumen del Pago----------")
print(f"Cargo: {cargoempleado.capitalize()}")
print(f"Nivel de Desempeño: {niveldesempeño.capitalize()}")
print(f"Salario Base: ${salariomensual}")
print (f"Bonificación: ${int(bonificacion)}")
print ((f"Total a Recibir: ${int(salariomensual + bonificacion)}"))
print("------------------------------------")









