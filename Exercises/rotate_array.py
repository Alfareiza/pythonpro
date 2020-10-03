"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated
to [5,6,7,1,2,3,4]. How many different ways do you know to solve this problem?
    >>> print(rotate_lst([1,2,3,4,5,6,7], 3))
    [5, 6, 7, 1, 2, 3, 4]
    >>> print(rotate_lst(list('python'), 3))
    ['h', 'o', 'n', 'p', 'y', 't']
    >>> for elemento in rotate_lst(list('alfonso'), 1):
    ...     print(elemento)
    ...
    o
    a
    l
    f
    o
    n
    s
    >>> print(rotate_lst_v2(list('tom jobim'), 1))
    ['m', 't', 'o', 'm', '', 'j', 'o', 'b', 'i']
"""
from itertools import chain
from time import time


def rotate_lst(iteravel, k: int):
    lenght = len(iteravel)
    novo_iteravel = [None] * lenght
    for i, j in enumerate(iteravel):
        new_index = -lenght + k
        novo_iteravel[new_index] = iteravel[i]
        lenght -= 1
    return novo_iteravel

def rotate_lst_2(iteravel, k: int):
    primera_parte = iteravel[-k:] # O(n) em tempo e em espaço
    segunda_parte = iteravel[:-k]
    return primera_parte + segunda_parte


def rotate_generator(iteravel, k: int):
    n = len(iteravel)
    primera_parte = range(n - k, n) # São criados os slices como um objeto range
    segunda_parte = range(n - k)
    indices_rotacionados = chain(primera_parte, segunda_parte)
    for indice_rotacionado in indices_rotacionados:
        yield iteravel[indice_rotacionado]

if __name__ == '__main__':
    inicio = time()
    lista = range(1, 1_000_000)
    for elemento in rotate_generator(lista, 1):
        print(elemento)
    final = time()
    print(f'Con yield Demoró: {final - inicio} segundos')
    inicio = time()
    rotate_lst(lista, 1)
    final = time()
    print(f'Sin yield Demoró: {final - inicio} segundos')
