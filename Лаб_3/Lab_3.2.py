def max_consecutive_chars(word):
    max_count = current_count = 1

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            current_count += 1
        else:
            current_count = 1
        max_count = max(max_count, current_count)

    return max_count

word = str(input("Введіть слово: "))
result = max_consecutive_chars(word)

print(f"Найбільша кількість однакових символів підряд: {result}")
