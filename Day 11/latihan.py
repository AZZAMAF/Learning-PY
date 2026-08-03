# Soal 1: "The Username Generator" (Manipulasi String & List)
# Soal:
    # Diberikan sebuah nama lengkap: "Azzam FrontEnd Dev".
    # Buat fungsi bernama buat_username(nama_lengkap) yang mengubah nama tersebut 
    # menjadi username sistem dengan ketentuan:
    #     Semua huruf diubah jadi huruf kecil (.lower()).
    #     Spasi diganti dengan garis bawah "_" (.replace(" ", "_")).
    #     Return string username jadinya (Contoh: "azzam_frontend_dev").

nama = "Azzam FrontEnd dev"

def make_username(full_name):
    # gua salah nya gak kasih spasi jirr di replace nya
    # username = full_name.lower().replace(" ", "_"). gini juga bisa kan 
    lower_text = full_name.lower()
    username = lower_text.replace(" ", "_")
    return username

print(make_username(nama))
    
# Soal 2: "The Age Grouping" (Kondisi Bertingkat / If-Elif-Else)
# Soal:Diberikan sebuah list umur orang: [12, 25, 40, 17, 60, 5].
# Buat fungsi bernama klasifikasi_umur(daftar_umur) yang melalukan looping dan mengembalikan sebuah Dictionary berisi pengelompokan 
# jumlah orang berdasarkan 
#   kategori:Umur < 13: masuk kategori "anak-anak"
#   Umur $13$ sampai $19$: masuk kategori "remaja"
#   Umur > 20: masuk kategori "dewasa"
#       Format Return: {"anak-anak": 2, "remaja": 1, "dewasa": 3} 
# (hitung jumlah orangnya di tiap kategori).

peopel = [12, 25, 40, 17, 60, 5]
# 1. TAMBAHKAN INI DI BARIS PALING ATAS FILE
from collections import Counter  

def klasifikasi_umur(list_age):
    result = []
   
    
    for age in list_age:
        if age < 13 :
            child = "anak anak"
            result.append(child)

        elif age <= 19: 
            teaneger = "Remaja"
            result.append(teaneger)
        else:
            adult = "dewasa"
            result.append(adult)
            
    # my mistake is i put these code in the top so the for in doesn't work kwkwkw
    # my_dict = dict(enumerate(result)) # ini mah untuk ngitung jumlah list nya cuk
    my_dict = {item: result.count(item) for item in set(result)}
# set : for deleted a duplicate item for the list and menyisakan unik item 
# bang kalau gak pake gimana pemborosan cok

    return my_dict
    # return  dict(Counter(result))
    
print(klasifikasi_umur(peopel))

# Soal 3: "The Cart Tax & Shipping Calculator" (Fungsi Kompleks & Matematika Finansial)
# Soal:
#     Buat fungsi bernama hitung_tagihan_akhir(total_belanja, member=False):
#         Jika status member bernilai True, berikan diskon member sebesar 10% 
#       dari total_belanja. 
# Jika False, tidak ada diskon.
#  Setelah dipotong diskon (kalau ada), tambahkan Pajak 11% dari harga setelah diskon tersebut.
#         Tambahkan Biaya Kirim tetap Rp 20.000 ke total akhir.
#         Return angka total akhir tagihannya.

def count_bill(shoping_total, member=False):
    discount = 10 / 100
    tax = 11 / 100
    shipping_cost = 20000
    if member == True: 
        shoping_total -= (shoping_total *discount)
        shoping_total += (shoping_total * tax)
        shoping_total += shipping_cost
        return shoping_total
    # shoping = shoping - discount
    else:
        shoping_total += (shoping_total * tax)
        shoping_total += shipping_cost
        return shoping_total

print(count_bill(100000, True))
#def count_bill(shoping_total, member=False):
#         # 1. Cek diskon member dulu
#     if member == True: 
#         shoping_total = shoping_total - (shoping_total * 0.10)
        
#     # 2. Hitung pajak dari harga terakhir (setelah diskon atau harga normal)
#     shoping_total = shoping_total + (shoping_total * 0.11)
    
#     # 3. Tambah ongkir tetap
#     shoping_total = shoping_total + 20000
    
#     return shoping_total

# print(count_bill(100000, True))
# # Output: 109900.0 (Diskon 10rb -> 90rb + Pajak 11% (9.9rb) + Ongkir 20rb)

# Soal 4: "The Unique Data Cleaner" (Set & List Dedup)
# Soal:
# Diberikan sebuah list tag artikel yang acak dan kembar-kembar:
# tags = ["python", "react", "javascript", "python", "css", "react", "html"].
# Buat fungsi bernama bersihkan_tag_duplikat(daftar_tag) yang:
#     Menghapus semua elemen yang kembar/duplikat (Hint: lu bisa manfaatkan set(daftar_tag) 
#   lalu ubah lagi jadi list(), atau looping cek manual).
#     Mengembalikan list baru yang isinya unik tanpa duplikat.

tags = ["python", "react", "javascript", "python", "css", "react", "html"]

def clean_log(data):
   clean_data = list(set(data))
   return clean_data

print(clean_log(tags))

# Soal 5: "The Ultimate Search Engine" (Pencarian Data / Linear Search)
katalog_produk = [
    {"id": 1, "nama": "Mechanical Keyboard RGB"},
    {"id": 2, "nama": "Wireless Mouse Gaming"},
    {"id": 3, "nama": "Monitor 24 Inch 144Hz"},
    {"id": 4, "nama": "Headset Gaming 7.1"},
    {"id": 5, "nama": "Mousepad Extended"}
]
# Buat fungsi bernama cari_produk(db_produk, kata_kunci)
# yang bertugas mencari produk berdasarkan kata kunci yang diketik user (misal "gaming").
#     Fungsi harus mengecek apakah kata_kunci (diubah ke .lower() biar aman) ada di dalam nama produk.
#     Jika ada, masukkan dictionary produk tersebut ke dalam list hasil.
#     Return list produk yang cocok.
def find_product(db_product, key_word):
    product = []
    for data in db_product:
        name_product = data["nama"].lower()
        # sumpah ini soal yang paling susah
        # karena gua gak ngerti urutan nya aja sih ternyata gampang bet
        if key_word in name_product:
               product.append(data)
               
    return product
# Padahal di soal diminta: "Masukkan dictionary produk tersebut ke dalam list hasil."
# Artinya, yang harus di-append adalah seluruh datanya (data), bukan cuma name_product-nya, biar struktur aslinya (beserta ID-nya) gak ilang.
test = find_product(katalog_produk, "gaming")               
print(test)