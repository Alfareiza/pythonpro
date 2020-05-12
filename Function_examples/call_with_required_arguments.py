# Function definition is here
def printme( str ): #Si aqui se le coloca str, al ser llamada la función se le debe enviar algo (string, int, etc)
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
printme([1,2,3])

#Esto dará el error "TypeError: printme() missing 1 required positional argument: 'str' "
