# soal 1: "The Basic Class & Constructor" (Membuat Class & __init__)

class Mobil:
    #Constraktor for atribute inisilation
    def __init__(self, brand, color, year):
        self.brand = brand # Atribut brand
        self.color = color # Atribut color
        self.year = year
    # Question: kenapa harus __init__(self). fungsi self untuk apa, kenapa di buat nya gitu,  how in js
    #how can that work
    # Soal 2: "The Object Method" (Perilaku Objek)
    # fungsi or method tambahan
    def info(self):
        return f"Mobil {self.brand} bewarna {self.color} keluaran tahun {self.year}"
    
# membuat object (instansiasi)// maksudnya apa instansiasi itu// iniliasasi juga apa jir
mycar = Mobil("lamborgini","red",1999)
print(mycar.info())

# Soal 3: "The Bank Account Simulator" (State & Action / Atribut Berubah)

class RekeningBank:
    
    def __init__(self,name,saldo=0):
        self.name = name
        self.saldo = saldo
    def saving(self, jumlah):
        self.saldo += jumlah
    def cek_saldo(self):
        return f"Saldo{self.name} saat ini : {self.saldo}"
    
user1 = RekeningBank("rido",1000000000)
user1.saving(3500)
print(user1.cek_saldo())


# parent class
class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def voice(self):
        return f"hewan bersuara"
    
    
class Kucing(Animal):
    def mengeong(self):
        return f"{self.name} berakata: meong!"
        
myPet = Kucing("milo")    
print(myPet.mengeong())

# Soal 5: "The User Profile System" (Mini Project OOP)

class UserProfile:
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True
        
    def deactive_account(self):
        self.is_active = False
    def get_status(self):
        if self.is_active == True:
            return f"Akun {self.username} Sedang Active"
        else:
            return f"Akun {self.username} Tidak Sedang Active"

user_odo = UserProfile('ridosan','ggwp@gmail.com')
user_odo.deactive_account()
print(user_odo.get_status())