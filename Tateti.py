import random
import numpy as np


# Nombre del módulo: CargarEquipos
# Descripción: Carga los datos de los jugadores de ambos equipos.
# Datos de Entrada: ids_existentes
# Datos de Salida: equipos (array de jugadores), dimEquipos (cantidad de jugadores por equipo).
def obtener_id(ids_existentes):
    id_usuario = input("Por favor, ingrese su ID (número): ")
    
    # Valida que el ID sea un número de exactamente 3 dígitos sin usar len
    if not id_usuario.isdigit() or not (100 <= int(id_usuario) <= 999):
        print("El ID debe ser un número de 3 cifras.")
        return obtener_id(ids_existentes)  # Llamada recursiva si no es válido

    id_usuario = int(id_usuario)  # Convierte a entero

    # Verifica si el ID ya existe
    if id_usuario in ids_existentes:
        print("El ID ya existe. Por favor, ingrese un ID único.")
        return obtener_id(ids_existentes)  # Llamada recursiva si ya existe

    return id_usuario


# Nombre del módulo: CargarEquipos
# Descripción: Carga los datos de los jugadores de ambos equipos.
# Datos de Entrada: max_jugadores
# Datos de Salida: equipos (array de jugadores)



def cargar_equipos(max_jugadores): 
    tipo_jugador = np.dtype([('id', int), ('nombre', 'U30'), ('puntaje', int)])
    equipos = np.empty((2, max_jugadores), dtype=tipo_jugador)

    # Crear un arreglo cn los IDs únicos
    ids_existentes = [0] * (max_jugadores * 2)  # Inicia una lista con el tamaño necesario

    # Carga de jugadores del equipo Círculo
    print("CARGA TUS JUGADORES DE EQUIPO CÍRCULO (O):")
    for i in range(max_jugadores):
        id_jugador = obtener_id(ids_existentes)  # Llamada al módulo obtener_id
        ids_existentes[i] = id_jugador  # Asignar el ID al arreglo
        nombre = input(f"Ingrese el nombre del jugador {i + 1} del equipo Círculo: ")
        equipos[0][i] = (id_jugador, nombre, 0)

    # Carga de jugadores del equipo Cruz
    print("CARGA TUS JUGADORES DE EQUIPO CRUZ (X):")
    for i in range(max_jugadores):
        id_jugador = obtener_id(ids_existentes)  # Llamada al módulo obtener_id
        ids_existentes[i + max_jugadores] = id_jugador  # Asignar el ID al arreglo
        nombre = input(f"Ingrese el nombre del jugador {i + 1} del equipo Cruz: ")
        equipos[1][i] = (id_jugador, nombre, 0)

    return equipos



# Nombre del módulo: ElegirJugadorAleatorio
# Descripción: Selecciona un jugador aleatorio de un equipo dado. 
# luego elimina al jugador de la lista después de haber sido seleccionado.
# Datos de Entrada: equipo (array de jugadores), dim (número de jugadores en el equipo).
# Datos de Salida: jugador seleccionado (un registro de jugador).
def elegir_jugador_aleatorio(equipo, jugadores_seleccionados):
    # Filtrar jugadores disponibles
    jugadores_disponibles = []
    for jugador in equipo:
        if jugador['id'] not in jugadores_seleccionados:
            jugadores_disponibles += [jugador]  # Añadir jugador a la lista de disponibles

    # Verificar si hay jugadores disponibles
    if not jugadores_disponibles:
        print("No hay más jugadores disponibles en este equipo.")
        return None

    # Seleccionar un jugador aleatorio
    jugador_seleccionado = random.choice(jugadores_disponibles)

    # Actualizar la lista de jugadores seleccionados
    jugadores_seleccionados += [jugador_seleccionado['id']]  # Añadir ID del jugador seleccionado

    return jugador_seleccionado

# Nombre del módulo: LanzarDado
# Descripción: Lanza un dado y devuelve un número entre 1 y 6.
# Datos de Entrada: Ninguno.
# Datos de Salida: resultado (número aleatorio entre 1 y 6).
def lanzar_dado():
    resultado = random.randint(1, 6)
    return resultado

# Nombre del módulo: InicializarTablero
# Descripción: Inicializa un tablero vacío para el juego de TA-TE-TI.
# Datos de Entrada: Ninguno.
# Datos de Salida: tablero (lista de listas que representa el tablero).
def inicializar_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

# Nombre del módulo: MostrarTablero
# Descripción: Muestra el estado actual del tablero.
# Datos de Entrada: tablero (estado actual del juego), hay_ganador (booleano que indica si hay ganador).
# Datos de Salida: Ninguno.
def mostrar_tablero(tablero, mostrar_ganadores=False, es_empate=False, ganadores=None, posiciones_ganadoras=None):
    # Mostrar índices de columnas
    print("   1   2   3")
    print("  ┌───────────┐")

    for i, fila in enumerate(tablero):
        # Mostrar índice de fila
        print(f"{i + 1} │", end=" ")
        for j, simbolo in enumerate(fila):
            # Determinar color basado en el estado del juego
            if es_empate:
                color = "\033[90m"  # Gris para empate
            elif mostrar_ganadores and ganadores and simbolo in ganadores:
                color = "\033[91m"  # Rojo para el ganador
            elif posiciones_ganadoras and (i, j) in posiciones_ganadoras:
                color = "\033[91m"  # Rojo para las posiciones ganadoras
            else:
                color = "\033[0m"  # Sin color para otros símbolos

            print(color + simbolo + "\033[0m", end=" │ ")  # Agrega el color al símbolo y restablece el color
        print("\n  └───────────┘")
        print("   └───────────┘")
# Nombre del módulo: VerificarGanador
# Descripción: Verifica si hay un ganador en el tablero.
# Datos de Entrada: tablero (estado actual del juego).
# Datos de Salida: .
def verificar_ganador(tablero):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != " ":
            return fila[0]

    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != " ":
            return tablero[0][col]

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]

    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]

    return None

# Nombre del módulo: RealizarMovimiento
# Descripción: Permite a un jugador realizar un movimiento en el tablero.
# Datos de Entrada: tablero (estado actual del juego), simbolo (símbolo del jugador que realiza el movimiento).
# Datos de Salida: exito (booleano que indica si el movimiento fue exitoso), abandono (booleano que indica si el jugador abandonó).
def realizar_movimiento(tablero, simbolo):
    # Validar la fila
    fila_valida = False
    while not fila_valida:
        fila_input = input("Elige una fila (1-3): ")
        if fila_input.isdigit() and 1 <= int(fila_input) <= 3:
            fila = int(fila_input) - 1  # Convertimos a índice
            fila_valida = True  # La entrada es válida, salimos del ciclo
        else:
            print("Entrada inválida. Debes ingresar un número del 1 al 3.")

    # Validar la columna
    columna_valida = False
    while not columna_valida:
        columna_input = input("Elige una columna (1-3): ")
        if columna_input.isdigit() and 1 <= int(columna_input) <= 3:
            columna = int(columna_input) - 1  # Convertimos a índice
            columna_valida = True  # La entrada es válida, salimos del ciclo
        else:
            print("Entrada inválida. Debes ingresar un número del 1 al 3.")

    # Verificamos si el espacio está vacío
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = simbolo
        return True  # Movimiento exitoso
    else:
        print("Ese espacio ya está ocupado. Intenta de nuevo.")
        return False  # Movimiento no exitoso



# Nombre del módulo: ActualizarPuntajes
# Descripción: Actualiza los puntajes de los jugadores después de una partida.
# Datos de Entrada: ganador (registro del jugador ganador), movimientos (número de movimientos realizados), equipos (array de jugadores).
# Datos de Salida: Ninguno.
# Función para actualizar los puntajes
def actualizar_puntajes(ganador, movimientos,equipos, jugador_circulo, jugador_cruz, empates):
    if ganador:
        # Si hay un ganador, se le suman 3 puntos
        for equipo in equipos:  # Recorrer los equipos
            for jugador in equipo:  # Recorrer los jugadores del equipo
                if jugador['id'] == ganador['id']:  # Si el jugador es el ganador
                    jugador['puntaje'] += 3  # Sumar 3 puntos al ganador
                    print(f"¡{ganador['nombre']} ha ganado y recibe 3 puntos!")
        # Resetear los empates después de un ganador
        empates = 0

    else:
        # Si hay empate, se aumentan los empates
        empates += 1
        print(f"Empate {empates} de 3.")
        
        # Si se alcanzan 3 empates, sumar 1 punto a cada jugador
        if empates >= 3:
            jugador_circulo['puntaje'] += 1  # Sumar 1 punto al jugador de Círculo
            jugador_cruz['puntaje'] += 1  # Sumar 1 punto al jugador de Cruz
            print(f"{jugador_circulo['nombre']} recibe 1 punto por empate.")
            print(f"{jugador_cruz['nombre']} recibe 1 punto por empate.")
            # Después de 3 empates, reiniciar el contador
            empates = 0

    return empates  


# Nombre del módulo: MostrarPuntajes
# Descripción: Muestra los puntajes actuales de los jugadores.
# Datos de Entrada: equipos (array de jugadores), dimEquipos (cantidad de jugadores por equipo).
# Datos de Salida: Ninguno.
def mostrar_puntajes(equipos, dimEquipos):
    print("\n   Puntajes actuales")
    print("  ┌───────────────┬───────────────┐")
    print("  │   Círculo (O) │   Cruz (X)    │")
    print("  ├───────────────┼───────────────┤")
    
    for i in range(dimEquipos):
        nombre_circulo = equipos[0][i]['nombre']
        puntaje_circulo = equipos[0][i]['puntaje']
        nombre_cruz = equipos[1][i]['nombre']
        puntaje_cruz = equipos[1][i]['puntaje']
        
        
        print(f"│ {nombre_circulo:<12} {puntaje_circulo:>3}│ {nombre_cruz:<12} {puntaje_cruz:>3}│")
    
    print("  └───────────────┴───────────────┘")


# Nombre del módulo: ObtenerPosicionesGanadoras
# Descripción: Devuelve las posiciones de las celdas ganadoras en el tablero.
# Datos de Entrada: tablero (estado actual del juego), simbolo (símbolo del jugador ganador).
# Datos de Salida: posiciones ( posiciones ganadoras).
def obtener_posiciones_ganadoras(tablero, simbolo):
    posiciones = []

    # Verificar filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == simbolo:
            posiciones = posiciones + [(i, 0), (i, 1), (i, 2)]

    # Verificar columnas
    for j in range(3):
        if tablero[0][j] == tablero[1][j] == tablero[2][j] == simbolo:
            posiciones = posiciones + [(0, j), (1, j), (2, j)]

    # Verificar diagonal principal
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == simbolo:
        posiciones = posiciones + [(0, 0), (1, 1), (2, 2)]

    # Verificar diagonal secundaria
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == simbolo:
        posiciones = posiciones + [(0, 2), (1, 1), (2, 0)]

    return posiciones




# Nombre del módulo: JugarPartida
# Descripción: Controla la lógica de una partida entre dos jugadores.
# Datos de Entrada: jugador1 (registro del primer jugador), jugador2 (registro del segundo jugador),equipoinicial
# Datos de Salida: ganador (registro del jugador ganador o None si hay empate), movimientos (número de movimientos realizados), abandono (booleano que indica si la partida fue abandonada).
def jugar_partida(jugador1, jugador2, equipo_inicial):
    tablero = inicializar_tablero()
    movimientos = 0

    # Determinar el turno inicial según el equipo que comienza
    if equipo_inicial == "Círculo":
        turno = 0  # Comienza el equipo Círculo
    else:
        turno = 1  # Comienza el equipo Cruz

    jugadores = [jugador1, jugador2]
    simbolos = ["O", "X"]

    while movimientos < 9:
        mostrar_tablero(tablero, False)
        print(f"Turno de {jugadores[turno][1]} con símbolo {simbolos[turno]}:")

        # Esperar hasta que el jugador realice un movimiento válido
        exito = False
        while not exito:
            exito = realizar_movimiento(tablero, simbolos[turno])  # Llamada al movimiento
            if not exito:
                print("Espacio ocupado. Intenta de nuevo.")  # Mensaje cuando el espacio está ocupado

        # Si el movimiento fue exitoso
        movimientos += 1
        ganador = verificar_ganador(tablero)
        if ganador:
            # Obtener posiciones ganadoras
            posiciones_ganadoras = obtener_posiciones_ganadoras(tablero, ganador)
            mostrar_tablero(tablero, True, ganadores=[ganador], posiciones_ganadoras=posiciones_ganadoras)
            print(f"¡El ganador es {jugadores[turno][1]}! 🎉")
            return jugadores[turno], movimientos
        
        turno = 1 - turno  # Cambiar turno (de Círculo a Cruz, o viceversa)

    # Si se alcanzan 9 movimientos sin ganador, es empate
    print("¡Es un empate! ")
    mostrar_tablero(tablero, es_empate=True)  # Mostrar tablero en gris
    return None, movimientos



# Nombre del módulo: MenuPrincipal
# Descripción: Controla el menú principal del juego y la interacción del usuario.
# Datos de Entrada: Ninguno.
# Datos de Salida: Ninguno.

def menu_principal():
    equipos = None
    dimEquipos = 0
    continuar_juego = True
    i = 0
    while continuar_juego:
        
        print("\n--- Menú Principal ---")
        print("1. Empezar juego (Cargar jugadores)")
        print("2. Mostrar puntajes")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            max_jugadores = input("Ingrese la cantidad de jugadores por equipo (2-10): ")
            
            # Validar si la entrada es un número y está en el rango 2-10
            while not (max_jugadores.isdigit() and 2 <= int(max_jugadores) <= 10):
                print("La cantidad de jugadores debe ser un número entre 2 y 10.")
                max_jugadores = input("Ingrese la cantidad de jugadores por equipo (2-10): ")

            max_jugadores = int(max_jugadores)  # Convertir a entero después de validación

            # Llamada a cargar_equipos 
            equipos = cargar_equipos(max_jugadores)
            dimEquipos = max_jugadores  # El número de jugadores por equipo

            jugadores_circulo = equipos[0]  # Jugadores del Equipo Círculo
            jugadores_cruz = equipos[1]      # Jugadores del Equipo Cruz

            # NUEVO CÓDIGO: para determinar quién comienza
            print("\n--- Lanzamiento de Dado ---")
            input("Presione Enter para lanzar el dado y determinar qué equipo comienza...")
            dado_lanzado = False  # Bandera 
            while not dado_lanzado:
                print("Lanzando dado para el equipo Círculo...")
                resultado_circulo = lanzar_dado()
                print(f"El equipo Círculo sacó un {resultado_circulo}")

                print("Lanzando dado para el equipo Cruz...")
                resultado_cruz = lanzar_dado()
                print(f"El equipo Cruz sacó un {resultado_cruz}")

                # Determina quién comienza según el lanzamiento del dado
                if resultado_circulo > resultado_cruz:
                    print("El equipo Círculo comienza la partida.")
                    equipo_inicial = "Círculo"
                    dado_lanzado = True  
                elif resultado_cruz > resultado_circulo:
                    print("El equipo Cruz comienza la partida.")
                    equipo_inicial = "Cruz"
                    dado_lanzado = True  
                else:
                    print("¡Es un empate! Lanzando nuevamente el dado...")

            # Validar para que no se repitan los jugadores
            jugadores_seleccionados_circulo = []  # Lista para guardar los jugadores seleccionados del equipo Círculo
            jugadores_seleccionados_cruz = []  # Lista para guardar los jugadores seleccionados del equipo Cruz

            # Selección de jugadores en el , según el equipo que comienza
            if equipo_inicial == "Círculo":
                print("El equipo Círculo selecciona primero.")
                jugador_inicial = jugadores_circulo[0]  # El primer jugador del equipo Círculo
                print(f"Jugador seleccionado de Círculo: {jugador_inicial['nombre']} (ID: {jugador_inicial['id']})")

                # Seleccion de los jugadores
                for i in range(max_jugadores):
                    jugador_circulo = elegir_jugador_aleatorio(jugadores_circulo, jugadores_seleccionados_circulo)
                    jugador_cruz = elegir_jugador_aleatorio(jugadores_cruz, jugadores_seleccionados_cruz)
                    print(f"Jugador seleccionado de Círculo: {jugador_circulo['nombre']} (ID: {jugador_circulo['id']})")
                    print(f"Jugador seleccionado de Cruz: {jugador_cruz['nombre']} (ID: {jugador_cruz['id']})")

                    print(f"----------------INICIO DE PARTIDA----------------")
                    empates = 0  # Contador de empates
                    partida_activa = True

                    while partida_activa:
                        ganador, movimientos = jugar_partida(jugador_circulo, jugador_cruz, equipo_inicial)

                        if ganador:
                            actualizar_puntajes(ganador, movimientos, equipos, jugador_circulo, jugador_cruz, empates)
                            partida_activa = False
                        else:
                            actualizar_puntajes(None, movimientos, equipos, jugador_circulo, jugador_cruz, empates)
                            empates += 1
                            if empates >= 3:
                                print("Se han alcanzado 3 empates.")
                                partida_activa = False
            else:
                print("El equipo Cruz selecciona primero.")
                jugador_inicial = jugadores_cruz[0]  # El primer jugador del equipo Cruz
                print(f"Jugador seleccionado de Cruz: {jugador_inicial['nombre']} (ID: {jugador_inicial['id']})")

                # Seleccion de los jugadores
                for i in range(max_jugadores):
                    jugador_cruz = elegir_jugador_aleatorio(jugadores_cruz, jugadores_seleccionados_cruz)
                    jugador_circulo = elegir_jugador_aleatorio(jugadores_circulo, jugadores_seleccionados_circulo)
                    print(f"Jugador seleccionado de Cruz: {jugador_cruz['nombre']} (ID: {jugador_cruz['id']})")
                    print(f"Jugador seleccionado de Círculo: {jugador_circulo['nombre']} (ID: {jugador_circulo['id']})")

                    print(f"----------------INICIO DE PARTIDA----------------")
                    empates = 0  # Contador de empates
                    partida_activa = True

                    while partida_activa:
                        ganador, movimientos = jugar_partida(jugador_circulo, jugador_cruz,equipo_inicial)

                        if ganador:
                            actualizar_puntajes(ganador, movimientos, equipos, jugador_circulo, jugador_cruz, empates)
                            partida_activa = False
                        else:
                            actualizar_puntajes(None, movimientos, equipos, jugador_circulo, jugador_cruz, empates)
                            empates += 1
                            if empates >= 3:
                                print("Se han alcanzado 3 empates.")
                                partida_activa = False

        elif opcion == "2":
            if equipos is not None:
                mostrar_puntajes(equipos, dimEquipos)
            else:
                print("No hay equipos cargados.")

        elif opcion == "3":
            print("Gracias por jugar.")
            continuar_juego = False

        else:
            print("Opción no válida, intente de nuevo.")


# Inicia el juego
menu_principal()