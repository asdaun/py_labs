import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guessed = False

    print("Комп'ютер загадав число від 1 до 100. Спробуйте його вгадати!")

    while not guessed:
        user_guess = int(input("Введіть ваше число: "))
        
        if user_guess < number_to_guess:
            print("Моє число більше.")
        elif user_guess > number_to_guess:
            print("Моє число менше.")
        else:
            print("Ви вгадали!")
            guessed = True
