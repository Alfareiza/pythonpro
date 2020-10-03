"""
https://wiki.python.org.br/ExerciciosArquivos
2. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de files.
 Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
 identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar
  o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere
um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma
a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
 através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá
  ser feito através de uma função, que será chamada pelo programa principal.

"""
import os
from tabulate import tabulate


class UsersToReport():

    def create_file(self, content='', filename='users_to_report.txt'):
        """
        Create a file giving a filename and content
        """
        try:
            with open(f'{os.path.dirname(os.path.abspath(__file__))}/files_of_exercises/{filename}', 'w') as fp:
                fp.write(content.strip())
        except FileNotFoundError:
            print(f'Sorry, the file {filename} doesn\'t exist')
        except FileExistsError:
            print(f'Sorry, there was ane error with the file {filename}')

    def read_file(self, filename):
        """
        Read a file and return a list
        """
        with open(f'{os.path.dirname(os.path.abspath(__file__))}/files_of_exercises/{filename}') as fp:
            lines = fp.readlines()
        return lines

    def bt_to_mb(self, num: int):
        num = round(num * 0.000001, 2)
        return f'{str(num)} MB'

    def parse_line(self, line):
        """
        Receive a str, equivalent to a line of the file.
                Ex. : 'alexandre\t\t\t456123789\n'
                They way to parse the line is the next:
                > From 0 until the firtst '\t will take the name
                > From len(line) until the first \t will take the number (including the last digit)
        return: dict with values of user
                Ex. : {'name': 'alexandre', 'consume_bt': 456123789, 'consume_mb': '456.12 MB', }
        """
        try:
            user_data = dict()
            user_data['name'] = line[0:line.index('\t')]
            user_data['consume_bt'] = int(line[line.rindex('\t') + 1:-1])
            user_data['consume_mb'] = self.bt_to_mb(int(user_data['consume_bt']))
        except Exception:
            print('The file could not be read')
        else:
            return user_data

    def calc_percent_by_user(self, users, total):
        """
        Add key 'percent' to dict user with consume value of every user
        Ex. : 'percent' :
        Receive: users (list of dicts)
                total (int)
        """
        for user_data in users:
            percent = user_data['consume_bt'] / total
            user_data['percent'] = f'{round(percent* 100, 2)} %'

    def calc_total(self, users):
        """
        Calculate total consume in bytes considering what every user consumed
        return: total (int)
         """
        total = 0
        for user in users:
            temp = user['consume_bt']
            total += temp
        return total

    def create_content(self, users, total):
        """
        Construct the header, body and footer for the output file
        Receive: users (list of dicts)
                total (int)
        """

        head_content = f"ACME Inc.\t\t\t\tUso do espaço em disco pelos usuários\n" \
                       f"{30 * '--'}\n"

        # Order list by value 'consume_bt' (int) of the dicts
        users = sorted(users, key=lambda k: k['consume_bt'], reverse=True)

        table, row = [], []
        for i, user in enumerate(users, 1):
            row = [i, user['name'].title(), user['consume_mb'], user['percent']]
            table.append(row)

        body_content = tabulate(table, headers=['N°', 'Nome', 'Espaço Utilizado', '% do uso'])
        footer_content = f"\n{30 * '--'}\n" \
                         f'\nEspaço total ocupado: {self.bt_to_mb(total)}\n' \
                         f'Espaço médio ocupado: {self.bt_to_mb(total / len(users))} '

        content = head_content + body_content + footer_content

        return content

    def report_users(self, filename='users_to_report.txt'):
        """
        Main function that process all the information
        Receive file for analysing
        """
        lines_of_file = self.read_file(filename)
        users = []
        for line in lines_of_file:
            users.append(self.parse_line(line))

        total = self.calc_total(users)
        self.calc_percent_by_user(users, total)

        content = self.create_content(users, total)
        self.create_file(content, filename='users_reported.txt')


if __name__ == '__main__':
    file0 = UsersToReport()
    file0.create_file(
            content="alexandre\t\t\t456123789\nanderson\t\t\t1245698456\nantonio\t\t\t\t123456456\n"
                    "carlos\t\t\t\t91257581\ncesar\t\t\t\t987458\nrosemary\t\t\t789456125\n"
                    "alfonso\t\t\t64956125\ncarlos julio\t\t\t55556125\njose julian jose\t\t\t995556125",
            filename='users_to_report.txt')
    file0.report_users('users_to_report.txt')
