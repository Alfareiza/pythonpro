"""
    >>> user1 = User('114322723', 'alfonsito', 'areiza', 31)
    >>> user1.increment_login_attempts()
    >>> user1.increment_login_attempts()
    >>> user1.increment_login_attempts()
    >>> user1.login_attempts
    3
    >>> user1.reset_login_attempts()
    >>> user1.login_attempts
    0
"""


class User():
    def __init__(self, ide: str, first: str, last: str, age: int, login_attempts=0):
        self.ide = ide
        self.first_name = first
        self.last_name = last
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        """Cria um dict a partir de 3 atributos, first_name, last_name e age"""
        person = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
        }
        for k, v in person.items():
            print(k.title(), ':', str(v).title())

    def increment_login_attempts(self):
        """Incremente as tentativas de login de um usuário"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reinicia o valor de login_attempts para 0"""
        self.login_attempts = 0


class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.title())


class Admin(User):
    def __init__(self, ide, first, last, age, login_attempts=0):
        super().__init__(ide, first, last, age, login_attempts)
        # self.privileges_admin = privileges_admin
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])

    def show_privileges_admin(self):
        print(f'Privileges of the Admin {self.first_name.title()}:')
        for privilege in self.privileges_admin:
            print(privilege.title())


if __name__ == '__main__':
    user0 = User('085.176.411-83', 'alfonso', 'areiza', 31)
    user0.describe_user()

    print(6 * "=====")
    user1 = User('114322723', 'alfonsito', 'areiza', 31)
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    print("The user has tried " + str(user1.login_attempts) + " times to login.")
    user1.reset_login_attempts()
    print("The user has tried " + str(user1.login_attempts) + " times to login.")

    print(6 * "=====")
    user2 = Admin('32651845', 'Gilma', 'Guerra', 31, ['can add post', 'can delete post', 'can ban user'])
    # user2.show_privileges_admin()  # É neccesário adicionar 'privileges_admin' no construtor do Admin

    print(6 * "=====")
    user2 = Admin('32651845', 'jessicka', 'castro', 24)
    user2.privileges.show_privileges()  # privileges setados na clase Privileges()
