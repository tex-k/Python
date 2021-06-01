def int_func(words):
    for i in range(len(words)):
        words[i] = words[i].title()
    return words


words = []
wrong_word = False
while True:
    word = input("Введите слово из маленьких латинских букв (или * для остановки): ")
    if word == "*":
        break
    for letter in word:
        num_let = ord(letter)
        if num_let < 97 or num_let > 122:
            print("Слово должно состоять из маленьких латинских букв")
            wrong_word = True
            break
    if wrong_word:
        wrong_word = False
        continue
    words.append(word)

print(int_func(words))
