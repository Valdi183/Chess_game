import pygame 
import sys

pygame.init()

# Configuración del tablero
TILE_SIZE = 80
BOARD_SIZE = 8
SCREEN_SIZE = TILE_SIZE * BOARD_SIZE

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Creación de la pantalla
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Ajedrez con Pygame")

# Cargar imágenes de las piezas
pieces = {}
pieces['wp'] = pygame.image.load('images/wp.png')  # ejemplo, debes tener tus propias imágenes
pieces['bp'] = pygame.image.load('images/bp.png')  # ejemplo, debes tener tus propias imágenes

# Función para dibujar el tablero
def draw_board():
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            color = WHITE if (x + y) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Función para dibujar las piezas
def draw_pieces(board):
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            piece = board[y][x]
            if piece:
                screen.blit(pieces[piece], (x * TILE_SIZE, y * TILE_SIZE))

# Tablero inicial
board = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_board()
    draw_pieces(board)
    
    pygame.display.flip()