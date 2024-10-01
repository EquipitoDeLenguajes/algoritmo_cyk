# algoritmo_cyk

Este proyecto implementa el algoritmo CYK (Cocke-Younger-Kasami) para analizar cadenas en una gramática en Forma Normal de Chomsky (CNF).

## Características
- **Evaluación de gramáticas en CNF**: El script analiza si una cadena pertenece al lenguaje generado por una gramática en CNF.
- **Generación de cadenas aleatorias**: Evalúa la complejidad temporal del algoritmo generando cadenas de longitud creciente.
- **Análisis de producciones unarias y binarias**: Soporta producciones unarias y binarias en la gramática.
- **Visualización de complejidad temporal**: Muestra una gráfica de la relación entre la longitud de la cadena y el tiempo de ejecución.
- **Lectura de gramática desde un archivo**: Carga una gramática CNF desde un archivo.

## Pre-requisitos

Debes contar con la instalación de la librería de `matplotlib` ya sea en un entorno virtual o de forma global en tu computadora.

Para instalar `matplotlib` con `pip`:

```sh
$ pip install matplotlib
```

## Cómo usar

### Paso 1: Crear un archivo con la gramática en CNF

El archivo `gramatica.txt` debe seguir el formato:

```
S -> A B A | a B | b
```

Donde las producciones están en la Forma Normal de Chomsky.

### Paso 2: Ejecuta el script `algoritmo_cyk.py` para analizar una cadena:

```sh
$ python3 algoritmo_cyk.py gramatica.txt [cadena]
```

Por ejemplo:

```
$ python3 algoritmo_cyk.py gramatica.txt ab
```

### Paso 3: Interpretar la salida
El script realizará el análisis de la cadena y mostrará si la cadena es aceptada o rechazada por la gramática.

Si el archivo `gramatica.txt` contiene:

```
S -> A B | A | B
A -> a
B -> b
```

Y ejecutamos:

```sh
$ python3 algoritmo_cyk.py gramatica.txt ab
```

El resultado será:

```sh
Resultado: Accepted
```

## Evaluación de la complejidad temporal

También puedes ejecutar el análisis de complejidad temporal generando cadenas aleatorias y midiendo los tiempos de ejecución. Para esto debes modificar la parte del llamado del script `algoritmo_cyk.py` que se encuentra al final del contenido del mismo. Comenta el llamado de la función main del archivo y elimina el comentario de la función de evaluar la complejidad temporal, quedando de la siguiente forma:

```py
if __name__ == "__main__":
    # main()
    evaluar_complejidad_temporal()
```

Luego ejecuta desde la terminal el script:

```sh
$ python3 algoritmo_cyk.py
```

Esto generará una gráfica que muestra la relación entre la longitud de la cadena y el tiempo de ejecución del algoritmo CYK como la siguiente:

<p align="center">
  <img src="https://github.com/user-attachments/assets/10faf446-215d-4699-9c30-54197e72e16c" alt="CYK_analisis_temporal">
</p>

En caso de que desees volver a utilizar tu propia palabra y analizarla con CYK elimina el comentario de el método main y comenta el método de evaluar la complejidad temporal:

```py

if __name__ == "__main__":
    main()
    # evaluar_complejidad_temporal()
```

## Autores
- Santiago Garzón
- Mateo Fonseca
- Karol Guerrero
- Sebastián Barros
