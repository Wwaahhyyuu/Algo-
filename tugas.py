print("Nama : Wahyu Agus Indrawati")
print("NIM  : 202410102064")
print("String dalam pemrograman komputer adalah sebuah deret simbol atau tipe data untuk teks yang merupakan gabungan huruf, angka, whitespace (spasi), dan berbagai karakter. String juga sering disebut sebagai “array of char”. Sedangkan tipe data string adalah tipe data yang digunakan untuk menyimpan barisan karakter. Pada bahasa python string diapit dengan tanda kutip tunggal maupun ganda. Fungsi ini digunakan untuk membuat identifier String/teks")
import random
nama = input("Masukkan Nama dan NIM: ").replace(" ", "")
vowel = {"vocal":"AIUEOaiueo"}
tampung = {"total":0}
huruf = []
nilai = 0
tampung_soal4 = []
for i in nama:
    angka = i.isdecimal()
    if i in vowel["vocal"]:
        tampung["total"] += 1
    if angka == False:
        nilai += 1
while True:
    angka_random = random.randint(1, nilai)
    if nama[angka_random].isalpha():
        huruf.append(nama[angka_random])
    if len(huruf) == random.randint(10, 20):
        for i in range(0, random.randint(1, 3)):
            tampung_soal4.append(huruf[random.randint(0, len(huruf) - 1)])
        break
jumlah_ascii = (ord(max(nama)) - int(nama[len(nama)-2:])) * (tampung["total"]//2)
for j in vowel["vocal"]:
    nama = nama.replace(j, "o")
print("Soal No1:",tampung["total"])
print("Soal No2:",jumlah_ascii)
print("Soal No3:","".join(huruf))
print("Soal No4:","".join(tampung_soal4).upper())
print("Soal No5:",nama+nama[-1:-8])
