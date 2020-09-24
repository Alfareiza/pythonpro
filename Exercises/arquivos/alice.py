filename = 'alice.txt'
try:
    with open(f'files_of_exercises/{filename}') as file:
        content: str = file.read()
except Exception as e:
    print(f'The next error ocurred : {e}')
else:
    words = content.split()
    print(f'The File \"{filename}\" has about {len(words)}')
