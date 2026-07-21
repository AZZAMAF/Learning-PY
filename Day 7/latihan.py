#1. Balik List: Buat fungsi yang menerima list [1, 2, 3], 
# kembalikan [3, 2, 1]. (Hint: list.reverse() atau slicing [::-1]).

listNumber = [1, 2, 3]

def listReturn(list):
    list.reverse()
    return list

result = listReturn(listNumber)
print(result)

# 2.Cari Nilai Maksimum: Tanpa pakai max(), 
# cari angka terbesar di list [10, 5, 20, 2]. 
# (Hint: looping, simpan angka terbesar sementara di satu variabel).

listNumber1 = [10, 5, 20,2 ]

def findBignumber(list):
    for n in list:
        if n >= 20:
            print(n)
            return 
            
findBignumber(listNumber1)

# 3.Gabung List: Diberikan dua list, gabungkan menjadi satu list unik.
listUnic = list(set(listNumber + listNumber1))
# fungsi set disini agar tidak menjalankan number yang sudah ada atau duplikasi
# list mengubah bentuk format dari set{} to []

print(listUnic)

# Cek Palindrome: Buat 
# fungsi yang mengecek apakah sebuah kata dibaca sama dari depan maupun belakang (contoh: "katak").

def palindrome(data):
    kataTerbalik = "".join(reversed(data))
    if data == kataTerbalik:
        return print("sama")
    else:
        return print("tidak sama")
# fungsih "".join() berfungsi untuk menggabungnkan data yang terpecah karena reversed
# yang menghasilkan object iterator yang dimn huruf2 itu terpecah pecah

palindrome('nenek')

# Hitung Vokal: Hitung jumlah huruf vokal (a, i, u, e, o) dalam sebuah kata.
# def vokal(letter):
#     word= letter
#     word.sort(key=lambda x:(x['a'],x['i'],x['u'],x['e'],x['o']))


# vokal('akai')
def vokal(letter):
    vowels = "aiueo"
    # Menghitung huruf jika huruf tersebut ada di dalam teks "aiueo"
    jumlah = sum(1 for char in letter.lower() if char in vowels)
    return jumlah

# Panggil fungsi dan cetak hasilnya
print(vokal('akai'))  
# Hasil: 3 (karena ada 'a', 'a', 'i')
# gua nyerah itu hasil ai

# Dictionary Lookup: Diberikan data { "apel": 5000, "jeruk": 3000 }, buat fungsi untuk mengecek harga barang berdasarkan nama.
buah ={ "apel": 5000, "jeruk": 3000 }

def checkBuah(data):
    
   for key, value in buah.items():
    # .items() : berfungsi sebagai pembuka gerbang key, value di dictionary sehingga dapat di gunakan
       if key == data :
           print(value)
           return 
    #    else:
    #        print("buah not found ")
    #        return 
               
    # 2. Taruh 'else' atau pesan tidak ketemu di LUAR perulangan 'for'
    # Baris di bawah ini HANYA akan dieksekusi jika perulangan di atas selesai 
    # dan tidak ada satu pun key yang cocok.
print("buah not found")
    
checkBuah("mangga")
# gak tau kenapa appel jalan lancar 5000 keluar harganya tapi jeruk gak cok
def checkBuahSimpel(data):

    if data in buah:
        print(buah[data])  # Langsung ambil harganya pakai key
    else:
        print("buah not found")
#  ini AI
checkBuahSimpel("apel")

# Filter Genap ke List Baru: Mirip nomor 10 tadi, tapi simpan hasilnya ke list baru ([]) lalu return list tersebut.
number = [1,5,10,20]

def filterGenap(angka):
    angkaList = []
    for n in angka:
        #  n = angka di delem number
        if n >= 5 :
            angkaList.append(n)
            # note: jangan masukan angkaList ke dalam for karena aka melakukan pengulangan lagi yang hasilnya []
            # append use for add value in []
    print(angkaList)
filterGenap(number)

# Double Nilai: Terima list angka, kembalikan list baru yang isinya dikali 2 semua.
listAngka = [2,4,5,7,8]
def kaliAnkaList(number):
    emptList = []
    for n in number:
    # para maternya : n looping yang ada di dalem number : number = listangka : listangka = nomor itu
        kali = n*2
        emptList.append(kali)
        # ingat append untuk memasukan value ke dalam list
    print(emptList)
        
kaliAnkaList(listAngka)
# FizzBuzz Sederhana: Loop dari 1 sampai 15. Jika angka bisa dibagi 3, 
# print "Fizz", kalau bagi 5 print "Buzz", kalau bagi keduanya print "FizzBuzz".

def fizbuzz():
    for n in range(1,16):
        # print(n)
        if n % 3 == 0 and n % 5 == 0:
            #  kenapa ada 0 if angka modulus itu hasil bagi ya, ex 10 % 3 = 1 modulusnya 1
            # 1 == 0 itu true gitu coyy jadi == 0 berfungsi untuk parameter itu ya apakah habis atau engga
            # kalau ada sisa berarti jadi false jadi angka itu tidak habis di bagi 3
            print('Fizzbuzzz')
        elif n % 5 == 0:
            print('Buzz')
        elif n % 3 == 0 :
            print('fizz')
        else:
            print(n)
#  gua gak tau ini kenap fizzbuzz nya gak jalan jirr 
# fungsi elif di sini bertujuan agar setiap angka hanya menghasilkan SATU output saja (tidak dobel-dobel), 
# dengan catatan kondisi yang paling spesifik wajib ditaruh di paling atas.
fizbuzz()
# Hapus Duplikat: Terima list [1, 2, 2, 3, 4, 4], kembalikan [1, 2, 3, 4].
oldList = [1, 2, 2, 3, 4, 4]

def newList(data):
    new_list = list(set(data))
    print(new_list)
    return
    
newList(oldList)