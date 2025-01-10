# Este programa gestiona un sistema de registros de estudiantes.
# Permite agregar, eliminar, consultar y mostrar la cantidad de estudiantes inscritos.
# Se almacenan las matrículas, nombres completos, curso, edad y dirección de los estudiantes.

# Variables:
# 1) matriculas (list): Lista que almacena las matrículas de los estudiantes inscritos (tipo de dato: lista de enteros).
# 2) registro_estudiantes (dict): Diccionario que asocia cada matrícula con los datos del estudiante (tipo de dato: diccionario).
# 3) entrada_valida (bool): controla si la matrícula ingresada es válida para permitir continuar o repetir la solicitud. (tipo de dato: Booleano).
# 4) matricula (int): Variable temporal para almacenar la matrícula ingresada por el usuario (tipo de dato: entero).
# 5) nombre_completo (str): Variable temporal para almacenar el nombre completo del estudiante (tipo de dato: string).
# 6) curso (str): Variable temporal para almacenar el curso del estudiante (tipo de dato: string).
# 7) edad (int): Variable temporal para almacenar la edad del estudiante (tipo de dato: entero).
# 8) direccion (str): Variable temporal para almacenar la dirección del estudiante (tipo de dato: string).
# 9) cantidad_inscritos (int): Variable para almacenar el número de estudiantes inscritos (tipo de dato: entero).
# 10) opcion (str): Variable para almacenar la opción seleccionada por el usuario (tipo de dato: string).

# Lista para almacenar las matrículas de los estudiantes
matriculas = []
# Diccionario para asociar matrícula con los datos del estudiante
registro_estudiantes = {}


def agregar_registro(matriculas):  # Función para agregar un estudiante al registro.
    print("*************** Agregar Registro ***************")

    # Inicializar la variable booleana para validar la entrada
    entrada_valida = False

    while not entrada_valida:  # Bucle While que se repite hasta que se ingrese una matrícula válida
        matricula = input('Ingrese matrícula: ')

        # Verifica si la entrada es un número entero
        if matricula.isdigit():  # Comprobamos si la entrada es un número
            matricula = int(matricula)  # Si la matricula ingresada es válida la convertimos a entero
            entrada_valida = True  # Marcamos la entrada como válida
        else:
            print("Entrada no válida. Por favor, ingrese un número entero para la matrícula.")  # Mensaje de error

    if matricula not in matriculas:  # Condición para verificar si la matrícula no está registrada
        nombre_completo = input("Ingrese nombres completos: ")
        curso = input("Ingrese curso: ")
        edad = int(input("Ingrese edad: "))
        direccion = input("Ingrese dirección: ")

        matriculas.append(matricula)  # Se agrega la matrícula a la lista
        registro_estudiantes[matricula] = {
            "nombre": nombre_completo,
            "curso": curso,
            "edad": edad,
            "direccion": direccion
        }  # Se asocia la matrícula con datos del estudiante

        print("*************** Registro agregado con éxito ***************")
    else:
        print('El número de matrícula ya está inscrita.')

    return matriculas


def eliminar_registro(matriculas):  # Función para eliminar un estudiante del registro.
    print("*************** Eliminar Registro ***************")
    matricula = int(input('Ingrese matrícula: '))

    if matricula in matriculas:
        matriculas.remove(matricula)  # Eliminar la matrícula de la lista
        registro_estudiantes.pop(matricula, None)  # Eliminar el registro del diccionario
        print("*** Estudiante eliminado del registro ***")
    else:
        print('La matrícula no está inscrita.')

    return matriculas


def consultar_registro(matriculas):  # Función para consultar matrícula y mostrar los datos del estudiante.
    print("*************** Consultar Registro ***************")
    matricula = int(input('Ingrese matrícula: '))

    if matricula in matriculas:
        print("**** El número de matrícula está inscrita con los siguientes datos: ****")
        estudiante = registro_estudiantes[matricula]
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Curso: {estudiante['curso']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Dirección: {estudiante['direccion']}")
    else:
        print("La matrícula no está inscrita.")

    print("*************** Consulta realizada con éxito ***************")


def mostrar_cupo_actual(matriculas):  # Función para mostrar la cantidad actual de estudiantes inscritos.
    print("******************** Cupo Actual ********************")
    cantidad_inscritos = len(matriculas)  # Contar el número de inscritos
    print(f"Cantidad de estudiantes inscritos: {cantidad_inscritos}")
    print("*************** Cupo mostrado con éxito ***************")


# Programa principal
while True:
    # Muestra el menú de opciones
    print("*************** Unidad Educativa Tena ***************")
    print('1) Agregar registro')
    print('2) Eliminar registro')
    print('3) Consultar registro')
    print('4) Cupo actual de Matrículas')
    print('5) Salir')

    # Solicita una opción al usuario
    opcion = input('Elija una opción: ')

    # Procesa la opción seleccionada
    if opcion == '1':
        matriculas = agregar_registro(matriculas)
    elif opcion == '2':
        matriculas = eliminar_registro(matriculas)
    elif opcion == '3':
        consultar_registro(matriculas)
    elif opcion == '4':
        mostrar_cupo_actual(matriculas)
    elif opcion == '5':
        print("*************** Gracias por usar el sistema. Adiós. ***************")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
