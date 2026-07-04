# Problem 1.7: The Simple Login
# Buat program sederhana untuk "login":
#     Buat variabel username_asli = "azzam" dan password_asli = "1234".
#     Minta user untuk input username dan password.
#     Gunakan if untuk mengecek:
#         Jika username sama dengan username_asli DAN password sama dengan password_asli, maka cetak "Login Berhasil!".
#         Jika salah satu (atau keduanya) salah, cetak "Username atau password salah."
#         Petunjuk: Gunakan operator and untuk mengecek dua kondisi sekaligus.

username_asli = "azzam"
password_asli = 1234

input_user = input("username : ")
input_pwd = int(input("password : "))
if input_user == username_asli and input_pwd == password_asli:
    print("Login Succes")
else:
    print("Failed Login")
# and ini harus bener 22 nya kalau or salah satunya  gitu coy not harus salah 22nya

# gua mau buat yang lebih seru
DB_name = ["azzam","rafi","ken"]
DB_pwd = [1222, 1223, 1444]

user1 = DB_name[0]
user2= DB_name[1]
user3= DB_name[2]

user1Pwd = DB_pwd[0]
user2Pwd = DB_pwd[1]
user3Pwd = DB_pwd[2] 


usernameDB = DB_name[0],DB_name[1], DB_name[2]

username = DB_name
allUser = user1, user2, user3


userInputname = input("userName : ") # nama yang  kit input ex : azzam
name = userInputname

userInputpwd = int(input("password : "))
pwd = userInputpwd



if name == user1 or user2 and pwd == user1Pwd :
    print("Loggin Succes")
else:
    print("failed")

# perbedaan antara input biasa dan int(input()) adalah ya untuk khusus angka kalau huruf bakal fungsinya ya untuk pwd biasanya