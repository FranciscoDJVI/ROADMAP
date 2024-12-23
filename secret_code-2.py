import random

letter_1 = "ABC"
letter_2 = "ABC"

nums_1 = "123"
nums_2 = "123"

digit_1 = random.choice(letter_1)
digit_2 = random.choice(letter_2)
digit_3 = random.choice(nums_1)
digit_4 = random.choice(nums_2)

code_initial = digit_1 + digit_2 + digit_3 + digit_4

print(
    """Bienvenido al juego del código secreto de papanoeal.En el cúal tendrás que ingresar un código que contenga dos letras entre "ABC" y dos números entre "123" y tratar de adivinar el secreto\n,Tienes 10 intentos!!! Buena suerte...\n"""
)
# print(code_initial)
counter = 1
correct = 0
while counter <= 10:
    code_user: str
    code_user = input(f"Intento #{counter}. Ingrese el codigo: ").upper()
    if len(code_user) < 4 or len(code_user) > 4:
        raise ValueError("Error el código debe tener 4 digitos")

    print("\nCódigo secreto")
    print(f"{code_initial}\n")
    print("Código ingresado por el usuario")
    print(code_user)

    aciertos = 0
    aciertos_list = []

    for index, caracter in enumerate(code_initial):
        pass

    for index, caracter in enumerate(code_user):
        if caracter == code_initial[index]:
            aciertos += 1
            aciertos_list.append("*")

            print(f"\nEl caracter {caracter} es correcto y esta en la posicion {index}")
            print(f"Aciertos {aciertos_list}\n")
        else:
            print(f"El caracter {caracter} no es correcto")
            print("No tienes aciertos\n")

    if aciertos == 4:
        print("Código resuelto")
        break
    counter += 1
