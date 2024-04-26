def palabra_palindroma(palindroma):
    return palindroma [::-1]

palabra =  input("Ingrese una palabra: ")
palabra_palindroma =  palabra_palindroma(palabra)
if  palabra == palabra_palindroma:
    print("La palabra es palindroma")
else:
    print("La palabra no es palindroma")