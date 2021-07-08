import string

"""
O Pantograma é uma sentença que contem todas as letras do alfabeto, ao menos um vez. Por exemplo, a sentença: 
- Quem traz CD, LP, fax, engov e whisky JB? (29 letras).
Desafio: Dada uma string, detecte se ela é ou não um Pantograma retornando True ou False. Ignore números, pontuações e acentos.
>>>

Pantogramas para testes:
- Jane quer LP, fax, CD, giz, TV e bom whisky.[2] (30 letras)
- TV faz quengo explodir com whisky JB. (30 letras)
- Vejo xá gritando que fez show sem playback. (35 letras)
- Todo pajé vulgar faz boquinha sexy com kiwi. (36 letras)
- Vi que ex-janota gordo fez show com playback. (36 letras)
- Já fiz vinho com toque de kiwi para belga sexy. (37 letras)
- Bancos fúteis pagavam-lhe queijo, whisky e xadrez. (41 letras)
"""


def is_pantograma(sentence: str):
    """
    Recebe uma frase e retorna True se é um Pantograma e False se não.
    :param sentence: :str
    :return: True or False: boolean
    >>> is_pantograma("Jane quer LP, fax, CD, giz, TV e bom whisky.[2]")
    True
    >>> is_pantograma("Alfonso")
    False
    >>> is_pantograma("Vejo xá gritando que fez show sem playback.")
    True
    >>> is_pantograma("Todo pajé vulgar faz boquinha sexy com kiwi")
    True
    """
    phrase = set(sentence.strip().lower())
    characters = set(string.ascii_lowercase)
    if not characters.difference(set(phrase)):
        return True
    else:
        return False


if __name__ == '__main__':
    sentences = ["Jane quer LP, fax, CD, giz, TV e bom whisky.[2]", \
                 "TV faz quengo explodir com whisky JB.", \
                 "Vejo xá gritando que fez show sem playback.", \
                 "Todo pajé vulgar faz boquinha sexy com kiwi.", \
                 "Vi que ex-janota gordo fez show com playback.", \
                 "Já fiz vinho com toque de kiwi para belga sexy.", \
                 "Bancos fúteis pagavam-lhe queijo, whisky e xadrez.", \
                 "Lorem ipsum dolor sit amet, consectetur adipiscing."]
    for sentence in sentences:
        print(sentence, is_pantograma(sentence))
