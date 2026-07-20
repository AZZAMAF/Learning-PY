# Problem 4.3: Mini-Sistem Inventory MyPET
#     Buat list bernama inventory yang berisi 2 dictionary: [{"item": "biskuit", "stok": 5}, {"item": "daging", "stok": 2}].
#     Buat fungsi cek_stok(nama_item).
#     Fungsi tersebut harus mencari nama_item di dalam inventory.
#         Jika ketemu dan stok > 0, print "Stok tersedia".
#         Jika stok 0 atau item tidak ada, print "Stok habis atau item tidak ditemukan".

inventroy = [
    {"item":"biskuit","stok":5},
    {"item":"daging","stok":2 }
]

def stockChek(itemName):
    update_list = []
    for stock in itemName:

        stockCopy = stock.copy()
        if stockCopy["stok"] >= 0 :
            update_list.append(stock)
            print('stock availabel')
        else:
            print('Stock not found')
        
    return update_list  

result = stockChek(inventroy)
print(result)

# ketika print berjalan maka akan run reslut kemudian run function mengambil data dari inventroy
# kemudia ke for loop mengambil data dari inventroy
# kemudian saya ocpy datanya dan buat logic ambil stock kemudian pengecekan stockChek
# jika ada maka availabel jika tidak stok not found kemudian jalan kan return
# untuk mengembalikan data terbaru

inventory = [
    {"item": "biskuit", "stok": 5},
    {"item": "daging", "stok": 2}
]

def cek_stok(nama_item):
    for barang in inventory:
        # Kita cek apakah nama item di database sama dengan yang dicari
        if barang["item"] == nama_item:
            # Jika namanya ketemu, kita cek stoknya
            if barang["stok"] > 0:
                print(f"Stok {nama_item} tersedia: {barang['stok']} buah.")
                return # Selesai karena sudah ketemu
            else:
                print(f"Stok {nama_item} habis.")
                return 
    
    # Kalau loop selesai sampai habis tapi tidak ketemu
    print("Item tidak ditemukan dalam database.")

# Testing
cek_stok("daging")
cek_stok("biskuit")
cek_stok("apel") # Item yang tidak ada