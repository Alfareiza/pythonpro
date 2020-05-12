"""
This program receive a letter and verify if it is consonant or vowel.
"""
letra = input('Digite uma Letra -> ')
def vocal_ou_consoante(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return 'Used digitó una vocal'
    else:
        return 'Usted digitó una consonante'

print(vocal_ou_consoante(letra))
