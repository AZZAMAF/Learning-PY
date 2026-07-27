# # Dictionary Looping (.items()): Di Python,
# kalau lu punya data dictionary (pasangan key-value seperti nama barang dan harga), 
# lu bisa nge-loop key dan valuenya sekaligus pakai .items().
#     Contoh: for nama, harga in data_barang.items():
# Kondisi Kombinasi (and): Kadang kita butuh menyaring data berdasarkan dua syarat sekaligus. 
# Kita bisa pakai kata kunci and di dalam if.

    # Contoh: if harga > 1000 and status == "tersedia":
    
    # # Buatlah sebuah fungsi bernama cari_buah_terjangkau(data_buah) yang bertugas untuk:
    # Melakukan looping pada dictionary tersebut menggunakan .items().
    # Menyaring buah yang harganya di bawah 10.000 saja.
    # Memasukkan nama buahnya saja (hanya key-nya) ke dalam sebuah list kosong ([]) menggunakan .append().
    # Mengembalikan (return) list nama buah yang sudah disaring tersebut.
toko_buah = {
    "apel": 5000,
    "jeruk": 3000,
    "mangga": 12000,
    "pisang": 4000,
    "semangka": 25000
}

def cari_buah_terjangkau(data_buah):
    nama_buah = []
    for key, value in data_buah.items():
        if value <= 10000:
            nama_buah.append(key)
            
    return nama_buah

print(cari_buah_terjangkau(toko_buah))

# Part 2: "The Category Counter" (Pencatat Kategori Produk)

# Materi yang harus lu pahami / cari tahu:
#     Looping Dictionary: Sama seperti sebelumnya, kita pakai 
# .items() buat ngambil nama barang dan datanya.
#     Kondisi Kompleks: Di dalam loop, kita bisa ngecek bagian tertentu dari nilai dictionary
# (misalnya mengecek status atau kategori barang).
#     Counter (+= 1): Menggabungkan teknik hitung jumlah yang sempat kita bahas di awal tadi.
#     
# Soal:
#     Diberikan sebuah data dictionary yang berisi daftar produk beserta status ketersediaannya:
inventaris_toko = {
    "laptop": "tersedia",
    "mouse": "habis",
    "keyboard": "tersedia",
    "monitor": "habis",
    "headset": "tersedia",
    "webcam": "tersedia"
}
# Buatlah sebuah fungsi bernama hitung_barang_tersedia(data_inventaris) yang bertugas untuk:
    # Membuat variabel counter awal dengan nilai 0 (misal jumlah_tersedia = 0).
    # Melakukan looping pada dictionary tersebut menggunakan .items().
    # Mengecek jika status barangnya adalah "tersedia", maka tambahkan nilai counter dengan 1 
    # (+= 1).
    # Mengembalikan (return) total angka dari counter tersebut setelah looping selesai.
    
def hitung_barang_tersedia(data_inventaris):
    count = 0
    for  status in data_inventaris.values():
        if status == "tersedia":
            count +=1
    return count
# use values() kalau mau cuman ambil value nya aja
#  emg kenapa sih harus di kasih items(). iyasih ini untuk aktifin biar value nya bisa di ambil tapi kan gak efesien
print(hitung_barang_tersedia(inventaris_toko))


# Soal:
# Diberikan sebuah data dictionary status pengerjaan tugas modul:
status_tugas = {
    "modul_html": "selesai",
    "modul_css": "belum",
    "modul_js": "selesai",
    "modul_react": "belum",
    "modul_git": "selesai"
}
# Buatlah sebuah fungsi bernama ambil_tugas_selesai(data_tugas) yang bertugas untuk:
#     Menyiapkan list kosong ([]) untuk menampung data.
#     Melakukan looping pada dictionary tersebut (pikirkan mau pakai .items() atau .values() yang paling pas).
#     Menyaring tugas yang statusnya "selesai" saja.
#     Jika statusnya "selesai", ambil nama tugasnya (key-nya), ubah jadi huruf kapital semua pakai 
# .upper(), lalu masukkan ke list kosong tadi pakai .append().
#     Mengembalikan (return) list nama tugas yang sudah berhuruf kapital tersebut.

def take_finish_work(work_data):
    final_data = []
    for key,status in work_data.items():
        if status == "selesai":
            changeKeydata = key.upper() # mengubah from small to big capital 
            final_data.append(changeKeydata) # put in the empty list in var final_data
    return final_data
print(take_finish_work(status_tugas))

keranjang_belanja = [
    {"nama": "Mechanical Keyboard", "harga": 500000, "jumlah": 1, "diskon": True},
    {"nama": "Mouse Gaming", "harga": 250000, "jumlah": 2, "diskon": False},
    {"nama": "Mousepad XL", "harga": 100000, "jumlah": 3, "diskon": True},
    {"nama": "Headset Stand", "harga": 150000, "jumlah": 1, "diskon": False}
]

# Buatlah sebuah fungsi bernama hitung_total_belanja(keranjang) yang bertugas untuk:
#     Menyiapkan variabel tracker angka untuk menampung total harga akhir 
# (misal total_harga = 0).
#     Melakukan looping untuk mengecek setiap item (dictionary) 
# yang ada di dalam list keranjang.
#     Di dalam loop, hitung subtotal awal untuk tiap barang: harga * jumlah.
#     Aturan Diskon:
#         Jika status diskon bernilai True, maka subtotal barang tersebut 
# dipotong 10% (artinya harga dikali 0.9).
#         Jika False, harga tetap seperti biasa tanpa potongan.
#     Tambahkan hasil subtotal (setelah diskon atau tidak) ke variabel total_harga utama (pakai +=).
#     Mengembalikan (return) nilai total_harga keseluruhan setelah semua item dihitung.

def count_shopping_total(chart):
    price_total = 0
    for items in chart: 
        price = items["harga"]
        amount = items["jumlah"]
        subtotal = price * amount
        if items["diskon"] == True:        
            diskon = subtotal * 0.9
            price_total += diskon
            
        else:
            price_total += subtotal
    return price_total
#  += ini berfungsi menambah nilai ke sebuah variabel ex: pricetotal += subtotal //OR// pricetotal = pricetotal + subtotal 
        
print(count_shopping_total(keranjang_belanja))

data_transaksi = [
    {"produk": "Laptop ASUS", "kategori": "Elektronik", "harga": 7000000, "terjual": 2},
    {"produk": "Kemeja Flanel", "kategori": "Pakaian", "harga": 150000, "terjual": 5},
    {"produk": "Mouse Wireless", "kategori": "Elektronik", "harga": 200000, "terjual": 10},
    {"produk": "Celana Jeans", "kategori": "Pakaian", "harga": 300000, "terjual": 3},
    {"produk": "Kopi Susu Literan", "kategori": "Kuliner", "harga": 50000, "terjual": 8}
]

# Buatlah sebuah fungsi bernama rekap_pendapatan_kategori(transaksi) yang bertugas untuk:
#         Menyiapkan sebuah dictionary kosong penampung (misal rekap = {}).
#         Melakukan looping pada list transaksi.
#         Di dalam loop, hitung total omset per baris transaksi: harga * terjual.
#         Ambil kategori produk tersebut (misal "Elektronik", "Pakaian", atau "Kuliner").
#         Masukkan hasil perhitungan omset tersebut ke dalam dictionary rekap berdasarkan kategorinya.
#             Aturan Kunci: Jika kategori tersebut belum ada di dalam rekap, buat key baru dengan nilai awal omset tersebut. 
# Jika kategorinya sudah ada, tambahkan omset baris itu ke nilai yang sudah ada sebelumnya (+=).
#         Mengembalikan (return) dictionary rekap yang berisi total omset per kategori.

def recap_income_category(transaction):
    recap = {}
    
    for data in transaction:
        price = data["harga"]
        sold = data["terjual"]
        omset = price * sold
        category = data["kategori"]
        print(omset)
        
        print(category)
        if category not in recap:
            recap[category] = omset
        else: 
            recap[category] += omset
    return recap
print(recap_income_category(data_transaksi))