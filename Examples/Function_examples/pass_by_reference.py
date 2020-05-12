# Function definition is here
def changeme(mylist):
    "This changes a passed list into this function"
    print("Values inside the function before change: ", mylist)

    mylist[2] = 50
    print("Values inside the function after change: ", mylist)
    return

# Now you can call changeme function
mylist = [10, 20, 30]
changeme(mylist) #Aqui llama la función y le envía -> myList
print("Values outside the function: ", mylist)

#Concusión: Cuando se le envía un valor a una función este regresa cambiado