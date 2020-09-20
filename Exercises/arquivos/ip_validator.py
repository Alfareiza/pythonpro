"""
https://wiki.python.org.br/ExerciciosArquivos
1. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP
e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
    i. O arquivo de entrada possui o seguinte formato:
        200.135.80.9
        192.168.1.1
        8.35.67.74
        257.32.4.5
        85.345.1.2
        1.2.3.4
        9.8.234.5
        192.168.0.256
    O arquivo de saída possui o seguinte formato:
        [Endereços válidos:]        [Endereços inválidos:]
        200.135.80.9                257.32.4.5
        192.168.1.1                 85.345.1.2
        8.35.67.74                  9.8.234.5
        1.2.3.4                     192.168.0.256
"""
import os

texto_entrada = '200.135.80.9\n192.168.1.1\n8.35.67.74\n257.32.4.5\n85.345.1.2\n1.2.3.4\n9.8.234.5\n192.168.0.256'


class File():

    def create_file(self, content='', filename='ip_to_validate.txt'):
        """
        Create a file giving a filename and content
        """
        with open(f'{os.path.dirname(os.path.abspath(__file__))}/files_of_exercises/{filename}', 'w') as fp:
            fp.write(content.strip())

    def read_file(self, filename):
        """
        Read a file and return a list
        """
        with open(f'{os.path.dirname(os.path.abspath(__file__))}/files_of_exercises/{filename}') as fp:
            lines = fp.readlines()
        return lines

    def valid_ip(self, ip):
        """
        Validate every number of the ip.
        Return True if all the bytes are between 0 and 255
        """
        if all([True if 0 <= int(i) <= 255 else False for i in ip.split('.')]):
            return True
        else:
            return False

    def report_ips(self, filename='ip_to_validate.txt'):
        """
        Analyse a file with a giving default structure and the analyse if every ip is valid
        Return: Create a new file with the result report
        """
        lines_of_file = self.read_file(filename)
        valid_ips, invalid_ips = '', ''
        for line in lines_of_file:
            if self.valid_ip(line):
                valid_ips += line
            else:
                invalid_ips += line

        content = f'[Endereços válidos:]\n{valid_ips}\n[Endereços inválidos:]\n{invalid_ips}'
        self.create_file(content, filename='ip_validated.txt')


if __name__ == '__main__':
    validator0 = File()
    validator0.create_file('200.135.80.9\n192.168.1.1\n8.35.67.74\n257.32.4.5\n85.345.1.2\n1.2.3.4\n9.8.234.5\n192.168.0.256')
    validator0.report_ips()
