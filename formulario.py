import datetime

while True:
    try:
        formularios = int(input(" » Ingrese aqui la cantidad de personas a registrar: "))
        if formularios > 0:
            break
        else:
            print("Entrada no valida, el numero proporcionado debe ser positivo.")

    except ValueError:
        print("Entrada no valida, el valor proporcionado debe ser un entero.")
nombre = []
edad = []
fecha_expedicion = []

for i in range(1,formularios+1):


# Inicio ontención de nombre para el formulario:

    while True:

        nombre_formulario = input(" » Ingrese aqui un nombre para el formulario, no mayor a 20 caracteres: ")
        validar_nombre = len(nombre_formulario)
        if validar_nombre <= 20 and not nombre_formulario[0].isspace():
            nombre.append(nombre_formulario)
            break
        else:
            print("Entrada incorrecta, asegurese de que el primer caracter no sea un espacio")




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

    fecha_ingresada = input(" » Ingrese aqui la fecha de expedicion con el siguiente formato: dia/mes/año(completo):   ")
    fecha_formulario= datetime.datetime.strptime(fecha_ingresada, "%d/%m/%Y")
    if fecha_formulario < datetime.datetime.now():
        fecha_expedicion.append(fecha_formulario)
    else:
        print("Esta ingresando un formato incorrecto")
        break





    if i == formularios:
        print("***************  * *************  *  ****************   *    ********************")
        print("Los datos recoletados para los nombres del formulario son : ", nombre)
        print("Los datos recoletados para edades del formulario son : ", edad)
        print("Los datos recoletados para fechas de expedición del formulario son : ", fecha_expedicion)
        print("***************  * *************  *  ****************   *    ********************")

