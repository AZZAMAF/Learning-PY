# Tugas Akhir: Sistem Manajemen Pet

# Buatlah program sederhana dengan aturan berikut:
#     Data Pet: Buat satu list yang berisi 3 dictionary. Setiap dictionary punya: nama, level_lapar (angka 0-100), dan status ("hidup").
#         Contoh: pets = [{"nama": "Kiko", "level_lapar": 50, "status": "hidup"}, ...]
#     Fungsi beri_makan(nama_pet): * Fungsi ini harus mencari pet berdasarkan namanya di dalam list tadi.
#         Jika ketemu, kurangi level_lapar-nya (misal: kurangi 20).
#         Jika level_lapar mencapai 0 atau kurang, ubah status menjadi "kenyang".
#     Fungsi cek_semua_pet():
#         Fungsi ini melakukan for loop untuk menampilkan nama, lapar, dan status setiap pet yang ada di list.

Pet = [
    {"name": "Rabit", "HungryLevel":100, "status":"life" },
    {"name": "Cat", "HungryLevel":0, "status":"Dead" },
    {"name": "Bird", "HungryLevel":50, "status":"life" }
]

def feedPet(namePet):

    for thePet in Pet:
        if thePet["name"] == namePet:
            thePet["HungryLevel"] -= 20
            print(f"{thePet['name']} : HungryLevel Berkurang 20 menjadi {thePet['HungryLevel']}")
            return
        elif thePet["HungryLevel"] <= 0 and thePet["status"] == "life" :
            print("HungryLevel : Full")
            return

        

# Testing            
feedPet("Rabit")
feedPet("Cat")
feedPet("Bird")

print('\n')
def callAllpet(allPet):
    for p in allPet:
        print(f" Hallo this is {p['name']} lapar: {p['HungryLevel']} Status Hidup:{p['status']}")  
        
        
callAllpet(Pet)
print('test11111112222')