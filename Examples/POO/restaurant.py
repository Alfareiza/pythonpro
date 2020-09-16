class Restaurant():
    def __init__(self, name, tipo):
        self.restaurant_name = name
        self.cuisine_tipo = tipo
        self.number_served = 0

    def describe_restaurant(self):
        print('The name of the restaurant is "', self.restaurant_name,
              '" and his especiatility is', self.cuisine_tipo, 'food.')

    def open_restaurant(self):
        print('The restaurant is Open!')

    def read_number_served(self):
        print("Now we have attended " + str(self.number_served) + " people.")

    def set_number_served(self, clients_served):
        """ Define o número de clientes atendidos"""
        if clients_served >= 0:
            self.number_served = clients_served
        else:
            print('You can not set a negative number')

    def increment_number_served(self, clients_attended):
        """Incremente o número de clientes atendidos"""
        if clients_attended >= self.number_served:
            self.number_served += clients_attended
        else:
            print('You can not roll back your attended clients')


class IceCreamStand(Restaurant):
    def __init__(self, name, tipo, flavors):
        super().__init__(name, tipo)
        self.flavors = flavors

    def get_flavors(self):
        message = ''
        for flavor in self.flavors:
            message += f', {flavor}'
        return message[2:].title()


las_vasijas = Restaurant('las vasijas', 'peruvian')
print(las_vasijas.restaurant_name.title())
print(las_vasijas.cuisine_tipo.title())
las_vasijas.describe_restaurant()
las_vasijas.open_restaurant()

print(6*'=====')
#  Instanciamento básico de 3 objetos tipo Restaurant
cucayo = Restaurant('Cucayo', 'Colombian')
nena_lela = Restaurant('Nena Lela', 'Italian')
piccolo = Restaurant('Piccolo', 'Italian Pizzas')
cucayo.describe_restaurant()
nena_lela.describe_restaurant()
piccolo.describe_restaurant()

print(6*'=====')
# Alterando atributos de um objeto de 3 formas diferentes (direto ao atributo, através de um método e incrementando)
mrfull = Restaurant('mrfull', 'fast food')
mrfull.read_number_served()
mrfull.number_served = 10
mrfull.read_number_served()
mrfull.set_number_served(20)
mrfull.read_number_served()
mrfull.increment_number_served(50)
mrfull.read_number_served()

print(6*'=====')
sorveteria = IceCreamStand('los helados', 'normal', ['arequipe', 'chocolate', 'fresa', 'frambuesa'])
# print(f'Atributos da sorveteria são:\n\t\t\t{sorveteria.__dict__}')
print(f'En sorveteria {sorveteria.restaurant_name.title()} tenemos helados de {sorveteria.get_flavors()}')
