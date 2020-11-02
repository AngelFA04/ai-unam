from collections import deque
# Práctica #02-A
# ¿Cómo salgo del Laberinto?

class laberinto:
    def __init__(self, n, m, arr):
        pass


def verify_positive(x,y):
    return (lambda x,y: x>=0 and y>=0)(x,y) 


def move(direccion, nodo_actual, lab, path):
    """Funcion para moverse en el plano
    Arriba, Derecha, Abajo, Izquierda
    """
    direcciones = {'U':[-1,0],'R': [0,1],'D':[1,0], 'L':[0,-1]}

    direction = direcciones[direccion]
    
    # Llevar registro de Path
    path = path
    
    try:
        coordenadas = (nodo_actual[0]+direction[0], nodo_actual[1]+direction[1])# Coordenadas que se generan si se mueva arriba
        
        if not verify_positive(coordenadas[0], coordenadas[1]):
            return None, coordenadas, direccion,'' 
        
        # print('-- nodo actual',nodo_actual[0], nodo_actual[1],'=',lab[nodo_actual[0]][nodo_actual[1]])
        # print(f'--- nodo {direccion} actual',
        #       coordenadas[0], coordenadas[1],'=',
        #       lab[coordenadas[0]][coordenadas[1]], end=' -> ')

        contenido = lab[coordenadas[0]][coordenadas[1]]
        
        if contenido == '#':
            return None, coordenadas, direccion, ''
        elif contenido == '.':
            return coordenadas, coordenadas, direccion, path
        elif contenido == 'D':
            return coordenadas, coordenadas, direccion, path
        else:
            return None, coordenadas, direccion, ''
    except IndexError:
        print('error: Index error')
        return None, None, '', ''

def oposite(direction):
    if direction == 'D':
        return 'U'
    elif direction == 'U':
        return 'D'
    elif direction == 'L':
        return 'R'
    elif direction == 'R':
        return 'L'


def explorar_nodo(nodo_actual, frontera, memoria, laberinto, path):
    """ Tomando como referencia al nodo actual, 
    explora a los nodos visitables desde ahí """
    frontera = frontera #
    memoria = memoria #
    
    path = dict()
    
    print(f'** Explorando nodo {nodo_actual}...')
    for d in ['U','R','D','L']:
        # print(d)
        # print(f'Path: \t {path}')
        
        new_node, coord, direction, p = move(d, nodo_actual, laberinto, path)
        # print(new_node)
        if not oposite(direction) == d:
            if coord and (new_node not in memoria):
                memoria.append(coord)
                if new_node:
                    frontera.append(new_node)
                    path[new_node] = dict()
                    path[new_node][d] = True
                # else:
                #    path[new_node][d] = False

    return frontera, memoria, path


def verificar_caminos(paths):
    paths = dict(paths)

    empties = []
        
    for k,v in paths.items():
        if v == dict():
            empties.append(k)
            print('Ahí te ves')
    

    while empties:
        for k,v in paths.items():
            for e in empties:
                if e in v:
                    print('Te encontre esponja')
                    del paths[k][e]

        for e in empties:
            print('Te encontre esponja')
            del paths[e]

        for k, v in paths.items():
            print(k,v)

        empties = []

        for k,v in paths.items():
            if v == dict():
                empties.append(k)
                print('Ahí te ves')
    
    print('empties', empties)
    
    return [paths]

def eliminar_vacio():
    pass


def buscar_salida(lab, origin, destiny):
    """
    Return solution_path, number_visited_nodes
    """
    complete_path = ''
    paths = dict()
    origin = origin[0]-1, origin[1]-1
    destiny = destiny[0]-1, destiny[1]-1
    # Arriba, Derecha, Abajo, Izquierda
    
    frontera = deque()
    memoria = deque()   
    frontera.append(origin)
    memoria.append(origin)
    print('Buscando salida...')
    print('Frontera: ', frontera)

    while frontera:
        nodo_actual = frontera.popleft()
        print('Frontera: ', frontera)

        if nodo_actual == destiny:
            # 
            print('Destino encontrado: ', nodo_actual, '==', destiny)
            paths = verificar_caminos(paths)

            print('El camino del señor:', paths)
            # print(len(memoria))
        else:
            print('Generando nuevas fronteras...')
            frontera, memoria, path = explorar_nodo(nodo_actual, frontera, memoria, lab, complete_path)
            paths[nodo_actual] = (path)
        print('Caminito: ', paths)
        print('Frontera: ', frontera)
        print('------------------')
    
    

    print('Memoria: ', memoria)
    
    # Regrar tupla de solucion sumandole 1
    return None
    pass


def main():
    # Recibir dimension de laberinto
    n, m = list(map(int,input().split()))
    
    lab = []
    # Recibir string de laberinto
    for i in range(0,n):
        lab.append(input()[:m])

    # Guardar coordenadas de origen y destino
    origin = tuple(map(int,input().split()))
    destiny = tuple(map(int,input().split()))
    # Convertir a matriz
    
    for i,l in enumerate(lab,0):
        print(i, '\t',l)
    
    print('Origen:', origin)
    print('Destino:',destiny)

    buscar_salida(lab, origin, destiny)

if __name__ == "__main__":
    main()