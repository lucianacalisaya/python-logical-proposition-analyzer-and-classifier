"""Analizador y Clasificador de Proposiciones Compuestas mediante Tablas de Verdad.

Conceptos utilizados: álgebra de Boole, sistemas numéricos (decimal a binario),
estructuras secuenciales, condicionales, repetitivas, listas y funciones.
"""


# ---------------------------------------------------------------------------
# OPERADORES LÓGICOS (álgebra de Boole)
# ---------------------------------------------------------------------------
def operador_not(p):
    """Calcula la negación lógica de una variable de verdad (0 o 1).

    Args:
        p (int): Valor binario (1 o 0).

    Returns:
        int: 1 si p es 0, o 0 si p es 1.
    """
    if p == 1:
        return 0
    else:
        return 1


def operador_and(p, q):
    """Calcula la conjunción lógica entre dos variables binarias.

    Args:
        p (int): Primer valor (0 o 1).
        q (int): Segundo valor (0 o 1).

    Returns:
        int: 1 si ambos son 1, 0 en caso contrario.
    """
    if p == 1 and q == 1:
        return 1
    else:
        return 0


def operador_or(p, q):
    """Calcula la disyunción lógica entre dos variables binarias.

    Args:
        p (int): Primer valor (0 o 1).
        q (int): Segundo valor (0 o 1).

    Returns:
        int: 0 si ambos son 0, 1 en caso contrario.
    """
    if p == 0 and q == 0:
        return 0
    else:
        return 1


def operador_condicional(p, q):
    """Calcula la implicación lógica (p → q).

    Args:
        p (int): Antecedente (0 o 1).
        q (int): Consecuente (0 o 1).

    Returns:
        int: 0 si p es 1 y q es 0, 1 en cualquier otro caso.
    """
    if p == 1 and q == 0:
        return 0
    else:
        return 1


def operador_bicondicional(p, q):
    """Calcula la doble implicación lógica (p ↔ q).

    Args:
        p (int): Primer valor (0 o 1).
        q (int): Segundo valor (0 o 1).

    Returns:
        int: 1 si p y q son iguales, 0 si son distintos.
    """
    if p == q:
        return 1
    else:
        return 0


# ---------------------------------------------------------------------------
# SISTEMAS NUMÉRICOS: generación de combinaciones
# ---------------------------------------------------------------------------
def decimal_a_binario(numero, cantidad_bits):
    """Convierte un número decimal a binario mediante divisiones sucesivas.

    Args:
        numero (int): Número decimal entero mayor o igual a 0.
        cantidad_bits (int): Cantidad de bits que debe tener el resultado
            (se rellena con ceros a la izquierda).

    Returns:
        list: Lista de bits, por ejemplo decimal_a_binario(2, 3) -> [0, 1, 0].
    """
    bits = []
    while numero > 0:
        residuo = numero % 2
        bits.insert(0, residuo)
        numero = numero // 2

    while len(bits) < cantidad_bits:
        bits.insert(0, 0)

    return bits


def generar_combinaciones(cantidad_variables):
    """Genera todas las combinaciones binarias para n variables.

    Cuenta desde 2^n - 1 hasta 0 y convierte cada número a binario, de modo
    que la primera fila sea todo 1 y la última todo 0 (orden usual en clase).

    Args:
        cantidad_variables (int): Número de variables (1, 2, 3, ...).

    Returns:
        list: Lista de listas de bits. Para 2 variables:
            [[1,1], [1,0], [0,1], [0,0]].
    """
    total_filas = 1
    for _ in range(cantidad_variables):
        total_filas = total_filas * 2

    combinaciones = []
    for numero in range(total_filas - 1, -1, -1):
        combinaciones.append(decimal_a_binario(numero, cantidad_variables))

    return combinaciones


# ---------------------------------------------------------------------------
# CLASIFICACIÓN Y PRESENTACIÓN
# ---------------------------------------------------------------------------
def clasificar_resultados(columna_final):
    """Clasifica la última columna de una tabla de verdad.

    Args:
        columna_final (list): Resultados binarios de la última columna.

    Returns:
        str: "TAUTOLOGÍA", "CONTRADICCIÓN" o "CONTINGENCIA".
    """
    if len(columna_final) == 0:
        return "SIN RESULTADOS"
    
    cantidad_unos = 0
    total_filas = len(columna_final)

    for resultado in columna_final:
        if resultado == 1:
            cantidad_unos = cantidad_unos + 1

    if cantidad_unos == total_filas:
        return "TAUTOLOGÍA"
    elif cantidad_unos == 0:
        return "CONTRADICCIÓN"
    else:
        return "CONTINGENCIA"


def formatear_fila(valores, anchos):
    """Construye una línea de texto con las columnas centradas y alineadas.

    Args:
        valores (list): Elementos (números o textos) de la fila.
        anchos (list): Ancho de cada columna.

    Returns:
        str: Línea lista para imprimir, con columnas separadas por "|".
    """
    linea = ""
    for i in range(len(valores)):
        texto = str(valores[i])
        linea = linea + texto.center(anchos[i])
        if i < len(valores) - 1:
            linea = linea + "|"
    return linea


def imprimir_tabla(encabezados, filas):
    """Imprime los encabezados y las filas de una tabla, alineados en columnas.

    Args:
        encabezados (list): Nombres de las columnas.
        filas (list): Lista de filas con los valores (0 o 1) de cada columna.
    """
    anchos = []
    for encabezado in encabezados:
        anchos.append(len(encabezado) + 2)

    linea_encabezado = formatear_fila(encabezados, anchos)
    separador = "-" * len(linea_encabezado)

    print(linea_encabezado)
    print(separador)
    for fila in filas:
        print(formatear_fila(fila, anchos))
    print(separador)


def mostrar_tabla(titulo, encabezados, filas):
    """Imprime la tabla de verdad completa y su clasificación.

    Args:
        titulo (str): Proposición que se está analizando.
        encabezados (list): Nombres de las columnas (variables y pasos).
        filas (list): Lista de filas; la última columna es el resultado final.
    """
    print("\n--- ANALIZANDO: " + titulo + " ---")
    imprimir_tabla(encabezados, filas)

    columna_final = []
    for fila in filas:
        columna_final.append(fila[len(fila) - 1])

    print("Resultado de la clasificación: " + clasificar_resultados(columna_final))
    print()


# ---------------------------------------------------------------------------
# PROPOSICIONES PREDEFINIDAS (una de cada tipo + el ejemplo a demostrar)
# ---------------------------------------------------------------------------
def analizar_modus_ponens():
    """Analiza la proposición [(p → q) ∧ p] → q (Modus Ponens)."""
    encabezados = ["p", "q", "p → q", "(p → q) ∧ p", "[(p → q) ∧ p] → q"]
    filas = []

    for combinacion in generar_combinaciones(2):
        p = combinacion[0]
        q = combinacion[1]

        paso1 = operador_condicional(p, q)
        paso2 = operador_and(paso1, p)
        resultado = operador_condicional(paso2, q)

        filas.append([p, q, paso1, paso2, resultado])

    mostrar_tabla("[(p → q) ∧ p] → q", encabezados, filas)


def analizar_tautologia():
    """Analiza la ley de De Morgan: ¬(p ∧ q) ↔ (¬p ∨ ¬q)."""
    encabezados = ["p", "q", "p ∧ q", "¬(p ∧ q)", "¬p ∨ ¬q",
                   "¬(p ∧ q) ↔ (¬p ∨ ¬q)"]
    filas = []

    for combinacion in generar_combinaciones(2):
        p = combinacion[0]
        q = combinacion[1]

        paso1 = operador_and(p, q)
        paso2 = operador_not(paso1)
        paso3 = operador_or(operador_not(p), operador_not(q))
        resultado = operador_bicondicional(paso2, paso3)

        filas.append([p, q, paso1, paso2, paso3, resultado])

    mostrar_tabla("¬(p ∧ q) ↔ (¬p ∨ ¬q)", encabezados, filas)


def analizar_contradiccion():
    """Analiza la proposición p ∧ ¬p (principio de no contradicción)."""
    encabezados = ["p", "¬p", "p ∧ ¬p"]
    filas = []

    for combinacion in generar_combinaciones(1):
        p = combinacion[0]

        paso1 = operador_not(p)
        resultado = operador_and(p, paso1)

        filas.append([p, paso1, resultado])

    mostrar_tabla("p ∧ ¬p", encabezados, filas)


def analizar_contingencia():
    """Analiza la proposición (p ∨ q) ∧ ¬p."""
    encabezados = ["p", "q", "p ∨ q", "¬p", "(p ∨ q) ∧ ¬p"]
    filas = []

    for combinacion in generar_combinaciones(2):
        p = combinacion[0]
        q = combinacion[1]

        paso1 = operador_or(p, q)
        paso2 = operador_not(p)
        resultado = operador_and(paso1, paso2)

        filas.append([p, q, paso1, paso2, resultado])

    mostrar_tabla("(p ∨ q) ∧ ¬p", encabezados, filas)


# ---------------------------------------------------------------------------
# PROPOSICIÓN PERSONALIZADA: construcción paso a paso
# ---------------------------------------------------------------------------
def aplicar_operador(codigo, a, b):
    """Aplica al par (a, b) el operador binario elegido por el usuario.

    Args:
        codigo (int): 1 = ∧, 2 = ∨, 3 = →, 4 = ↔.
        a (int): Primer valor (0 o 1).
        b (int): Segundo valor (0 o 1).

    Returns:
        int: Resultado (0 o 1) de aplicar el operador.
    """
    if codigo == 1:
        return operador_and(a, b)
    elif codigo == 2:
        return operador_or(a, b)
    elif codigo == 3:
        return operador_condicional(a, b)
    else:
        return operador_bicondicional(a, b)


def pedir_numero(mensaje, minimo, maximo):
    """Solicita un número entero en un rango y repite hasta que sea válido.

    Args:
        mensaje (str): Texto que se muestra al pedir el dato.
        minimo (int): Menor valor permitido.
        maximo (int): Mayor valor permitido.

    Returns:
        int: Número ingresado por el usuario, dentro del rango.
    """
    validos = []
    for numero in range(minimo, maximo + 1):
        validos.append(str(numero))

    entrada = input(mensaje)
    while entrada not in validos:
        print("Opción no válida. Ingrese un número entre "
              + str(minimo) + " y " + str(maximo) + ".")
        entrada = input(mensaje)

    return int(entrada)


def armar_filas(columnas):
    """Convierte una lista de columnas en una lista de filas.

    Args:
        columnas (list): Lista de columnas; cada columna es una lista de 0 y 1.

    Returns:
        list: Lista de filas; la fila i contiene el elemento i de cada columna.
    """
    filas = []
    for i in range(len(columnas[0])):
        fila = []
        for columna in columnas:
            fila.append(columna[i])
        filas.append(fila)
    return filas


def construir_columna(codigo, nombres, columnas):
    """Crea una nueva columna combinando columnas ya existentes.

    Args:
        codigo (int): Operación elegida: 1 = ¬, 2 = ∧, 3 = ∨,
            4 = condicional, 5 = bicondicional.
        nombres (list): Nombres de las columnas disponibles.
        columnas (list): Valores (0 o 1) de cada columna disponible.

    Returns:
        list: [nombre_nuevo, columna_nueva, usados] con el texto de la
            operación, sus resultados fila por fila y la lista de posiciones
            de las columnas que se utilizaron como operandos.
    """
    simbolos = ["∧", "∨", "→", "↔"]
    total = len(nombres)

    a = pedir_numero("Primer operando (número de columna): ", 1, total) - 1
    columna_nueva = []

    if codigo == 1:
        nombre_nuevo = "¬" + nombres[a]
        for i in range(len(columnas[a])):
            columna_nueva.append(operador_not(columnas[a][i]))
        usados = [a]
    else:
        b = pedir_numero("Segundo operando (número de columna): ", 1, total) - 1
        nombre_nuevo = "(" + nombres[a] + " " + simbolos[codigo - 2] + " " + nombres[b] + ")"
        for i in range(len(columnas[a])):
            columna_nueva.append(aplicar_operador(codigo - 1, columnas[a][i], columnas[b][i]))
        usados = [a, b]

    return [nombre_nuevo, columna_nueva, usados]


def analizar_personalizada():
    """Permite construir cualquier proposición de 2 a 4 variables paso a paso.

    El usuario crea columnas nuevas combinando variables o resultados
    anteriores. La proposición final es la última columna creada y solo
    se puede terminar cuando todas las demás columnas fueron utilizadas.
    """
    letras = ["p", "q", "r", "s"]

    print("\nConstructor de proposiciones personalizadas")
    print("Construya su proposición paso a paso.")
    print("Cada operación crea una nueva columna.")
    print("Use el número de columna para elegir los operandos.")
    print("La última columna será la proposición analizada.")
    cantidad = pedir_numero("¿Cuántas variables usará? (2-4): ", 2, 4)
    combinaciones = generar_combinaciones(cantidad)

    nombres = []
    columnas = []
    usadas = []
    for j in range(cantidad):
        nombres.append(letras[j])
        usadas.append(0)
        columna = []
        for fila in combinaciones:
            columna.append(fila[j])
        columnas.append(columna)

    terminado = False
    while not terminado:
        encabezados_numerados = []
        for i in range(len(nombres)):
            encabezados_numerados.append("[" + str(i + 1) + "] " + nombres[i])

        print("\nTabla actual:")
        imprimir_tabla(encabezados_numerados, armar_filas(columnas))

        print("Operaciones disponibles:")
        print("  1. ¬  (negación)")
        print("  2. ∧  (conjunción)")
        print("  3. ∨  (disyunción)")
        print("  4. →  (condicional)")
        print("  5. ↔  (bicondicional)")
        print("  6. Terminar (la proposición final es la última columna)")
        codigo = pedir_numero("Operación (1-6): ", 1, 6)

        if codigo == 6:
            if len(nombres) == cantidad:
                print("Debe crear al menos una operación antes de terminar.")
            else:
                pendientes = []
                for i in range(len(nombres) - 1):
                    if usadas[i] == 0:
                        pendientes.append("[" + str(i + 1) + "] " + nombres[i])

                if len(pendientes) == 0:
                    terminado = True
                else:
                    print("No puede terminar: hay columnas sin usar en la proposición final:")
                    for texto in pendientes:
                        print("  " + texto)
                    print("Inclúyalas con una operación (∧, ∨, →, ↔).")
        else:
            nueva = construir_columna(codigo, nombres, columnas)
            for posicion in nueva[2]:
                usadas[posicion] = 1
            nombres.append(nueva[0])
            columnas.append(nueva[1])
            usadas.append(0)
            print("Se creó la columna: " + nueva[0])

    mostrar_tabla(nombres[len(nombres) - 1], nombres, armar_filas(columnas))


# ---------------------------------------------------------------------------
# MENÚ PRINCIPAL
# ---------------------------------------------------------------------------
def ejecutar_menu_principal():
    """Mantiene activo el programa mediante un bucle while e interactúa
    con el usuario mediante condicionales.
    """
    opcion = ""
    while opcion != "6":
        print("==================================================")
        print("  ANALIZADOR Y CLASIFICADOR DE TABLAS DE VERDAD   ")
        print("==================================================")
        print("Valores de verdad: 1 = Verdadero, 0 = Falso")
        print("1. [(p → q) ∧ p] → q       (Modus Ponens)")
        print("2. ¬(p ∧ q) ↔ (¬p ∨ ¬q)    (Tautología)")
        print("3. p ∧ ¬p                  (Contradicción)")
        print("4. (p ∨ q) ∧ ¬p            (Contingencia)")
        print("5. Proposición personalizada (2 a 4 variables)")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            analizar_modus_ponens()
        elif opcion == "2":
            analizar_tautologia()
        elif opcion == "3":
            analizar_contradiccion()
        elif opcion == "4":
            analizar_contingencia()
        elif opcion == "5":
            analizar_personalizada()
        elif opcion == "6":
            print("Gracias por utilizar el analizador. ¡Hasta luego!")
        else:
            print("Opción no válida. Ingrese un número del 1 al 6.\n")


# Punto de entrada principal
if __name__ == "__main__":
    ejecutar_menu_principal()