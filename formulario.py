import datetime

formularios = int(input("Ingrese la cantidad de formularios que desea imprimir: "))
nombre = []
edad = []
fecha_expedicion = []

for i in range(1,formularios+1):


# Inicio furmulario que obtiene el nombre del formulario:

    nombre_formulario = input("Por favor ingrese un nombre para el formulario que no pase de 20 caracteres: ")
    validar_nombre = len(nombre_formulario)

    if validar_nombre <= 20:
        nombre.append(nombre_formulario)
    else:
        print("Nombre demasiado largo, inicie de nuevo el proceso")
        break


#Inicio formulario de edad

    edad_formulario = int(input("Ingrese su edad: "))
    if edad_formulario >= 18 or edad <= 100:
        edad.append(edad_formulario)
    else:
        print("Edad invalida, inicie de nuevo el proceso")
        break

#Inicio formulario de fecha de expeidción

    fecha_ingresada = input("Ingrese la fecha de expedicion con el siguiente formato: dia-mes-año:   ")
    fecha_formulario= datetime.datetime.strptime(fecha_ingresada, "%d-%m-%y")
    if fecha_formulario < datetime.datetime.now():
        fecha_expedicion.append(fecha_formulario)
    else:
        print("Formato incorrecto, inicie de nuevo el proceso")
        break





    if i == formularios:
        print("***************  * *************  *  ****************   *    ********************")
        print("Los datos recoletados para los nombres del formulario son : ", nombre)
        print("Los datos recoletados para edades del formulario son : ", edad)
        print("Los datos recoletados para fechas de expedición del formulario son : ", fecha_expedicion)
        print("***************  * *************  *  ****************   *    ********************")

