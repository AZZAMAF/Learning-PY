# 1.Penjumlah: Buat fungsi yang menerima 2 angka dan mengembalikan hasil penjumlahannya.

def addition(a,b):
    c = a + b 
    print(c)    
addition(1,2)

# Genap/Ganjil: Buat fungsi yang menerima satu angka, 
# kembalikan "Genap" jika genap, dan "Ganjil" jika ganjil.

def evenOdd(x):
    if x % 2 ==0:
        print("Genap")
    else:
        print("Ganjil")
    
# end def
evenOdd(1)

# Huruf Pertama: Buat fungsi yang menerima satu kata, kembalikan huruf pertamanya saja.
def oneWord(word):
    
    # print(word[0])
    return word[0]
    # kenapa return gak jalan jirr

result = oneWord('hallo')
print(result)

# Luas Persegi: Buat fungsi yang menerima sisi persegi, kembalikan luasnya (sisi * sisi).
def ractangel(a):
    Luas = a * a
    return Luas

result = ractangel(12)

print(result)

# Cek Nama: Buat fungsi yang menerima nama. Jika namanya "azzam", cetak "Halo bos", 
# jika bukan, cetak "Halo orang asing".

def bosName(name):
    if name == "azzam":
        return "Hallo Bos"
    else:
        return "Hallo orang Asing"
    
Hallobos = bosName("azzam")
print(Hallobos)

# Pilih Angka Besar: Buat fungsi yang menerima 2 angka, kembalikan angka yang paling besar.
def bigNumber(a,b):
    if a >= b:
        return a
    elif b >= a:
        return b

angkaBesar = bigNumber(12,32)
print(angkaBesar)

# Sapaan: Buat fungsi yang menerima nama dan umur,
# kembalikan string "Halo [nama], tahun depan umurmu [umur+1] tahun".

def greetings(name, age):
    return print(f"Halllo {name},tahun depan umurmu {age+1} tahun ")

greetings("anna",12)

# Hitung Panjang Kata: Buat fungsi yang menerima sebuah kata, 
# kembalikan berapa jumlah huruf dalam kata tersebut (Hint: pakai len()).
def aWord(word):
    lengthWord = len(word)
    return print(lengthWord)

aWord("hello")

# Ubah ke Detik: Buat fungsi yang menerima menit, kembalikan jumlah detiknya (menit * 60).
def minute(m):
    scnd= m * 60
    return print(scnd)

minute(12)

# Filter List: Diberikan list [1, 5, 10, 20], 
# buat fungsi untuk mengambil angka yang lebih besar dari 5 saja.

number = [1,5,10,20]
def collectNumber(n):
    for n in number:
        if n >= 5:
            print(n)
        
        
collectNumber(number)
    