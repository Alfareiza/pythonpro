mylist = [10, 20, 30]


# Function definition is here
def changeme(mylist):
    "This changes a passed list into this function"
    mylist = [1, 2, 3, 4]  # This would assi new reference in mylist
    print("Values inside the function: ", mylist)
    # Como aqui no retorna nada, myList solo cambia dentro de la función
    pass


# Now you can call changeme function
changeme(mylist)
print('Values outside the function: ', mylist)
