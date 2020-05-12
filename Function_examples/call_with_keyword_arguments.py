# Function definition is here -----------------------------------
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
printme( str = "My string")

# Other Function definition is here -----------------------------
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age = 50, name = "miki" ) # llamado por keyword consiste en enviar los valores desde el llamado de la función
                                     # El orden como son enviados los parámetros no importa
                                     # El nombre de la variable debe ser el mismo que recibe la función (age, miki).
