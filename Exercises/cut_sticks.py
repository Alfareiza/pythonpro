"""
En el siguiente código, se itera tantas vezes
sea necesario el mismo array hasta que quede vazío.

En cada iteración se detecta cual es el valor menor,
y se le resta a todos los elementos existentes del array.

Ejemplo:
[5, 4, 4, 2, 2, 8] 
# El valor menor es el 2, al restar este valor del
# restante del arr, queda así:
[3, 2, 2, 6]
# El valor menor es el 2, al restar este valor del
# restante del arr, queda así:
[1, 4]
# El valor menor es el 1, al restar este valor del
# restante del arr, queda así:
[3]
# El valor menor es el 3, al restar este valor del
# restante del arr, queda así:
[]

En cada iteración se cuenta cuantas veces se restaron valores.
En la primera iteración, se restaron 6
En la segunda iteración, se restaron 4
En la tercera iteración, se restaron 2
En la cuarta iteración, se restó 1

La función retonará entonces : [6, 4, 2, 1]

"""
arr = [5, 4, 4, 2, 2, 8]

r_accum = []
while sum(arr) > 0:
    accum = 0
    current_min = min(arr)
    i = 0
    while i <= len(arr) - 1:
        result = arr[i] - current_min
        if result > 0:
            arr[i] = result
            accum += 1
            i += 1
        elif result == 0:
            accum += 1
            del arr[i]
            
    r_accum.append(accum)

print(r_accum)
