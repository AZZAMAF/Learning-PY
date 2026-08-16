# Soal 1: "The Private Attribute & Getter" (Enkapsulasi Dasar)
class BankAccount:
    
    def __init__(self, user, saldo_awal=0):
        self.user = user
        self.__saldo = saldo_awal
        
    def get_saldo(self):
        return self.__saldo, self.user
    # setoran duit
    def get_deposit(self, deposit):
        if deposit <= 0 :
            return f'deposit failed'
        elif deposit:
            self.__saldo += deposit
            return self.__saldo
        
    # oh i relize the self itu variabel ya yagn bisa kita panggil ya oh gitu 
myWallet = BankAccount('azam', 1000)
# Soal 2: "The Controlled Setter" (Enkapsulasi Validasi Nilai)
# my mistake is just call the wallet without bankaccount
# jadi gua buat giini deposit = BankAccount(1000) // ini pasti depostinya bakal error
# karena saldonya nol gitu. kok bisa saldo nya nol, karena kita pangglil di deposit itu saldow awal
# bukan depositnya. dan deposit will run deposit failed karena masi nol jir
# yang bener lewat code di bwah ini. we take the mywallet and call the getdposit(30000)
myWallet.get_deposit(30000)
print(myWallet.get_saldo())

# Soal 3: "The Polymorphism Shape" (Banyak Bentuk / Method Overriding)
# Soal:
    # Buat Parent Class bernama Karyawan yang punya method hitung_gaji(self). Di kelas induk, method ini cukup mereturn 0.
    # Buat Child Class pertama bernama KaryawanTetap yang mewarisi Karyawan, dengan constructor menerima gaji_bulanan. Override method hitung_gaji(self) untuk mereturn nilai gaji_bulanan.
    # Buat Child Class kedua bernama KaryawanFreelance yang mewarisi Karyawan, dengan constructor menerima tarif_per_jam dan jam_kerja. Override method hitung_gaji(self) untuk mereturn hasil tarif_per_jam * jam_kerja.
    # Buat objek dari kedua jenis karyawan tersebut dan panggil method hitung_gaji() masing-masing.
class Employee:
    
    def __init__(self, name, id, ):
        self.name = name
        self.id = id
    
    def salary(self):
        return 0


class PermanentEmployees(Employee):
    
    def salary(self, monthly_salary):
        return monthly_salary
    
class freelance(Employee):
    
    def salary(self, per_hour, work_hour):
         return per_hour * work_hour
# soal no 3 ini jelek banget buat gua pusing dan pegaplikasiannya tidak standar industri
# aneh banget harus nya kamu buat soal yang lebih detail  dan komplex menggunakan standar logika penghitungan salry by id and name empployer gitu loh

default_employee = Employee('ahmad',12345678)
print(default_employee.salary())

pe = PermanentEmployees('rokan',123456)
print(pe.salary(100))

fe = freelance('guntur', 1090828)
print(fe.salary(1000,12))    
        
    
class Book:
    
    def __init__(self, author, title):
        self.author = author
        self.title = title
    
    def __str__(self):
        return f'The Book Title : {self.title} | Author Name : {self.author}'

book1 = Book('ken',"ara2 ikeh kudsai")
print(book1)

# Soal 5: "The Mini E-Commerce OOP System" (Final Boss OOP)

class Product:
    
    def __init__(self, name, price=0):
        self.name = name
        self.__price = price
    def get_infor(self):
        return f"name: {self.name} | price : {self.__price}"
    # Buat fungsi getter agar class anak bisa mengambil nilai privat __price
    def get_price(self):
        return self.__price

class ProductElectronic(Product):
    
    def __init__(self, name, price, gurante):
        super().__init__(name, price)
        self.gurante = gurante
    # super(), untuk memepermudah dan mempersingkat penulisan code biar gak satu
    # tapi aing disini gak ngertinya emg harus di tulis ulang ya code2 gua aja gak
    # apa biar leetcode or clean code gitu
    def get_infor(self, info_tambahan):
        # self.gurante = gurante
        # Panggil self.get_price() bukan self.__price
        return f"name: {self.name} | price : {self.get_price()} | gurante : {self.gurante}{info_tambahan}"
    
    
leptop = ProductElectronic('asuss',12000000,2)
print(leptop.get_infor(' thn garansinya'))    

class ProductCloth(Product):
    # default  method// defult  constractor jadi apapun yang kita masukan kedalam __init__ ini hanya default  value aja
    def __init__(self, name, price=0,size=''):
        super().__init__(name, price)
        self.size = size
        
    def get_infor(self, ):
        return f"{super().get_infor()} | size : {self.size}"
            

# super().get_infor()    how  to   return  with size ya // super().get_infor() 
# anjay bisa
clothe_adiras  =  ProductCloth('adiras',100000,size='L')
print(clothe_adiras.get_infor())