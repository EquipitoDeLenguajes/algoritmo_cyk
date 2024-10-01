import sys
import time
import random
import matplotlib.pyplot as plt

P = []
G = {"P": {}, "S": ""}
strings = []


def evaluar_complejidad_temporal():
    tiempos = []
    longitudes = []
    cadena = ""

    # Generar cadenas de longitud creciente entre 'a' y 'b'
    for longitud in range(1, 200):
        cadena = "".join(random.choice("ab") for _ in range(longitud))
        longitudes.append(longitud)

        # Medir el tiempo de ejecución del algoritmo CYK
        start_time = time.time()
        CYK(G, cadena)  # Suponiendo que G está definido correctamente
        end_time = time.time()

        tiempo = end_time - start_time
        tiempos.append(tiempo)

        print(
            f"Longitud: {longitud + 1}, Tiempo de ejecución: {tiempo:.6f} segundos"
        )

    # Generar la gráfica de tiempos de ejecución
    plt.plot(longitudes, tiempos, marker="o")
    plt.xlabel("Longitud de la cadena")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Complejidad Temporal del Algoritmo CYK")
    plt.grid(True)
    plt.show()


def read_grammar_from_file(file_path):
    """
    Lee la gramática desde un archivo y la formatea en CNF.
    """
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if "->" in line:
                # Separar la producción en lado izquierdo y lado derecho
                left, right = line.split("->")
                left = left.strip()
                # Las producciones pueden estar separadas por '|'
                right = [r.strip().split() for r in right.split("|")]
                for r in right:
                    P.append(
                        [left] + r
                    )  # Agregar las producciones a P como lista
            else:
                # Si no es una producción, es una cadena a analizar
                strings.append(line.strip())

    # Imprimir la gramática leída
    print("Gramática leída:")
    for production in P:
        print(production)


def CYK(G, x):
    """
    Algoritmo CYK para verificar si la cadena x pertenece al lenguaje.
    Devuelve una matriz que representa la tabla CYK.
    """
    n = len(x)
    T = [[[] for _ in range(n)] for _ in range(n)]

    # Imprimir la cadena a analizar
    print(f"\nAnalizando la cadena: {x}")

    # Fase 1: Inicialización de la diagonal (producciones unarias)
    for i in range(n):
        for key, values in G["P"].items():
            for value in values:
                if len(value) == 1 and value[0] == x[i]:  # Producción unaria
                    T[i][i].append(key)
                    print(
                        f"Producción unaria encontrada para '{x[i]}': {key} -> {value[0]}"
                    )

    # Imprimir la tabla después de inicializar la diagonal
    print("\nTabla después de la fase 1 (inicialización de la diagonal):")
    for row in T:
        print(row)

    # Fase 2: Rellenar la tabla usando las producciones binarias
    for l in range(2, n + 1):  # Longitud de los substrings
        for i in range(n - l + 1):  # Inicio del substring
            j = i + l - 1  # Fin del substring
            for k in range(i, j):  # Punto de división
                for key, values in G["P"].items():
                    for value in values:
                        if len(value) == 2:  # Producciones binarias
                            B, C = value
                            if B in T[i][k] and C in T[k + 1][j]:
                                T[i][j].append(key)
                                print(
                                    f"Producción binaria encontrada: {key} -> {B} {C}, en T[{i}][{j}]"
                                )

    # Imprimir la tabla final después de aplicar CYK
    print("\nTabla final después de la fase 2:")
    for row in T:
        print(row)

    # Verificar si S está en la celda [0][n-1]
    # También verificamos producciones unarias adicionales después de la tabla
    if G["S"] in T[0][-1]:
        return True
    else:
        # Aquí añadimos una verificación adicional para producciones unarias al final
        for key, values in G["P"].items():
            for value in values:
                if len(value) == 1 and value[0] in T[0][-1]:
                    if key == G["S"]:
                        return True
        return False


def main():
    if len(sys.argv) < 3:
        print("Uso: python3 algoritmo_cyk.py gramatica.txt cadena")
        sys.exit(1)

    grammar_file = sys.argv[1]
    string = sys.argv[2]

    read_grammar_from_file(grammar_file)

    # Definir el símbolo inicial de la gramática
    G["S"] = P[0][0]

    # Añadir las producciones a la gramática G
    for p in P:
        if p[0] not in G["P"]:
            G["P"][p[0]] = []
        G["P"][p[0]].append(p[1:])

    # Imprimir la gramática almacenada
    print("\nGramática almacenada en el diccionario G:")
    print(G)

    # Medir el tiempo de ejecución del algoritmo CYK
    start_time = time.time()
    result = CYK(G, string)
    end_time = time.time()

    # Mostrar si la cadena es aceptada o no
    if result:
        print("\nResultado: Accepted")
    else:
        print("\nResultado: Rejected")

    # Medir y mostrar la complejidad temporal
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time:.6f} segundos")


if __name__ == "__main__":
    main()
    # evaluar_complejidad_temporal()
