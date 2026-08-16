# 5 Soal Day 16: "The API & Module Navigator" (Menghubungkan Program ke Dunia Luar)
# Soal 1: "The Built-in Module Import" (Memanfaatkan Modul Bawaan)

#     Materi: Menggunakan modul bawaan Python (math atau random).

#     Soal:
#     Buat fungsi bernama pilih_pemenang(daftar_nama):
#         Lakukan import random.
#         Gunakan fungsi dari modul random (misal random.choice()) untuk memilih satu nama secara acak dari sebuah list nama-nama yang dikirimkan.
#         Return nama pemenang yang terpilih.

import random 

name = ["azzam","furqon","zen",'ale']
def chose_winner(list_name):
    the_winner =random.choice(list_name)
    return f'the  winner  is {the_winner}'

print(chose_winner(name))
    

# Soal 2: "The Custom Module Concept" (Memecah File / Modular Programming)

#     Materi: Memahami konsep import antar file Python buatan sendiri.

#     Soal:
#     Bayangkan lu punya dua file terpisah di folder yang sama:
#         File pertama bernama math_utils.py yang berisi fungsi penjumlahan:
#         Python
#         def tambah(a, b):
#             return a + b
#         Di file utama lu (main.py), bagaimana cara lu mengimpor fungsi tambah tersebut dari math_utils lalu menggunakannya untuk menjumlahkan 5 + 10? Tuliskan baris kode import dan pemanggilannya.



# Soal 3: "The HTTP Request Simulation" (Dasar Request API)

#     Materi: Memahami konsep dasar pemanggilan API menggunakan modul populer requests (simulasi pengambilan data web).

#     Soal:
#     (Asumsikan library requests sudah ter-install)
#     Buat fungsi bernama ambil_data_api(url):

#         Lakukan import requests.
#         Lakukan requests.get(url) untuk mengambil data.
#         Ambil hasil datanya dalam format JSON dengan method .json().
#         Bungkus dengan try-except (atau tangkap status response) untuk jaga-jaga kalau URL-nya mati atau error. Return data JSON-nya jika berhasil.

import requests

respon = requests.get('https://jsonplaceholder.typicode.com.')

print(respon.status_code)  # Menghasilkan angka 200 jika berhasil



# Soal 4: "The JSON API Data Filter" (Mengolah Data Hasil API)

#     Materi: Menyaring data spesifik dari dictionary hasil response API.

#     Soal:
#     Misalkan lu dapet data dari API cuaca palsu berbentuk dictionary kayak gini:
#     Python

#     data_cuaca = {
#         "kota": "Jakarta",
#         "suhu": 32,
#         "kondisi": "Cerah Berawan",
#         "kelembapan": 75
#     }

#     Buat fungsi bernama format_info_cuaca(data):

#         Ambil nilai "kota" dan "suhu" dari dictionary tersebut.

#         Return string dengan format: "Cuaca di [kota] saat ini [suhu] derajat Celsius."

# Soal 5: "The Error Handling API Call" (API yang Tahan Banting)

#     Materi: Menggabungkan Error Handling (try-except) dengan pemanggilan API eksternal.

#     Soal:
#     Buat fungsi bernama cek_koneksi_aman(url_api):

#         Coba lakukan request ke URL menggunakan requests.get(url_api, timeout=3).

#         Jika berhasil terkoneksi, return string: "Koneksi ke server berhasil!".

#         Jika terjadi error koneksi atau timeout (gunakan except Exception as e:), return string: "Gagal terhubung ke server: [pesan_error]".