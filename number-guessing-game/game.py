import random

num = input("Type a number: ")

# Sjekk at input er et gyldig tall over 0
if num.isdigit():
    num = int(num)

    # Hvis tallet er mindre enn null
    if num <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
# beskjed-melding
else:
    print("Please type a number next time.")
    quit()

# Genererer vinnertallet fra 0 til num (0-20 hvis num=20)
random_num = random.randint(0, num)
count_guesses = 0

# While True brukes til å kjøre helt til spillet er ferdig gjennomført.
# Vi velger ett tall, og vi gjetter på tallet helt til vi har funnet det. Da stopper break-kommandoen løkken.
while True:
    count_guesses += 1
    user_guess = input("Make a guess: ")
    
    # Validerer gjettet
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    # Sjekker gjettet mot vinnertallet
    if user_guess == random_num:
        print("You got it!")
        break
    # Her stopper break commandoen while løkken
    elif user_guess > random_num:
        print("number is lower")
    else:
        print("number is higher")

# Printer totalt antall forsøk
print(f"You got it in {count_guesses} guesses!")
