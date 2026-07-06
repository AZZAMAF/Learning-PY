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