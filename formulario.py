import datetime

# Variables:
nombre = []
edad = []
fecha_expedicion = []
fecha_actual = datetime.datetime.now()

while True:
    try:
        formularios = int(input(" » Ingrese aqui la cantidad de personas a registrar: "))
        if formularios > 0:
            break
        else:
            print("Entrada no valida, el numero proporcionado debe ser positivo.")

    except ValueError:
        print("Entrada no valida, el valor proporcionado debe ser un entero.")


for i in range(1,formularios+1):

    if i > 1:
        print("     **********************  *  *  *  ****************************")
        print("                   INICIO NUEVO FORMULARIO")
        print("     **********************  *  *  *  ****************************")


# Inicio ontención de nombre para el formulario:

    while True:

        nombre_formulario = input(" » Ingrese aqui un nombre para el formulario, no mayor a 20 caracteres: ")
        validar_nombre = len(nombre_formulario)
        if validar_nombre <= 20 and not nombre_formulario[0].isspace():
            nombre.append(nombre_formulario)
            break
        else:
            print("Entrada incorrecta.")




# Inicio obtención de edad para el formulario:

    while True:
        try:
            edad_formulario = int(input(" » Ingrese aqui su edad: "))
            if 18 <= edad_formulario <= 100:
                edad.append(edad_formulario)
                break
            else:
                print("Recuerde que la edad debe estar entre 18 y 100 años, por favor intente de nuevo.")
        except ValueError:
            print("No esta ingresando numeros enteros, por favor intente de nuevo.")



# Inicio obtención de fecha de expeidción para el formulario:
    while True:
        try:
            fecha_ingresada = input(" » Ingrese aqui la fecha de expedicion con el siguiente formato: dia/mes/año(completo):   ")
            fecha_formulario= datetime.datetime.strptime(fecha_ingresada, "%d/%m/%Y")

            fecha_por_validar = fecha_actual.year - fecha_formulario.year
            if 0 <= fecha_por_validar <= 100:
                fecha_expedicion.append(fecha_formulario)
                break
            else:
                print("La fecha ingresada no debe ser mayor a 100, ni menor a 0 años, intente de nuevo.")


        except ValueError:
            print("Esta ingresando un formato incorrecto, recuerde que debe ser: dia/mes/año(completo)")





    if i == formularios:

        for j in range(0,formularios):

            print("")
            print("***********  *  *****  *  *****  *  **********")
            print(nombre[j].upper())
            print("   Edad : ", edad[j])
            print("   fecha de expedición : ", fecha_expedicion[j].strftime("%d/%m/%Y"))
            print("***********  *  *****  *  *****  *  **********")
            print("")

