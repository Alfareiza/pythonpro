class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make='', model='', year=None):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Sempre que seja criada uma instância vai ter por padrão 0 nessa variável
        # Também pode ser criada no corpo do init como odometer_reading=0

    def get_descriptive_name(self):
        """ Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        """Define o valor de leitura de hodômetro com o valor especificado
        Rejeita a alteração se for tentativa de definir um valor menor para hodômetro
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer")

    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You can not rest miles from your car!')

    def fill_gas_tank(self):
        """Adiciona gas ao carro."""
        print(f"Gas added to your {self.make.title()} {self.model.title()}")


class ElectricCar(Car):
    """Representa aspectos de um carro específicos de veículos elétricos."""
    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico
        """
        super().__init__(make, model, year)  # Acrescento os atributos da classe Pai "Car"
        # self.battery_size = 70  # Definindo atributo novo para a clase filha
        self.battery = Battery()  # Definindo atributo como objeto

    def describe_battery(self):
        """Exibe uma frase de que descreve a capacidade da bateria"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):  # Sobrescrita de método
        """Carros elétricos não têm tanques de gasolina."""
        print("This car doesn't need a gas tank")


class Battery():  # É criada uma clase para batería pois ela terá muitos mais atributos
    """Uma tentativa simples de modelar uma bateria para um carro elétrico"""
    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print('This ar has a ' + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        """Atualiza a capacidade da batería e define-la com 85 se o valor for diferente"""
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(f"This car can go approximately {range} miles on a full charge.")


if __name__ == '__main__':
    my_new_car = Car('audi', 'a4', 2016)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()

    # Alterando atributos da instância
    my_new_car.odometer_reading = 23  # Forma 1 : Alterando atributo de instância existente (my_new_car)
    my_new_car.read_odometer()
    my_new_car.update_odometer(1000)  # Forma 2 : Alterando atributo pelo método consiguindo validar valor enviado
    my_new_car.read_odometer()
    my_new_car.increment_odometer(250)  # Forma 3 : Incrementando atributo através de um método
    my_new_car.read_odometer()

    print(6 * '=====')
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(f"Os atributos do objeto my_tesla são:\n\t\t\t {my_tesla.__dict__}\n")
    print(my_tesla.get_descriptive_name())

    my_tesla.battery.describe_battery()  # Chamando método a través do atributo (tipo objeto) do objeto.
    my_tesla.fill_gas_tank()  # Método fill_gas_tank sobrescrito no filho

    other_car = Car('renault', '4', 1998)
    other_car.fill_gas_tank()

    my_tesla.battery.get_range()  # Chamando método a través do atributo (tipo objeto) do objeto.
    # o atributo battery só poderá ser chamado desde o objeto my_tesla
    print(6 * '=====')
    last_car = ElectricCar('mazda', '3', 2019)
    last_car.battery.get_range()
    last_car.battery.upgrade_battery()
    last_car.battery.get_range()
