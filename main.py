
#No 1
mahasiswa = {"nim": 20121090, "nama": "Qois Sahroni", "kelas":"TI 3B", "alamat": "Ngadirejo,Reban,Batang"}
print(type(mahasiswa))
print(mahasiswa)
print()

# No 2
print()
print("-------------------------------------------------------------")
print("       Aplikasi sederhana menggunakan String dan Array       ")
print("-------------------------------------------------------------")
print("NIM        : ",mahasiswa["nim"])
print("Nama       : ",mahasiswa["nama"])
print("Kelas      : ",mahasiswa["kelas"])
print("Alamat     : ",mahasiswa["alamat"])
print("-------------------------------------------------------------")



#No 3
urutkankata = ("UNISS", "di", "belajar", "pada", "Mahasiswa", "data", "ruang", "lab", "struktur", "semester", "tema", "Array", "String", "dan", "di", "dengan", "Batang", 3)

print("{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(urutkankata[4],urutkankata[1],urutkankata[0],urutkankata[16],
 urutkankata[3],urutkankata[9],urutkankata[17],urutkankata[2], urutkankata[8], urutkankata[5], urutkankata[15], urutkankata[10], urutkankata[12], urutkankata[13],urutkankata[11], urutkankata[14], urutkankata[6], urutkankata[7]))
print()



#No 4
from array import*
def squared(number):
    return number * number

nilai = array("i", [1, 3, 4, 5, 10, 15, 20])
print ()
print("------------------------------------------------------")
print("         Aplikasi Sederhana menggunakan Array         ")
print("------------------------------------------------------")

formula1 = nilai[4] + nilai[1] * nilai[5]
formula2 = nilai[1] * nilai[2] / 2
formula3 = squared(nilai[5]) * nilai[1] + nilai[3]
formula4 = nilai[5] - nilai[3] * nilai[2]

print("a.",nilai[4],"+",nilai[1],"x",nilai[5],"=",formula1)
print("b.",nilai[1],"x",nilai[2],":","2","=",formula2)
print("c.",nilai[5],"²","x", nilai[1],"+",nilai[3],"=", formula3)
print("d.",nilai[5],"-", nilai[3],"x", nilai[2],"=",formula4)