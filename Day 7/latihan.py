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
    for n in listNumber1:
        if n >= 20:
            print(n)
            return n 
            
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
def urutkan_vokal(letter):
    # Ubah string menjadi list agar bisa di-sort
    list_huruf = list(letter)
    
    # Elemen vokal diberi prioritas 0 (di depan), konsonan diberi prioritas 1 (di belakang)
    list_huruf.sort(key=lambda x: 0 if x.lower() in 'aiueo' else 1)
    
    # Gabungkan kembali list menjadi string
    return "".join(list_huruf)

print(urutkan_vokal('akai'))
# Hasil: 'aaik' (vokal 'a', 'a', 'i' pindah ke depan, konsonan 'k' ke belakang)
# gua nyerah itu hasil ai