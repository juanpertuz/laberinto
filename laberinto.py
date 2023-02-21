muros = (
    (0, 0), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
    (1, 0), (1, 2), (1, 8), (1, 5), (1, 6), (1, 8),
    (2, 0), (2, 4), (2, 8),
    (3, 0), (3, 2), (3, 3), (3, 4), (3, 6), (3, 8),
    (4, 0), (4, 2), (4, 6), (4, 8),
    (5, 0), (5, 4), (5, 6), (5, 8),
    (6, 0), (6, 2), (6, 3), (6, 4), (6, 6), (6, 8),
    (7, 0), (7, 4), (7, 6), (7, 8),
    (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 8)
)


def laberintos(tamaño, muros):
    laberinto = []
    for x in range(tamaño):
        fila = []
        for y in range(tamaño):
            if tuple((x, y)) in muros:
                fila.append('x')
            else:
                fila.append(' ')
        laberinto.append(fila)
    for fila in laberinto:
        print(fila)


laberintos(9, muros)
