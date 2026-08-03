#1: "The Tracker Variable" (Pelacak Nilai)
def cari_angka_terkecil(daftar_angka):
    angkaTerkecil = daftar_angka[0]
    
    for angka in daftar_angka:
        # angka masuk ke in yang dimana isinya kumpulan nilai
        if angka < angkaTerkecil:
            # kemudian ke condition if yang dimaa jika agka lebih kecil dari angka terkecil
            # = true ex:45 < 0 = false, 45 < 12 = salah, 12 < 89= true, 12 < 33 = true, 12 < 67 = true, 12 < 9 = false, 9 < 9 = true
            # so the last output is 9 
            terkecil = angka 
            #  gua gak ngerti kenapa harus di kasih variabel dulu terus di return nya di loop nya
            #  yap ini juga code gua tiru dari algoritmanya ai tinggal gua ganti aja condisinya
            # mungkin biar lebih rapih aja ya dan gak ngebingungin
    
    return terkecil
    
kumpulan_nilai = [45, 12, 89, 33, 67, 9]
hasil = cari_angka_terkecil(kumpulan_nilai)
print('ini adalah angka terkecil', hasil)
# Ini pertanyaan emas. Jawabannya sederhana: Bayangkan lu lagi nyari barang di dalam tumpukan kardus.
# Kalau lu ngecek kardus pertama, terus lu langsung nyerah atau langsung ngomong (return),
# lu bakal salah karena belum ngecek kardus-kardus di belakangnya.
#Makanya, proses ngecek (for loop) harus selesai dulu sampai kardus terakhir. 
# Pas udah ketemu siapa pemenangnya (angka paling kecil di antara semuanya), 
# baru deh di luar loop kita bilang: "Nih, hasil akhirnya!" (return).

#2: "The Counter Tracker" (Pencatat Jumlah Kemunculan)
def hitung_angka_lima(daftar_angka):
    jumlahlima = 0
    for angka in daftar_angka:
        if angka == 5:
            jumlahlima += 1

    return jumlahlima
# jujur gua semepet bingung terus gua tanya ai langsung di kasih jawabnya tapi bukan untukangka 5 ya
# ini sih tingal gua ganti kondisinya gitu 
# intinya kalau ada angka 5 yang sama, jumlahlima akan bertambah 1 (+= 1)


listangka=[5, 2, 5, 8, 5, 1, 9, 5]
hasil = hitung_angka_lima(listangka)
print('this is ouput: ada', hasil,'angka 5')
#3: "The Collector" (Pengumpul Data ke List Baru)
# menyaring angka-angka yang lebih besar dari 10 saja,

def ambil_angka_besar(daftar_angka):
    numberbiggerthenTen = []
    for number in daftar_angka:
        if number > 10:
            numberbiggerthenTen.append(number)
        # remember append akan memasukan nilai kedalam  var numberbiggerthenTen dari var number
        # jika number lebih besar dari 10 maka number masukan ke numberbiggerthenTen gitu coy melalui append
    return numberbiggerthenTen

listAngka= [3, 8, 12, 5, 20, 7, 15]
result = ambil_angka_besar(listAngka)
print('this number bigger ten :',result)

#4: "The String Splitter" (Pecah dan Balik Kalimat)
# # Soal:
# Diberikan sebuah kalimat: "belajar javascript dan python itu seru".
# Buat fungsi bernama balik_urutan_kata(kalimat) yang:
#     Memecah kalimat tersebut menjadi list kata.
#     Membalik urutan kata-katanya (bukan hurufnya, 
# tapi urutan katanya jadi paling belakang ke paling depan).
#     Hint: Hasil akhirnya nanti harus berupa string lagi yang digabung pakai " ".join(...),
# atau biarkan jadi list dulu biar gampang dilihat.

def balik_uruta_kata(kalimat):
    daftarkata = kalimat.split()
    # split() = for membabagi kalimat atau memecah kalimat// ['seru', 'itu', 'python', 'dan', 'javascript', 'belajar']
    dibalik = daftarkata[::-1]
    # [::--1] for membalik kalimatnya // seru itu python dan javascript belajar
    print(dibalik)
    newKalimat =" ".join(dibalik)
    # " ".join(dibalik) for mengembalikan menjadi string biasa dari list itu // seru itu python dan javascript belajar
    print(newKalimat)
    return newKalimat
    
    
balik_uruta_kata("belajar javascript dan python itu seru")
print(balik_uruta_kata("hallo"))

#5: "The Vowel Hunter" (Penyaring Huruf Vokal)
# Soal:
# Diberikan sebuah kata: "pemrograman".
# Buat fungsi bernama cari_huruf_vokal(kata) yang:
#     Menyaring huruf-huruf vokal (a, i, u, e, o) dari kata tersebut.
#     Memasukkan huruf-huruf vokal yang ketemu itu ke dalam list baru menggunakan .append().
#     Mengembalikan (return) list yang isinya kumpulan huruf vokal tersebut.
def cari_huruf_vokal(kata):
    hurufVokal= []
    
    for huruf in kata.lower():
        if huruf in "aAiueo":
        # print(kata)
            hurufVokal.append(huruf)
        # gua tuh salah nya di appen(ini cok) harusnya gua isi huruf malah gua isi kata wkwkwk
        
    return hurufVokal

word = "Pemrograman"
print(cari_huruf_vokal(word))


