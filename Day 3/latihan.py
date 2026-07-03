# Problem 2.3: Menggabungkan Keduanya (List of Dictionaries)
# Ini adalah level up. Di dunia nyata, biasanya kita tidak menyimpan data terpisah. 
# Kita menyimpan List yang berisi banyak Dictionary. 
# Ini adalah bentuk dasar dari data JSON yang dipakai hampir di semua website.
# Tugas:
#     Buat variabel bernama database_teman yang isinya List (tanda []).
#     Di dalam List tersebut, masukkan 2 Dictionary (tanda {}) yang masing-masing berisi nama dan umur.
#         Contoh: [{"nama": "Azzam", "umur": 20}, {"nama": "Rafi", "umur": 21}]
#     Print umur dari teman kedua (indeks ke-1)

friendsDB = [
    {"name" :"Azzam", "age": 20},
    {"name" :"alex", "age" :21}
]
print(friendsDB[1]["age"])

# Problem 2.4: Update Data
#     Dari Dictionary friendsContact yang kamu buat tadi, coba ubah nomor telepon "ken" menjadi 1111111.
#     (Hint: Caranya sama seperti membuat data baru, cukup akses key-nya lalu beri nilai baru dengan =).
#     Print friendsContact setelah diubah.

friendsContact  ={
    "ken" : 813192012,
    "san" : 813193212,
    "ran" : 8123901234,
}
friendsContact["ken"] = 11111111
print(friendsContact["ken"])

