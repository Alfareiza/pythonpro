from numbers import Number
from typing import Iterable, Tuple, Iterator
from math import inf


def _minmax_recursiva(iterador: Iterator, valor_minimo: Number, valor_maximo: Number):
    try:
        elemento = next(iterador)
    except StopIteration:
        return valor_minimo, valor_maximo
    else:
        if elemento < valor_minimo:
            valor_minimo = elemento
        if elemento > valor_maximo:
            valor_maximo = elemento
        return _minmax_recursiva(iterador, valor_minimo, valor_maximo)


def minmax(iteravel: Iterable) -> Tuple[Number, Number]:
    """
    >>> minmax([])
    Traceback (most recent call last):
        ...
    ValueError: Não existe mínimo e máximo
    >>> minmax([1])
    (1, 1)
    >>> minmax(a for a in range(10))
    (0, 9)
    >>> minmax(range(950))
    (0, 949)
    """
    iterador = iter(iteravel)
    valor_minimo, valor_maximo = _minmax_recursiva(iterador, inf, -inf)
    if valor_minimo is inf:
        raise ValueError('Não existe mínimo e máximo')
    return valor_minimo, valor_maximo
