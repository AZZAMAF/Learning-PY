# Problem 4.4: Temukan Kesalahannya
# Coba perhatikan kode ini, di mana kesalahannya? (Jangan dijalankan dulu, coba analisa lewat mata).
def hitung_diskon(harga):
    if harga > 100000:
        diskon = harga * 0.1
    print("Diskon kamu adalah: " + diskon)

# ya karena gak ada else nya sedangkan parameter if itu 10rb jir
# Apa yang terjadi jika saya memanggil hitung_diskon(50000)? Mengapa program ini akan crash?
# Setelah kamu tahu jawabannya, kita akan masuk ke tahap akhir program ini: Synthesis (Portfolio Piece). Kamu sudah sangat siap!
# Berikut cara memperbaiki kodenya agar tidak crash:
def hitung_diskon(harga):
    diskon = 0  # Inisialisasi awal (Penting!) // gak paham kenapa harus di kasih ini
    if harga > 100000:
        diskon = harga * 0.1
    
    # Gunakan f-string agar tidak perlu konversi tipe data manual
    print(f"Diskon kamu adalah: {diskon}")