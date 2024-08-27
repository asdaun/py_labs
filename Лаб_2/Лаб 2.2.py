import math
from game_module import guess_the_number

def calculate_z(m):
    z = (math.sqrt(2) - math.sqrt(3 * m)) / (2 * m)
    return z

def main():
    m = float(input("Введіть значення m: "))
    z = calculate_z(m)
    print(f"Значення z: {z}")
    
    guess_the_number()

if __name__ == "__main__":
    main()
