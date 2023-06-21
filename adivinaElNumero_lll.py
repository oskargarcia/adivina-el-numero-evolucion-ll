num = int(input("Ingresa el numero a adivinar ==>  "))
intentos = int(input("\nIngresa los intentos a realizar ==>  "))
min = int(input("\nIngresa el rrango minimo ==> "))
max = int(input("\nIngresa el rango maxino == > "))
print("-"*20)
print(f"¡Bienvenido! Por favor ingrese números entre {min} y {max} para ganar.\n")
while intentos > 0 :
    print(f"Intentos restantes: >> {intentos} <<")
    numero = int(input("Cual es el numer?  "))
    if numero in range(min, max+1) :
        if numero == num :
            print("**¡Felicidades!** El número ingresado es correcto.")
            break
        else:
            intentos -= 1
            if intentos == 0 :
                print(f"Se acabaron los intentos. El número correcto era {num}.")
            else:
                if numero > num :
                    print("Respuesta incorrecta. El número que ingresó es >> mayor << que el número secreto.")
                else :
                    print("Respuesta incorrecta. El número que ingresó es >> menor << que el número secreto.")         
    else:
        print("El número que ingresó no se encuentra en el rango de valores indicado. Intente nuevamente")
print("Fin del juego. ¡Gracias por participar!")
