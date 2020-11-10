from collections import deque
from node import Node, find_child
# Práctica #02-A - Anchura
# ¿Cómo salgo del Laberinto?


def verify_positive(x, y):
    return (lambda x, y: x >= 0 and y >= 0)(x, y)


def move(direccion, nodo_actual, lab):
    """Funcion para moverse en el plano
    Arriba, Derecha, Abajo, Izquierda
    """
    direcciones = {'U': [-1, 0], 'R': [0, 1], 'D': [1, 0], 'L': [0, -1]}

    direction = direcciones[direccion]
    try:
        # Coordenadas que se generan si se mueva arriba
        coordenadas = (nodo_actual[0]+direction[0],
                       nodo_actual[1] + direction[1])

        if not verify_positive(coordenadas[0], coordenadas[1]):
            return None, coordenadas, direccion

        contenido = lab[coordenadas[0]][coordenadas[1]]

        if contenido == '#':
            return None, coordenadas, direccion
        elif contenido == '.':
            return coordenadas, coordenadas, direccion
        elif contenido == 'D':
            return coordenadas, coordenadas, direccion
        else:
            return None, coordenadas, direccion

    except IndexError:
        # print('error: Index error')
        return None, None, ''


def oposite(direction):
    if direction == 'D':
        return 'U'
    elif direction == 'U':
        return 'D'
    elif direction == 'L':
        return 'R'
    elif direction == 'R':
        return 'L'


def explorar_nodo(nodo_actual, frontera, memoria, laberinto):
    """ Tomando como referencia al nodo actual,
    explora a los nodos visitables desde ahí """

    relations = list()

    for d in ['U', 'R', 'D', 'L'][::-1]:
        new_node, coord, direction = move(d, nodo_actual, laberinto)
        # print(new_node)
        if not oposite(direction) == d:
            if coord and (new_node not in memoria):
                memoria.append(coord)
                if new_node:
                    frontera.append(new_node)
                    relations.append(Node(new_node, parent=nodo_actual,
                                     direction=direction))

    return frontera, memoria, relations


def ver_caminos(target, path):
    # print(path)
    path_string = ''
    current = None

    for p in path:
        if p.child == target:
            current = p
            break
        # print(p.child, p.parent, p.direction)

    # print('Current', current)
    while current.parent != None:
        path_string = f'{path_string}{current.direction}'
        current = find_child(child=current.parent, nodes=path)

    return path_string[::-1]


def verificar_caminos(paths):
    """
    Funcion para generar el camino correcto y más corto
    """
    paths = dict(paths)
    total = (len(paths))
    empties = []

    for k, v in paths.items():
        print(k, v)

    for k, v in paths.items():
        if v == dict():
            empties.append(k)

    while empties:
        for k, v in paths.items():
            for e in empties:
                if e in v:
                    del paths[k][e]
        for e in empties:
            del paths[e]

        empties = []

        for k, v in paths.items():
            if v == dict():
                empties.append(k)

    result = []
    for p in paths.values():
        for v in p.values():
            result.append(tuple(v)[0])

    print('----------------')

    for k, v in paths.items():
        print(k, v)

    return ''.join(result), total


def buscar_salida(lab, origin, destiny):
    """
    Return solution_path, number_visited_nodes
    """
    paths = list()
    origin = origin[0]-1, origin[1]-1
    destiny = destiny[0]-1, destiny[1]-1

    frontera = deque()
    memoria = deque()
    explorados = set()

    frontera.append(origin)
    memoria.append(origin)
    # print('Buscando salida...')
    # print('Frontera: ', frontera)

    paths.append(Node(origin, parent=None))
    
    while frontera:
        # print(frontera)
        nodo_actual = frontera.pop()
        # print('Frontera: ', frontera)
        if nodo_actual == destiny:
            # print('Destino encontrado: ', nodo_actual, '==', destiny)
            path_string = ver_caminos(nodo_actual, paths)
            print(path_string)
            print(len(explorados))
            break
        else:
            # print('Generando nuevas fronteras...')
            frontera, memoria, path = explorar_nodo(nodo_actual,
                                                    frontera,
                                                    memoria, lab)
            explorados.add(nodo_actual)
            paths.extend(path)

    return None


def main():
    # Recibir dimension de laberinto
    n, m = list(map(int, input().split()))
    lab = []
    # Recibir string de laberinto
    for i in range(0, n):
        lab.append(input()[:m])

    # Guardar coordenadas de origen y destino
    origin = tuple(map(int, input().split()))
    destiny = tuple(map(int, input().split()))

    buscar_salida(lab, origin, destiny)


if __name__ == "__main__":
    main()
