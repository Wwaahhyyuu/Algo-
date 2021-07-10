kata = input("Enter a string: ")
panjang_kata = len(kata)
i = 0
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_spasi = 0
while i < panjang_kata:
    if(kata[i] == "a" or kata[i] == "A" or kata[i] == "A" or kata[i] == "i" or kata[i] == "I" or kata[i] == "u" or kata[i] == "U" or kata[i] == "e" or kata[i] == "E" or kata[i] == "o" or kata[i] == "O") :
        jumlah_vokal += 1
    elif (kata[i] == " "):
        jumlah_spasi += 1
    else :
        jumlah_konsonan += 1
    i+=1
print("Total Number of Vowels in user entered string is: ", jumlah_vokal)
print("Total Number of Consonant in user entered string is: ", jumlah_konsonan)
print("Total Number of Blanks in user entered string is: ", jumlah_spasi)