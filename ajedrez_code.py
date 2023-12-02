print("Este es un pequeño juego de ajedrez")
print("Recuerda que las columnas y filas van desde la número 0 hasta la número 7")
"""
Guarda el estado actual del tablero de ajedrez en un archivo de texto, usando un formato donde 
las filas del tablero están separadas por nuevas líneas y las columnas por tabuladores. 
La codificación utf-8 asegura que los carácteres especiales como los símbolos de ajedrez
Se "reconozcan" en el archivo.
"""
def guardar_tablero(tablero, nombre_fichero):
    with open(nombre_fichero, 'a', encoding = "utf-8") as file:
        for fila in tablero:
            file.write('\t'.join(fila) + '\n')

"""
Imprime el tablero de ajedrez por consola en el esado actual, en un formato que lo hace más
legible. Esto es gracias a que  las filas del tablero están separadas por líneas y los elementos 
de cada fila están separados por tabuladores.
"""
def mostrar_tablero(tablero):
    for fila in tablero:
        print('\t'.join(fila))
    print('\n')

"""
 Almacena las coordenadas de una pieza en el tablero (llamada origen) y las coordenadas a las que se moverá 
 esa pieza (llamada destino), realizando el movimiento correspondiente en el tablero.
"""
def realizar_movimiento(tablero, origen_fila, origen_col, destino_fila, destino_col):
    pieza = tablero[origen_fila][origen_col]
    tablero[origen_fila][origen_col] = ' '
    tablero[destino_fila][destino_col] = pieza

# Estas son las piezas de ajedrez en código hexadecimal
pb = "\u2659"
tb = "\u2656"
cb= "\u2658"
ab = "\u2657"
reina_b = "\u2655"
rey_b = "\u2654"

pn= "\u265F"
tn = "\u265C"
cn = "\u265E"
an = "\u265D"
reina_n = "\u265B"
rey_n = "\u265A"
"""
La función main es la que crea el tablero de ajedrez, y guarda los distintos estados del tablero
según los movimientos que se hagan. Además, se llaman a las funciones de guardado del tablero, y de
mostrar el tablero. El bucle while será el encargado de preguntar al usuario donde quiere mover cada pieza
y repetir el proceso (por eso es un bucle)
"""
def main():
    nombre_fichero = input("Introduce el nombre del fichero para guardar la partida: ")
    tablero_inicial = [
        [tb, cb, ab, reina_b, rey_b, ab, cb, tb],
        [pb] * 8,
        [' '] * 8,
        [' '] * 8,
        [' '] * 8,
        [' '] * 8 , 
        [pn] * 8,
        [tn, cn, an, reina_n, rey_n, an, cn, tn],
    ]

    guardar_tablero(tablero_inicial, nombre_fichero)
    mostrar_tablero(tablero_inicial)

    """
     Este bucle pregunta por un movimiento, si la respuesta es distinta a s, se termina el juego.
     En caso de seguir jugando, pregunta la ficha que quieres mover según su posición (preguntando 
     fila y columna), y luego hace lo mismo, para preguntar al jugador donde quiere poner esa pieza.
     Por último, se llaman a las 3 funciones definidas anteriormente en bucle, para que se vaya guardando 
     cada movimiento que haga el usuario, y vaya mostrando el estado del tablero en el archivo creado
     hasta que se interrumpa el bucle (con una respuesta distinta a la s de "sí")
    """
    while True:
        opcion = input("¿Quieres hacer un movimiento? (s/n): ").lower()

        if opcion != 's':
            break

        origen_fila = int(input("Introduce la fila de la pieza que quieres mover: "))
        origen_col = int(input("Introduce la columna de la pieza que quieres mover: "))
        destino_fila = int(input("Introduce la fila a la que quieres mover la pieza: "))
        destino_col = int(input("Introduce la columna a la que quieres mover la pieza: "))

        realizar_movimiento(tablero_inicial, origen_fila, origen_col, destino_fila, destino_col)
        guardar_tablero(tablero_inicial, nombre_fichero)
        mostrar_tablero(tablero_inicial)

"""
Esto, verifica si el script se está ejecutando directamente o está siendo importado desde otro módulo.
En caso de estar ejecutandose el script directamente, se cumpliría la condición, por tanto se llama a la 
función "main()" definida anteriormente. 
"""
if __name__ == "__main__":
    main()
