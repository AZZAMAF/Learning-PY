# Soal 1: "The Safe Division" (Handling ZeroDivisionError)
# Soal:
# Buat fungsi bernama bagi_angka(angka_pertama, angka_kedua) yang membagi angka_pertama dengan angka_kedua.
#     Bungkus proses pembagian di dalam blok try dan except.
#     Jika terjadi error pembagian dengan nol (ZeroDivisionError),
#     return string: "Error: Tidak bisa membagi angka dengan nol!".
#     Jika berhasil, return hasil pembagiannya.

def devide_number(first_number, second_number):
    try:
        result = first_number / second_number
        return result
    except ZeroDivisionError:
        return 'You cannot devide by zero'
    except ValueError:
        return 'That was not a valid number'
    
print(devide_number(10,2))

# Soal 2: "The Safe Type Converter" (Handling ValueError)
# Soal:
# Buat fungsi bernama ubah_ke_angka(teks) yang mencoba mengubah input string menjadi integer (int(teks)).
#     Gunakan try-except.
#     Jika string gagal diubah menjadi angka (ValueError), return nilai 0 sebagai fallback.
#     Jika berhasil, return angka hasil konversinya.

def change_number(text):
    # aneh bet lu printah lu ambigu. gua kira teh text string misal"gojek" jadi angka kalau cuman string "123" to 123 int itu mah gampang lah koca huuu
    try:
        number = int(input("input Text: " + text))
        return number
    except ValueError:
        return 0
    
print(change_number(""))

# Soal 3: "The Dictionary Safe Getter" (Handling KeyError)
profil_user = {"nama": "Azzam", "role": "Frontend Developer"}
# Buat fungsi bernama ambil_data_aman(data, kunci):
#     Coba ambil nilai dari data[kunci].
#     Gunakan try-except untuk menangkap KeyError jika key yang dicari tidak ada di dalam dictionary.
#     Jika key tidak ditemukan, return string: "Data tidak ditemukan".

def take_secure_data(data, key):
    try:
        take_data= data[key]
        return take_data
    except KeyError:
        return "Data not found"
    
print(take_secure_data(profil_user,"role"))

# Soal 4: "The Multi-Validation Input" (Fungsi dengan Multiple Except)
# Soal:
# Buat fungsi bernama proses_data_user(teks_angka, pembagi):
#     Fungsi ini harus mengubah teks_angka menjadi integer, lalu membaginya dengan pembagi.
#     Tangkap ValueError jika string gagal jadi angka (return: "Input harus berupa angka!").
#     Tangkap ZeroDivisionError jika pembagi bernilai 0 (return: "Penyebut tidak boleh nol!").
#     Jika aman, return hasil akhirnya.

def process_user_data(text_angka, devider):
    try:
        number = int(text_angka)
        devide = number / devider
        return devide
    except ValueError:
        return "Input must be number!"
    except ZeroDivisionError:
        return "donominator"
    
print(process_user_data('txt', 10))

# Soal 5: "The Custom Error & Validation" (Raising Exception)
# Soal:
#     Buat fungsi bernama validasi_umur_pendaftaran(umur):
#         Jika umur < 17, sengaja raise sebuah ValueError dengan pesan: "Umur minimal 17 tahun untuk mendaftar!".
#         Jika umur >= 17, return string: "Pendaftaran berhasil diterima!".
#         Bungkus pemanggilan fungsi ini dengan try-except saat di-print untuk menangkap pesan error dari raise tersebut.

def age_validate(age):
    if age < 17: 
        raise ValueError("Umur minimal 17 tahun untuk mendaftar!")
    elif age >= 17:
        return "Pendaftaran berhasil diterima!"

try:
    print(age_validate(10))
except ValueError as error:
    print(f"Failed sistem {error}")
    # try and except ini untuk debugging kah atau troubelshooting gitu penggunaannya