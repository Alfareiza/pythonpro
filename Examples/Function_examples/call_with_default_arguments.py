# Function definition is here
def printinfo(name, age=35):  # En llamados por default, se hacen este tipo de atribuciones en la definición de función
    # Primero se colocan las non-feault y luego los defult arguments
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return


# Now you can call printinfo function
printinfo(age=50, name="miki")  # Estos valores son enviados a la función y esta no los cambiará
printinfo(name="miki")  # Como no se envió 'age', la función asumirá que esta es 35 pq ha sido declarada allí
