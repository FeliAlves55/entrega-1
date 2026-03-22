import random
import string 

rango = string.ascii_letters
categories = {
"Programacion": ["python","programa","variable","funcion","bucle"],
"Valores": ["cadena","entero","lista",]
}

print("¡Bienvenido al Ahorcado!")
print()
print("Categorias:" )
#Mostrar Categorias
for elem in categories:
    print("|",elem)
category_ch = input("Escribe el nombre de la categoria a jugar: ")

#Fijarse que este dentro de las categorias
while category_ch not in categories:
    category_ch = input("La categoria es incorrecta eliga de nuevo: ")

#Seleccion de palabra al azar
category_play = categories[category_ch]
words_mix= random.sample(category_play, len(category_play))

index= 0
puntaje = 0

while index < len(words_mix):
    guessed = []
    attempts = 6
    word = words_mix[index]
    
    while attempts > 0 :

        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje = puntaje + 6
            print(f"Tu puntaje es de: {puntaje}")
            print()
            ask = input("Quieres volver a jugar?| si/no: ")
            if ask == "si":
              index +=1
              guessed = []
              attempts = 6
              word = words_mix[index]
            elif ask == "no":
              print()
              print("Buen juego hasta pronto!") 
              break

        else:
         print(f"Intentos restantes: {attempts}")
         print(f"Letras usadas: {', '.join(guessed)}")
         letter = input("Ingresá una letra: ")
         if letter in guessed:
            print("Ya usaste esa letra.")
         if len(letter) == 1 and letter in rango:
            if letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")
                puntaje = puntaje - 1
         else:
            print()
            print("¡¡Entrada no valida!!.")
        print()

    print(f"¡Perdiste! La palabra era: {word}")
    puntaje = 0
    print(f"Tu puntaje es de: {puntaje}")
    print()
    ask = input("Quieres volver a jugar?| si/no: ")           
    if ask == "si":
        index +=1
    elif ask == "no":  
        print()      
        print("Buen juego hasta pronto!") 
        break