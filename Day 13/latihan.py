# Soal 1: "The Writer Assistant" (Menulis File Teks)
# Soal:
# Buat fungsi bernama simpan_catatan(nama_file, teks_catatan) yang bertugas:
#     Membuka file (gunakan with open(...) as file:) dengan mode tulis ("w").
#     Menuliskan teks_catatan ke dalam file tersebut pakai .write().
#     Pastikan tidak ada error dan file berhasil terbuat secara otomatis.
def save_noted(file_name, note):
    with open(file_name, "w") as file:
         file.write(note)
         return note

print(save_noted("test.txt", "aku adalah supermen"))

# Soal 2: "The Reader Agent" (Membaca File Teks)
# Soal:
# Buat fungsi bernama baca_catatan(nama_file) yang bertugas:
#     Membuka file teks yang ada menggunakan mode baca ("r").
#     Membaca seluruh isi teks di dalamnya pakai .read().
#     Return string isi catatan tersebut.
#     (Bonus pengaman): Bungkus dengan try-except (menangkap FileNotFoundError) 
# supaya kalau file-nya belum ada, 
# program gak crash tapi mengembalikan string: "File tidak ditemukan!".

def read_note(file_name):
    try:
        with open(file_name, "r") as file:
                    
            content = file.read()
            return content
    except FileNotFoundError:
        return'file note found'
        
print(read_note("test.txt"))

# Soal 3: "The Append Logger" (Menambah Log Tanpa Menimpa)
# Soal:
# Beda dari mode "w" yang bakal ngehapus isi lama, mode "a" dipakai buat nambahin teks di baris paling bawah.
# Buat fungsi bernama tambah_log_aktivitas(nama_file, aktivitas_baru):
#     Membuka file dengan mode "a".
#     Menuliskan aktivitas_baru ke dalam file, tambahkan karakter baris 
# baru "\n" di ujungnya supaya rapi ke bawah tiap kali ditambah data baru.
#     Berhasil menyimpan tanpa merusak data sebelumnya.

def add_activity_log(file_name, new_activity):
    with open(file_name, "a") as file:
        file.write(f"\n{new_activity}")
        print('success add log')

add_activity_log('test.txt','kamu pasti bisa')

# Soal 4: "The JSON Saver" (Menyimpan Struktur Data Kompleks)
import json
data_user = {"nama": "Azzam", "keahlian": ["React", "Python", "UI/UX"], "aktif": True}
# Buat fungsi bernama simpan_ke_json(nama_file, data):
    # Lakukan import json.
    # Gunakan json.dump(data, file) di dalam blok 
# with open(nama_file, "w") as file: untuk menyimpan struktur 
# dictionary tersebut ke file .json.

def save_to_json(file_name, data):
    with open(file_name, "w") as file_json:
        json.dump(data, file_json, indent=4)
        print('data json succes')
        
save_to_json('test.json', data_user)

# Soal 5: "The JSON Loader" (Membaca Kembali Data JSON)
# Soal:
# Buat fungsi bernama muat_dari_json(nama_file):
#     Lakukan import json.
#     Buka file .json dengan mode baca ("r").
#     Gunakan json.load(file) untuk membaca data JSON tersebut 
# kembali ke dalam bentuk dictionary Python.
#     Return data yang sudah dimuat. 
# (Bungkus try-except untuk jaga-jaga kalau filenya belum ada).

def load_from_json(file_name):
    try :
        with open(file_name, 'r')as file:
            read_json = json.load(file)
            return read_json
    except FileNotFoundError:
        return 'error'
    
print(load_from_json('test.json'))