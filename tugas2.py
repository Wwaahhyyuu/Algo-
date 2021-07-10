masukkan_kata = input("Enter a Setence: ")
jadikan_list = masukkan_kata.split()
hitung_kata = len(jadikan_list)

huruf_besar = 0
huruf_kecil= 0
jumlah_angka= 0
for kar in masukkan_kata :
    if kar.isupper():
        huruf_besar += 1 
    if kar.islower():
        huruf_kecil += 1  
    if kar.isdecimal():
        jumlah_angka += 1 
print("Number of digits in sentence is=", jumlah_angka) 
print("Number of words in sentence is=", hitung_kata)  
print("Number of upper case letters in sentence is=", huruf_besar)
print("Number of lower case letters in sentence is=", huruf_kecil)
