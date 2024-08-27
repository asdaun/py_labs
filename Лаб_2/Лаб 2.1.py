import math
import random

def calculate_z(m):
    z = (math.sqrt(2) - math.sqrt(3 * m)) / (2 * m)
    return z

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

def main():
    # Введення значення m
    m = float(input("Введіть значення m: "))
    z = calculate_z(m)
    print(f"Значення z: {z}")
    
    guess_the_number()

if __name__ == "__main__":
    main()
