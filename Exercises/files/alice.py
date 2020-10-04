def count_words(path_filename):
    """
    Count the aprox number of words in a file
    """
    try:
        with open(f'files_of_exercises/{filename}') as file:
            content: str = file.read()
    except Exception as e:
        print(f'The next error ocurred : {e}')
    else:
        words = content.split()
        print(f'The File \"{filename}\" has about {len(words)}')


def count_single_word(path_filename, word):
    """
    Count the aprox number of words in a file
    """
    try:
        with open(f'files_of_exercises/{filename}') as file:
            content: str = file.read()
    except Exception as e:
        print(f'The next error ocurred : {e}')
    else:
        words = content.split()
        print(f'The word \"{word}\" is {words.count(word.lower())} times')


if __name__ == '__main__':
    filename = 'alice.txt'
    count_words(filename)
    count_single_word(filename, 'the')
