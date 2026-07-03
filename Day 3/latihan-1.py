#Function
# Problem 3.1: Function Sederhana
    # Buat fungsi bernama sapa_teman(nama) yang mencetak "Halo [nama], apa kabar?".
    # Panggil fungsi tersebut dengan 3 nama teman yang berbeda.

def Hello(nama):
    print(f'hello ${nama}, apa kabar?')

Hello("azzam")
Hello("ken")
Hello("san")    


# Problem 3.2: Function dengan Return
# Fungsi tidak selalu harus print. Fungsi bisa mengembalikan (return) sebuah hasil supaya bisa disimpan ke dalam variabel.
#     Buat fungsi hitung_tambah(a, b) yang mengembalikan hasil a + b.
#     Simpan hasil dari fungsi tersebut ke dalam variabel hasil_akhir.
#     Print hasil_akhir


def Tambah(a,b):
    return a + b

finalScore = Tambah(10,12)

print(finalScore)