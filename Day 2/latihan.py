# Problem 2.1: Mengelola Daftar (List)
#     Buat sebuah list bernama daftar_teman yang berisi 3 nama teman kamu.
#     Tambahkan satu nama lagi ke daftar tersebut menggunakan fungsi .append().
#     Print daftar lengkapnya.
#     Print nama teman yang ada di posisi indeks ke-1 (ingat, Python mulai hitung dari 0).

daftarTeman = [
    "ken","ihsan","faruf"
]


print(daftarTeman)

daftarTeman.append("kentaki")

print(daftarTeman)

print(daftarTeman[1])

# Problem 2.2: Kamus Sederhana (Dictionary)
#     Buat dictionary bernama kontak_teman.
#     Masukkan 3 teman sebagai Key dan angka (nomor telepon) sebagai Value.
#     Print nomor telepon salah satu teman dengan cara memanggil namanya (Key-nya).

friendsContact  ={
    "ken" : 813192012,
    "san" : 813193212,
    "ran" : 8123901234,
}

print(friendsContact["ken"])

#List itu enak di pakai di data yang begitu2 saja contoh nya kumpulan dari nama atau pun suatu angka
# Dictionary lebih fleksibel dan mudah di pakai serta gak ribet cocok kalau mau buat database yang kompleks