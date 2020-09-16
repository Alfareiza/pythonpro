# Básica leitura de um arquivo
with open('pi_digits.txt') as file_object:
    print(f'atributos do objeto file_object: {file_object.__dict__}')

    metodos_disponíveis = [i for i in file_object.__dir__() if '__' not in i]
    print(f'metodos disponíveis a file_object: {metodos_disponíveis}')

    contents = file_object.read()
    print(f"Conteúdo do arquivo file:\n{contents.rstrip()}")


print(10 * "=====")
# Lendo o arquivo desde se path relativo
with open('text_files/numbers.txt') as file_object:
    contents = file_object.read()
    print(f"Conteúdo do arquivo numberts.txt:\n{contents.rstrip()}")


print(10 * "*****")
# Lendo o arquivo por linha desde se path absoluto
file_path_numbers = '/Examples/files/text_files/numbers.txt'
with open(file_path_numbers) as file_object:
    # contents = file_object.read()
    print(f"Conteúdo do arquivo {file_path_numbers.split('/')[-1:][0]} por linha:")
    for line in file_object:
        print(f"\t\t{line.rstrip()}")


print(10 * "#####")
# Armazena as linhas do arquivo numa lista dentro do with em é exibido, fora do with
with open('text_files/numbers.txt') as file_object:
    lines = file_object.readlines() #  Lê todo o arquivo e armazena ele numa lista

print(f"Conteúdo do arquivo numbers.txt por linha fora do with:")
for i, line in enumerate(lines):
    print(f"Linha{i} > {line.rstrip()}")


print(10 * "%%%%%%")
# Armazena as linhas do arquivo num str dentro do with e é exibido, fora do with
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines() #  Lê todo o arquivo e armazena ele numa lista

pi = ''
for line in lines:
    pi += line.strip()

print(pi)
print(len(pi))


print(10 * "%%%%%%")
# Armazena as linhas do arquivo num str dentro do with e é exibido, fora do with
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines() #  Lê todo o arquivo e armazena ele numa lista

pi = ''
for line in lines:
    pi += line.strip()

print(pi)
print(len(pi))