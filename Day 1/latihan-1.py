# Problem 1.3: Input Sederhana
# Buat program yang:
#     Meminta pengguna memasukkan nama mereka (gunakan input()).
#     Meminta pengguna memasukkan tahun lahir mereka.
#     Hitung umur mereka di tahun 2026 (kurangi 2026 dengan tahun lahir).
#     Print: "Halo [nama], umur kamu sekarang sekitar [umur] tahun."

# nama// birth year // 2026 - By = umur sekarang 

name = input("Name :")
birthYear = int(input("Birth year : "))
age = 2026 - birthYear 

print(f"Hallo {name}, umur kamu sekarang sekitar {age}")

# roblem 1.4: String Slicing (Mengambil potongan)
# Diberikan string text = "Programming".
#     Print hanya kata "Gram" dari string tersebut (Gunakan teknik slicing [start:stop]).
#     Clue: Kalau mau ambil dari indeks 3 sampai 6, kamu tulis text[3:7]. Coba otak-atik angkanya sampai dapat "Gram".
text = "programming"
print(text[3:7])