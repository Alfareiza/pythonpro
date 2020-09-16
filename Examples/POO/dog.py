class Dog():
    """Uma tentativa simples de modelar um cachorro"""

    def __init__(self, name, age):
        """Inicializa os atributos name e age"""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentado  em resposta de um comando"""
        print(f"{self.name.title()} is now sitting!")

    def roll_over(self):
        """Simula um cachorro sentado  em resposta de um comando"""
        print(f"{self.name.title()} is now rolled over!")


my_dog = Dog("maya", 2)  # Instanciamento de un objeto 'my_dog' de tipo 'Dog'
print('My dog is', my_dog.name.title(), '.')
print('My dog is', str(my_dog.age), 'years old.')
my_dog.sit()
my_dog.roll_over()

print(6*'=====')

other_dog = Dog('motita', 10)   # Instanciamento de un objeto 'other_dog' de tipo 'Dog'
print('Other dog is', other_dog.name.title(), '.')
print('Other dog is', str(other_dog.age), 'years old.')
other_dog.sit()
other_dog.roll_over()
