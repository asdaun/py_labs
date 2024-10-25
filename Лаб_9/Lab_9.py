import string

def create_file_TF1_1():
    lines = [
        "Hello, world! This is a test file.",
        "Python programming is fun; let's learn more!",
        "File handling in Python is essential.",
        "End of the file... or is it?"
    ]
    
    with open("TF1_1.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")

def process_file_TF1_1_to_TF1_2():
    try:
        with open("TF1_1.txt", "r") as file1:
            content = file1.readlines()

        with open("TF1_2.txt", "w") as file2:
            for line in content:
                words = line.translate(str.maketrans('', '', string.punctuation)).split()
                for word in words:
                    file2.write(word + "\n")
    
    except FileNotFoundError:
        print("Error: The file TF1_1.txt was not found.")

def read_and_print_TF1_2():
    try:
        with open("TF1_2.txt", "r") as file2:
            print("Contents of TF1_2.txt:")
            for line in file2:
                print(line.strip())
    
    except FileNotFoundError:
        print("Error: The file TF1_2.txt was not found.")

create_file_TF1_1()
process_file_TF1_1_to_TF1_2()
read_and_print_TF1_2()
