print("Este es un pequeño juego de ajedrez")
print("Recuerda que las columnas y filas van desde la número 0 hasta la número 7")

# Estas son las piezas de ajedrez en código hexadecimal
pb = "\u2659"
tb = "\u2656"
cb = "\u2658"
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
Este archivo, tiene una pequeña diferencia con el del archivo "ajedrez_code.py" y es que este código,
está organizado en una clase. Esto simplemente cambia un poco la estructura del código. Algunos cambios
significativos, son la forma en la que llamamos a las funciones, ya que al pertenecer a una clase, se 
combierten en métodos de esa clase, y estas tienen acceso a los atributos que se definen en la clase
gracias a "self". para entender mejor lo que hace, podríamos resumirlo en que "self" es simplemente 
una convención utilizada para referirse al objeto dentro de la clase.

Realmente, en este caso, no es algo fundamental utilizar una clase para estructurar bien el código. 
Simplemente con tener funciones cuyos nombres ayuden al lector del código a entender bien la estructura
de este, y que ayude también a optimizar el código
"""
class JuegoAjedrez:
    def __init__(self):
        self.tablero = [
        [tb, cb, ab, reina_b, rey_b, ab, cb, tb],
        [pb] * 8,
        [' '] * 8,
        [' '] * 8,
        [' '] * 8,
        [' '] * 8 , 
        [pn] * 8,
        [tn, cn, an, reina_n, rey_n, an, cn, tn],
    ]

    def guardar_tablero(self, nombre_fichero):
        with open(nombre_fichero, 'a', encoding="utf-8") as file:
            for fila in self.tablero:
                file.write('\t'.join(fila) + '\n')

    def mostrar_tablero(self):
        for fila in self.tablero:
            print('\t'.join(fila))
        print('\n')

    def realizar_movimiento(self, origen_fila, origen_col, destino_fila, destino_col):
        pieza = self.tablero[origen_fila][origen_col]
        self.tablero[origen_fila][origen_col] = ' '
        self.tablero[destino_fila][destino_col] = pieza

    def jugar(self):
        nombre_fichero = input("Introduce el nombre del fichero para guardar la partida: ")
        self.guardar_tablero(nombre_fichero)
        self.mostrar_tablero()

        while True:
            opcion = input("¿Quieres hacer un movimiento? (s/n): ").lower()

            if opcion != 's':
                break

            origen_fila = int(input("Introduce la fila de la pieza que quieres mover: "))
            origen_col = int(input("Introduce la columna de la pieza que quieres mover: "))
            destino_fila = int(input("Introduce la fila a la que quieres mover la pieza: "))
            destino_col = int(input("Introduce la columna a la que quieres mover la pieza: "))

            self.realizar_movimiento(origen_fila, origen_col, destino_fila, destino_col)
            self.guardar_tablero(nombre_fichero)
            self.mostrar_tablero()


if __name__ == "__main__":
    juego = JuegoAjedrez()
    juego.jugar()