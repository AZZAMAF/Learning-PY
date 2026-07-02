# Problem 1.5: Grade Calculator
# Buat program yang:
#     Meminta input angka (nilai ujian) dari user.
#     Ubah input tersebut jadi int.
#     Gunakan if, elif, dan else untuk mencetak:
#         Nilai >= 90: Cetak "Grade A"
#         Nilai >= 80: Cetak "Grade B"
#         Nilai >= 70: Cetak "Grade C"
#         Di bawah 70: Cetak "Grade F (Belajar lagi ya!)"

str_input = input("Your Grade : ")
grade = int(str_input)

if grade == 100:
    print("perfet")
elif grade >= 90:
    print("Grade A")
elif grade >= 80:
    print("Grade B")
elif grade >= 70:
    print("Grade C")
else:     
    print("Grade F Belajar lagi ya")
# pertama aku tulis input ini tipenya str and i change to int in grade var
#kemudian ya tinggal saya buat tuh algoritmatnya saya tambahkan else diakhir
# karena else itu mengeksekusi apa yang tidak di eksekusi oleh if dan elif

# Problem 1.6: Ganjil-Genap
#     Minta user memasukkan satu angka.
#     Gunakan operator modulus (%) untuk mengecek apakah angka tersebut ganjil atau genap.
#     (Petunjuk: angka % 2 == 0 artinya angka tersebut genap karena sisa baginya adalah 0).
#     Print: "Ini angka Genap" atau "Ini angka Ganjil".
Number = int(input("Put Number Here :"))

if Number % 2:
    print("this Number is ganjil")
elif Number % 3:
    print("this is genap")
# pertama saya atur input as int 
# if number gepan maka hasilnya 0
# else number ganjil maka hasilnya 3


