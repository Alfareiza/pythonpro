def recursive_min_max(lista: list) -> tuple:
    """
    Implementación recursiva dejando todas las comparacinoes en la pila de ejecución 
    hasta alcanzar la mínima lista para resolver la comparación de los elementos
    
    Análisis de Complejidad de Tiempo
    
    2n Comparaciones        -> f(n) = 2n -> n
    2n Slicing              -> f(n) = 2n -> n
    2n + 2 Atribuiciones    -> f(n) = 2n + 2 -> n
    2n + 1 Decisión         -> f(n) = 2n + 1 -> n
    
    Total: f(n) = 4n -> 0(n)
    
    Complejidad de Espacio
    
    2 Funciones         -> f(n) = c -> 1
    2n Variables (list) -> f(n) = 2n -> n
    n^2 call stack      -> f(n) = n^2 -> n^2
    
    Total: f(n) = 1 + n + n^2 -> O(n^2)
    """

    def recursive_menor(lista: list) -> int:
        primeiro = lista[0]

        if len(lista) == 1:
            return primeiro
        else:
            menor = recursive_menor(lista[1:])
            return menor if menor < primeiro else primeiro

    def recursive_maior(lista: list) -> int:
        primeiro = lista[0]

        if len(lista) == 1:
            return primeiro
        else:
            maior = recursive_maior(lista[1:])
            return maior if maior > primeiro else primeiro

    if not lista:
        raise ValueError

    _menor = recursive_menor(lista)
    _maior = recursive_maior(lista)

    return (_menor, _maior)


if __name__ == '__main__':
    print(recursive_min_max([0, 105, 27, 55]))
