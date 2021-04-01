import re

file_path_numbers = 'texto_to_be_regexed.txt'


def texto():
    with open(file_path_numbers) as file_object:
        contents = file_object.read()
        # print(contents)
    return contents


contents = texto()


def uso_de_match(contents):
    # MATCH: Encuentra la coincidencia exacta de lo que buscas en la primera linea de un string
    result = re.match("Alfonso", contents)
    if result:
        print('Se encontraron coincidencias')
    else:
        print('No se encontraron coincidencias')


def uso_de_search():
    info = "Chelsae: aol.com|Dorie: 4shared.com|Felipe: nhs.uk|Ahmed: technorati.com|Francisco: ggl.com.es"
    result = re.search(r"\bF\w+", info)
    # Retorna objeto con el match encontrado y su posicion de inicio y final
    print(result)
    # group() Imprime el primer match encontrado
    print(result.group())

    info = "987984519563224"
    result = re.search(r"(\d{3})(\d{4})", info)
    # group(1) o group(2) me trae el match de los grupos capturados, escogiendo cual quiero
    print(result.group(2))
    # groups trae una tupla con los grupos capturados
    print(result.groups())
    # span me retorna el indice y fin según el # de grupo solicitado
    print(result.span(1))


def uso_de_findall(contents):
    string = "Nissie: A+, Devland: AB+, Wallie: AB-, Thaine: O+, Herrick: A+, Patsy: B+, Corella: A-, Avis: O-, Windy: A+"
    result = re.findall("A[+-]", string)
    # Lista con todos los matchs encontrados
    print(result)
    result = re.findall(r"\d{9}", contents)
    print(result)


def uso_de_split():
    # separa el string en donde encuentra una coincidencia
    # Y retorna una lista de todos esos strings en donde las divisiones ocurrieron.
    string = "Chelsae: aol.com|Doria: 4shared.com|Felipe: nhs.uk|Ahmed: technorati.com|Davie: amazon.com|Egon: google.it"
    result = re.split(r'\|', string)
    # Dividirá el resultado por | y me traerá una lista con el resultado
    print(result)


def uso_de_sub():
    # En base a un patron, retorna un string donde se realizaron el remplazo con el contenido especificado
    # buscar y remplazar
    string = 'Este es\nun tutorial\nde python'
    espacio = ' '
    print('Este es el texto antes del uso de sub:\n', string)
    result = re.sub(r'\n', espacio, string)
    print('\nEste es el texto despues del uso de sub:\n', result)

    # Realiza un reemplazo
    result = re.sub(r'\n', espacio, string, 1)  # 1 indica que reemplazará una vez
    print("\nEste es el resultado al haber logrado 1 reemplazo:\n", result)

    # Subn retorna una tupla con el nuevo string y el número de reemplazos realizados.
    result = re.subn(r'\n', espacio, string)
    print("\nTupĺa con nuevo string y cant de vezes de reemplazos:\n", result)


if __name__ == '__main__':
    # uso_de_match(contents)
    # uso_de_search()
    uso_de_findall(contents)
    # uso_de_split()
    # uso_de_sub()
