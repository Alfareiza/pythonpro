"""
Libro Curso Intensito Python, Exercisio 9.14 Dados, Pag 251:
a. Crie uma clase Die com um atributo chamado sides, cujo valor default é 6.
    i. Escreva um método chamado roll_die() que exiba um número aleatório entre 1 e
    número de lados do dado.
    ii. Crie um dado de seis lados e lance-o cinco vezes.
    iii. Crie um dado de dez lados e outro de vinte lados. Lance cada dado cinco vezes.
"""
from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"Resultado de dado de {self.sides} lados : {randint(1, self.sides)}")


if __name__ == '__main__':
    dado1 = Die()  # Criação de dado com 6 lados (valor default)
    dado1.roll_die()  # Lançamento de lado de 6 lados
    dado1 = Die(10)  # Criação de dado com 10 lados
    dado1.roll_die()  # Primer lançamento do dado de 10 lados
    dado1.roll_die()
    dado1.roll_die()
    dado1.roll_die()
    dado1.roll_die()
    dado1 = Die(20)  # Criação de dado com 20 lados
    dado1.roll_die()  # Primer lançamento do dado de 20 lados
    dado1.roll_die()
    dado1.roll_die()
    dado1.roll_die()
    dado1.roll_die()
