#  Criando arquivo programming.txt
filename = 'text_files/programming.txt'
with open(filename, 'w') as file_object:  # Se o arquivo existisse, ele substitui o existente
    file_object.write("I love Python.\n")  # Python só escrebe informação tipo texto
    file_object.write("Hello World\n")
    # Neste exemplo ele irá escrever os dois textos um do lado do outro, e por causa disso deve ser enviado o \n.
    # Se não acha o arquivo pela rota dada, retornará erro de 'FileNotFoundError'


#  Concatenando informação do arquivo programming.txt
filename = 'text_files/programmin.txt'
with open(filename, 'a') as file_object:  # Se o arquivo existisse, ele concatenará, se não criará um novo.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I Love creating apps\n")
    # Após primera execução ele sempre vai concatenar. Caso queira limpar o arquivo antes de concatenar,
    # deverá ser criado o arquivo de novo para recever novas concatenações.

