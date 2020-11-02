from collections import deque
# Práctica #02-A
# ¿Cómo salgo del Laberinto?

class laberinto:
    def __init__(self, n, m, arr):
        pass


def verify_positive(x,y):
    return (lambda x,y: x>=0 and y>=0)(x,y) 


def move(direccion, nodo_actual, lab):
    direcciones = {'U':[-1,0],'R': [0,1],'D':[1,0], 'L':[0,-1]}

    direction = direcciones[direccion]
    
    # Llevar registro de Path
    path = ''
    
    try:
        coordenadas = (nodo_actual[0]+direction[0], nodo_actual[1]+direction[1])# Coordenadas que se generan si se mueva arriba
        
        if not verify_positive(coordenadas[0], coordenadas[1]):
            return None
        
        # print('-- nodo actual',nodo_actual[0], nodo_actual[1],'=',lab[nodo_actual[0]][nodo_actual[1]])
        print(f'--- nodo {direccion} actual',
               coordenadas[0], coordenadas[1],'=',
               lab[coordenadas[0]][coordenadas[1]])

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
        print('error: Index error')
        return None, coordenadas, ''




def explorar_nodo(nodo_actual, frontera, memoria, laberinto, path):
    """ Tomando como referencia al nodo actual, 
    explora a los nodos visitables desde ahí """
    frontera = frontera #
    memoria = memoria #
    path = path
    print(f'** Explorando nodo {nodo_actual}...')
    
    for d in ['U','R','D','L']:
        print(d)
        try:
            new_node, coord, p = move(d, nodo_actual, laberinto)
            print(new_node)
            if coord and new_node not in memoria:
                memoria.append(coord)
                if new_node:
                    frontera.append(new_node)
                    path = f'{path}{p}'
        except TypeError:
                print('Nothing')
        

    # arriba = move('U', nodo_actual, laberinto)
    # print('-~ arriba', arriba)

    # derecha = move('R', nodo_actual, laberinto)
    # print('-~ derecha', derecha)

    # abajo = move('D', nodo_actual, laberinto)
    # print('-~ abajo', abajo)

    # izquierda = move('L', nodo_actual, laberinto    )
    # print('-~ izquierda', izquierda)

    return frontera, memoria, path


def buscar_salida(lab, origin, destiny):
    """
    Return solution_path, number_visited_nodes
    """
    path = ''
    origin = origin[0]-1, origin[1]-1
    destiny = destiny[0]-1, destiny[1]-1
    # Arriba, Derecha, Abajo, Izquierda
    
    frontera = deque()
    memoria = deque()   
    frontera.append(origin)
    memoria.append(origin)
    print('Buscando salida...')
    print(frontera)
    
    print(destiny)
    while frontera:
        nodo_actual = frontera.popleft()
        print(frontera)
        if nodo_actual == destiny:
            # 
            print('Destino encontrado: ', nodo_actual, '==', destiny)
            print(path)
            print(len(memoria))
            # Regresar coordenada de destino
            # Regrar tupla de solucion sumandole 1
            # return nodo_actual
        else:
            print('Generando nuevas fronteras...')
            frontera, memoria, path = explorar_nodo(nodo_actual, frontera, memoria, lab, path)
        print('Frontera: ', frontera)
    
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
    
    print(origin)
    print(destiny)

    buscar_salida(lab, origin, destiny)

if __name__ == "__main__":
    main()