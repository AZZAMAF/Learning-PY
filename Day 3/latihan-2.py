# Melanjutkan Minggu 3: Function Lanjutan
# Sekarang kita coba bikin fungsi yang lebih "cerdas" 
# dengan menggunakan logika if-else yang sudah kamu pelajari di minggu pertama.
# Problem 3.3: Fungsi dengan Logika
#     Buat fungsi bernama cek_status_umur(umur).
#     Fungsi ini menerima umur (angka).
#     Kalau umur >= 18, return string "Dewasa".
#     Kalau umur < 18, return string "Belum Dewasa".
#     Panggil fungsi tersebut dengan angka 15 dan 20, lalu simpan hasilnya di variabel dan print.

def statusAgecheck(age):
    if age >= 18 :
        return "Dewasa"
    else:
        return "Belum Dewasa"

audultCheck = statusAgecheck(15)
tenegarCheck = statusAgecheck(20)

print(tenegarCheck)
print(audultCheck) 

# Problem 3.4: Function dengan Parameter Default
# Kadang kita ingin fungsi punya nilai standar kalau usernya lupa memasukkan input.
#     Buat fungsi sapa_pengguna(nama="User").
#     Jika fungsi dipanggil tanpa argumen (sapa_pengguna()), dia harus cetak "Halo, User".
#     Jika fungsi dipanggil dengan nama (sapa_pengguna("Azzam")), dia harus cetak "Halo, Azzam".

def helloUser(nama="User"):
    print(f"Hallo, {nama}")


helloDefault = helloUser()
helloAzam = helloUser(nama="azzam")
