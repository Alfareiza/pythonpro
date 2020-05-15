"""
This program receive a letter and verify if it is consonant or vowel.
"""
letra = input('Digite uma Letra -> ')

def vocal_ou_consoante(letra):
    if letra in set('aeiou'):
        return 'Used digitó una vocal'
    else:
        return 'Usted digitó una consonante'

print(vocal_ou_consoante(letra))
