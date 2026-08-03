# Soal 1: "The Discount Hunter" (Fungsi dengan Multi-Parameter)
# Soal:
# Buat fungsi bernama hitung_harga_setelah_diskon(harga_asli, persentase_diskon)
# yang menerima harga barang dan diskon (dalam bentuk persen, misal 20 untuk 20%).
#     Rumus: harga_asli - (harga_asli * (persentase_diskon / 100))
#     Return: Kembalikan hasil angka akhirnya.
#     Test Case: hitung_harga_setelah_diskon(200000, 25) harus menghasilkan 150000.0.

def count_price_after_discount(real_price, discount_persentance):
    real_price = real_price - (real_price * (discount_persentance / 100)) 
    # i'm not understand what is this / 100 = apakah discount = 100 gitu ya
    # intinya harus di ubah jadi per 100 kalau mau hitung persen di komputer
    # Nggak, bro! Maksud / 100 itu karena diskon dalam soal ditulis pakai angka bulat biasa (misal 25 buat 25%). Nah, di dalam matematika komputer, kalau kita mau ngitung persen dari suatu angka, bentuk persen itu harus diubah dulu jadi desimal (pecahan dari 100).
    return real_price

print(count_price_after_discount(20000, 25))

# Soal 2: "The Odd-Even Separator" (Pemisah Angka Ganjil & Genap)
# Soal:
# Diberikan sebuah list angka: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Buat fungsi bernama pisahkan_ganjil_genap(list_angka) yang  
# memproses list tersebut dan mengembalikan sebuah Dictionary dengan format:
# {"genap": [2, 4, ...], "ganjil": [1, 3, ...]}.

angka= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def separete_odd_even(list_number):
    list_odd = []
    list_even = []
   
    for number in list_number :
        if number % 2 == 0 :
            list_even.append(number)
        else:
            list_odd.append(number)
            #  gua tau ini secara penulisan gak gini jelek ya, tau gua heheh tapi biar enak aja bacanya
    return  print(f"genap :  {list_even} ganjil :  {list_odd}")

separete_odd_even(angka)

# Soal 3: "The Short-Word Filter" (Penyaring Kata Pendek)\
    # Soal:
# Diberikan sebuah list kalimat/kata: ["aku", "suka", "pemrograman", "python", "dan", "react"].
# Buat fungsi bernama ambil_kata_pendek(daftar_kata) yang menyaring dan 
# hanya mengambil kata-kata yang jumlah hurufnya kurang dari atau sama dengan 4 (len(kata) <= 4),
# lalu masukkan ke list baru dan return hasilnya.

kata =  ["aku", "suka", "pemrograman", "python", "dan", "react"]

def take_short_word(word_list):
    newListword = []
    
    for word in word_list:
        if len(word) <= 4 :
            newListword.append(word)
    return newListword

print(take_short_word(kata))

# Soal 4: "The Passing Grade Checker" (Penyaring Kelulusan Siswa)
data_siswa = [
    {"nama": "Budi", "nilai": 75},
    {"nama": "Ani", "nilai": 88},
    {"nama": "Joko", "nilai": 50},
    {"nama": "Siti", "nilai": 92}
]
# Buat fungsi bernama cari_siswa_lulus(data) yang mengembalikan list nama siswa (key "nama") 
# yang nilainya di atas atau sama dengan 70 (>= 70).

def find_student_graduation(data):
    student_name = []
    for siswa in data:
        if siswa["nilai"] >= 70:
            student_name.append(siswa["nama"])
    return student_name
print(find_student_graduation(data_siswa))

# Soal 5: "The Inventory Value Calculator" (Kalkulator Valuasi Stok)
gudang = [
    {"item": "Laptop", "harga": 5000000, "stok": 3},
    {"item": "Mouse", "harga": 100000, "stok": 10},
    {"item": "Keyboard", "harga": 300000, "stok": 5}
]
# Buat fungsi bernama hitung_total_aset(data_gudang) yang menghitung total nilai seluruh aset 
# di gudang (rumus per item: harga * stok, lalu seluruh item dijumlahkan total keseluruhannya). 
# Return angka total akhirnya.

def total_assets_counter(data):
    result_total = 0 
    
    # pantes tadi error ini tadi gua jadiin list kosong bukan nol hehehe
    for item in data:
        item_price = item["harga"] * item["stok"]
        result_total += item_price
        # remember = result = result + itemprice 
        
    print(f"result_total : {result_total}")
    return result_total
    
total_assets_counter(gudang)