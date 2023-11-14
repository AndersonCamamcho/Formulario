import datetime

# Variables:
name = []
age = []
expedition_date = []
current_date = datetime.datetime.now()

while True:
    try:
        forms = int(input(" » Ingrese aqui la cantidad de personas a registrar: "))
        if forms > 0:
            break
        else:
            print("Entrada no valida, el numero proporcionado debe ser positivo.")

    except ValueError:
        print("Entrada no valida, el valor proporcionado debe ser un entero.")


for i in range(1, forms + 1):

    if i > 1:
        print("     **********************  *  *  *  ****************************")
        print("                   INICIO NUEVO FORMULARIO")
        print("     **********************  *  *  *  ****************************")


# Home name intention for the form:
    while True:
        try:
            form_name = input(" » Ingrese aqui un nombre para el formulario, no mayor a 20 caracteres: ")
            validate_name = len(form_name)
            if validate_name <= 20 and not form_name[0].isspace():
                name.append(form_name)
                break
            else:
                print("Entrada incorrecta.")
        except:
            print("Entrada incorrecta")





# Home obtaining age for the form:
    while True:
        try:
            form_ege = int(input(" » Ingrese aqui su edad: "))
            if 18 <= form_ege <= 100:
                age.append(form_ege)
                break
            else:
                print("Recuerde que la edad debe estar entre 18 y 100 años, por favor intente de nuevo.")
        except ValueError:
            print("No esta ingresando numeros enteros, por favor intente de nuevo.")



# Start obtaining the issue date for the form:
    while True:
        try:
            date_entered = input(" » Ingrese aqui la fecha de expedicion con el siguiente formato: dia/mes/año(completo):   ")
            form_date= datetime.datetime.strptime(date_entered, "%d/%m/%Y")

            date_to_be_validated = current_date.year - form_date.year
            if 0 <= date_to_be_validated <= 100:
                expedition_date.append(form_date)
                break
            else:
                print("La fecha ingresada no debe ser mayor a 100, ni menor a 0 años, intente de nuevo.")


        except ValueError:
            print("Esta ingresando un formato incorrecto, recuerde que debe ser: dia/mes/año(completo)")





    if i == forms:

        for j in range(0, forms):

            print("")
            print("***********  *  *****  *  *****  *  **********")
            print(name[j].upper())
            print("   Edad : ", age[j])
            print("   fecha de expedición : ", expedition_date[j].strftime("%d/%m/%Y"))
            print("***********  *  *****  *  *****  *  **********")
            print("")

