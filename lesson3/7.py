def int_func(words):
    for i in range(len(words)):
        words[i] = words[i].title()
    return words


wrong_word = False
while True:
    words = input("Введите строку со словами из латинских букв в нижнем регистре:").split()
    for word in words:
        for letter in word:
            num_let = ord(letter)
            if num_let < 97 or num_let > 122:
                print("Слова должны состоять из маленьких латинских букв")
                wrong_word = True
                break
        if wrong_word:
            break
    if wrong_word:
        wrong_word = False
        continue
    break

words = int_func(words)
str = ""
for word in words:
    str += word + " "

print(str.strip())