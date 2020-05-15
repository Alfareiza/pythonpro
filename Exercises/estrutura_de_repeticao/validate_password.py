"""
 Exercise #15 of https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
Write a Python program to check the validity of password input by users. Go to the editor
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""
import string

# invalidChars = set(string.punctuation.replace("_", ""))#A set is created without considering '_'
invalidChars = set(string.punctuation) #A set is created with the atribute punctuation of the class string
lowercase = set(string.ascii_lowercase) #A set is created with the atribute ascii_lowercase of the class string
uppercase = set(string.ascii_uppercase) #A set is created with the atribute ascii_uppercase of the class string
digits = set(string.digits) #A set is created with the atribute digits of the class string

def validate_password():
x = True
while x:
        word = input('Digite su contraseña --> ')
        msg = ''
        if not any(letra in invalidChars for letra in word): #If NINGUNA letra of the word is in invalidChars, will into
            msg += 'Password must have one special character.\n'

        if not any(letra in lowercase for letra in word): #If NINGUNA letra of the word is in lowercase, will into
            msg += 'Password must have one lowercase character.\n'

        if not any(letra in uppercase for letra in word): #If NINGUNA letra of the word is in uppercase, will into
            msg += 'Password must have one uppercase character.\n'

        if not any(letra in digits for letra in word): #If NINGUNA letra of the word is in digits, will into
            msg += 'Password must have one number.\n'

        if len(word) < 6:
            msg += 'The Minimum length must be 6 characters.\n'
        elif len(word) > 16:
            msg += 'The Maximum length must be 16 characters.\n'
        else:
            pass

        if msg:
            print(msg)
        else:
            print('Your password is Ok !')
            x = False

validate_password()