# Problem 4.1: The "Code-to-Feed" Logic (Persiapan untuk proyek MyPET kamu!)
# Bayangkan proyek MyPET kamu. Kita perlu logika sederhana untuk memberi makan pet.
#     Buat variabel global level_lapar = 50 (rentang 0-100, 100 artinya sangat lapar).
#     Buat fungsi beri_makan(makanan).
#         Jika makanan adalah "biskuit", level_lapar berkurang 10.
#         Jika makanan adalah "daging", level_lapar berkurang 30.
#         Jika makanan lain, print "Makanan tidak dikenal".
#     Fungsi harus print sisa level_lapar setelah diberi makan.
#     Hint: Gunakan global level_lapar di dalam fungsi agar kamu bisa mengubah variabel luar tersebut.

HungryLevel = 50 
foods=[
    "biskuit", "meat", "apple"
]

def feedPet(food):
    if food == foods[0]:
        return f" this is the HungryLevel :{HungryLevel - 10}"
    elif food == foods[1]:
        return f" this is the HungryLevel :{HungryLevel - 30}"
    else:
        print("food not found")

print(feedPet("biskuit"))
print(feedPet("meat"))


# Problem 4.2: List Processing
#     Buat list angka: [10, 25, 40, 55, 70].
#     Buat fungsi filter_lulus(daftar_angka) yang mengembalikan List baru berisi angka yang >= 40.
#     Hint: Gunakan for loop untuk mengecek setiap angka di dalam list.

listNumber = [
    10,25,40,55,70
]

output = []
# for x in listNumber:
#     print(x)

def passedFilter(listNumber):
    for x in listNumber:
        # print(x)
        if x >= 40:
            output.append(x)
            print(output)
                

print(passedFilter(listNumber))
    
        