def swap_first_last(sentence):
    words = sentence.split()
    
    if len(words) == 1:
        print("Речення містить тільки одне слово. Зміна не потрібна.")
        return
    
    words[0], words[-1] = words[-1], words[0]

    swapped_sentence = ' '.join(words)
    print(swapped_sentence)

input_sentence = input("Введіть речення: ")

swap_first_last(input_sentence)
