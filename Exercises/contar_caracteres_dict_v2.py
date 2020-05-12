def contar_caracteres(s):
  #  Ejemplo:
  #  >>>contar_caracteres('Alfonso')
  #  {'f':1,'l':1,'n':1,'o':2,'s':1} """
    
    resultado = {} #declaración del dict
    for caracter in s:
        resultado [caracter]  = resultado.get(caracter,0) +1
# ejemplo : resultado ['a'] = [1]
    return resultado

if __name__ == '__main__':
    print(contar_caracteres('Alfonso'))
    print(contar_caracteres('Areiza'))