import db
import main
from features import menu

def add() :
    nama = input('Nama Barang : ')
    tipe_menu = input('Tipe Menu : ')
    kategori_menu = input('Kategori Menu : ')
    harga_menu = input('Harga : ')
    
    db.insert_item(nama, tipe_menu, kategori_menu, harga_menu)
    
def dele() :
    name = input('Nama barang yang mau di delete : ')
    db.del_item(name)
    
def check() :
    items = db.fetch_item()
    for item in items :
        index = item[0]
        nama = item[1]
        tipe_menu = item[2]
        kategori_menu = item[3]
        harga_menu = item[4]
        print(f"\n\nNama Barang : {nama} \ndengan id : {index}\ndengan tipe : {tipe_menu}\ndengan kategori : {kategori_menu}\ndengan harga : {harga_menu}")

def start() :
    password = "admin123"
    password_in = input("Masukkan Password : ")
    if password_in == password :
        while True :  
            menu = int(input('\npilihan : \n\n1. Tambah Barang\n2. Hapus Barang\n3. Check Barang\n4. Kembali\n\nSilahkan Pilih : '))
            if menu == 1 :
                add()
            elif menu == 2 :
                dele()
            elif menu == 3 :
                check()
            elif menu == 4 :
                main.menu()
            else :
                break
    
if __name__ == '__main__' :
    start()