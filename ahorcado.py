# juego del ahorcado wiiiiiiii
#1- definir una palabra
#2-numero definido de intentos
#3- pedir al usuario que ingrese una letra a la vez
#resultado de acierto o de perdida


def ahorcado():
    #definimos
    palabra_secreta = "machi"
    letras_adivinadas = []
    #lista es para almacenar las letras que concuerden con mi palabra
    intentos = 5 #número de intentos

    while intentos > 0:
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_ "
        print(palabra_mostrada)

        if palabra_mostrada == palabra_secreta:
                print("has adivinado la palabra")
                break

            #pedir al usuario una letra
        letra_usuario = input ("Ingrese una letra: ")

            #verificar si la letra a sido adivinada en letras vacías
        if letra_usuario in letras_adivinadas:
                print("ya has adivinado esa letra")
                continue
        if letra_usuario in palabra_secreta:
                print("Bien, tú letra está en la palabra")
                letras_adivinadas.append(letra_usuario)
        else: 
                intentos -= 1
                print(f"incorrecto, te quedan {intentos} intentos")

        if intentos == 0:
                print(f"Lo siento, has perdido, la palabra secreta era {palabra_secreta}")

    #llamar a la función
ahorcado()
