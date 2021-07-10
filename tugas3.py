word = input("Masukkan String : ")
result = ''
for i in range(len(word)):
    if word[i].isupper():
        result += word[i].lower()
    else:
        result += word[i].upper()

''
print(result)
