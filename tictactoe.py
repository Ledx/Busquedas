# Resolucion del juego tic tac toe usando minimax
# Para interactuar con el juego basta con manipular el tablero definido en la linea 115,
# se puede dejar como esta o poner x, o en algunas posiciones para ver como terminaria el juego.

def quedanJugadas(tablero):
    # Funcion para determinar si quedan jugadas posibles en el tablero
    for i in range(3):
        for j in range(3):
            if (tablero[i][j] == '_'):
                return True
    return False


def evaluar(b):
    # Funcion de evaluacion
    # Revisando las filas vecinas
    for fila in range(3):
        if (b[fila][0] == b[fila][1] and b[fila][1] == b[fila][2]):
            if (b[fila][0] == jugador):
                return 10
            elif (b[fila][0] == oponente):
                return -10

    # Revisando las columnas vecinas
    for col in range(3):

        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

            if (b[0][col] == jugador):
                return 10
            elif (b[0][col] == oponente):
                return -10

    # Revisando las diagonales
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

        if (b[0][0] == jugador):
            return 10
        elif (b[0][0] == oponente):
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

        if (b[0][2] == jugador):
            return 10
        elif (b[0][2] == oponente):
            return -10

    # Si no hay posibilidad de victoria proxima, se devuelve 0
    return 0



def minimax(tablero, profundidad, es_maximo, ju, op):
    # Funcion minimax, valua el tablero
    puntaje = evaluar(tablero)

    if (puntaje == 10):
        return puntaje

    if (puntaje == -10):
        return puntaje

    if (quedanJugadas(tablero) == False):
        return 0

    if (es_maximo):
        mejor = -1000

        for i in range(3):
            for j in range(3):

                if (tablero[i][j] == '_'):
                    tablero[i][j] = ju
                    mejor = max(mejor, minimax(tablero,profundidad + 1, not es_maximo,ju,op))
                    tablero[i][j] = '_'
        return mejor

    else:
        mejor = 1000

        for i in range(3):
            for j in range(3):
                if (tablero[i][j] == '_'):
                    tablero[i][j] = op
                    mejor = min(mejor, minimax(tablero, profundidad + 1, not es_maximo,ju,op))
                    tablero[i][j] = '_'
        return mejor


def mejorMovimiento(tablero,ju,op):
    # Devuelve la mejor jugada posible

    mejor_valor = -1000
    mejor_movimiento = (-1, -1)

    for i in range(3):
        for j in range(3):
            if (tablero[i][j] == '_'):
                tablero[i][j] = ju
                valor_movimiento = minimax(tablero, 0, False,ju,op)
                tablero[i][j] = '_'

                if (valor_movimiento > mejor_valor):
                    mejor_movimiento = (i, j)
                    mejor_valor = valor_movimiento

    print("El valor del mejor movimiento es :", mejor_valor)
    return mejor_movimiento


# Tablero del juego
# x representa al jugador humano, o a la maquina y _ representa una casilla aun no seleccionada

tablero = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

jugador, oponente = 'x', 'o'
while (quedanJugadas(tablero)):
    mejor_movimiento = mejorMovimiento(tablero, jugador, oponente)
    tablero[mejor_movimiento[0]][mejor_movimiento[1]] = jugador

    print("La jugada optima para el oponente es :", end=" ")
    print(mejor_movimiento[0],",", mejor_movimiento[1])

    mejor_movimiento = mejorMovimiento(tablero, oponente, jugador)
    tablero[mejor_movimiento[0]][mejor_movimiento[1]] = oponente

    print("La jugada optima el jugador es :", end=" ")
    print(mejor_movimiento[0],",", mejor_movimiento[1])

print("El tablero es :")
for i in range(3):
    print()
    for j in range(3):
        print(tablero[i][j], end=" ")

