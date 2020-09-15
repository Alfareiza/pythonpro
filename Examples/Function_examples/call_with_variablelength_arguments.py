

#  Function definition is here known as 'Parámetros Variables en Funciones' ----------------
def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output arg is: ", arg1)

    for var in vartuple:
        print("vartuple: ", var)
    return


#  Now you can call printinfo function
#  printinfo(10)
printinfo(70, 60, 50)


# Parámetros Variables en Funciones
def sum(self, *args):
    aux = 0
    for valor in args:
        aux = aux + valor
    print('Resultado : ', aux)
    return


sum(1, 10)


def print_three_things(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')


mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)
