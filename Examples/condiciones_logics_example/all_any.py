#https://pythonhelp.wordpress.com/2012/11/06/all-e-any/

listaDeInteiros = [2, 6, 4, 7, -2]
def using_all():
    listaDeInteiros = [2, 6, 4, 7, -2]
    if all(i % 2 == 0 for i in listaDeInteiros): #Verifica si todos los elementos en la lista CUMPLEN una condición
        print ('Todos sao pares')
    else:
        print ('Tem algum impar')
    return

def using_any():
    if not any(i % 2 != 0 for i in listaDeInteiros): #Verifica si todos los elementos en la lista NO CUMPLEN una condición
        print ('Todos sao pares')
    else:
        print ('Tem algum impar')
    return

def usingall_2():
    lista_de_strings = ['Alfonso','Areiza','Guerra','30 años']
    if all(s != '' for s in lista_de_strings):
        print ("funcao_que_nao_trata_strings_vazias(lista_de_strings)")
    else:
        print ("Erro: strings vazias existem na lista!")
    return

usingall_2()

