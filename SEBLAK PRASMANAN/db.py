import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "menu_seblak"
)

def insert_item(nama, tipe_menu, kategori_menu, harga_menu) :
    cursor = db.cursor()
    cursor.execute("INSERT INTO menu (nama, tipe_menu, kategori_menu, harga_menu) VALUES (%s, %s, %s, %s)", (nama, tipe_menu, kategori_menu, harga_menu))
    db.commit()
    if cursor.rowcount > 0 :
        print("Data berhasil masuk")
    else :
        print("Data gagal masuk")
        
def del_item(nama) :
    cursor = db.cursor()
    cursor.execute("DELETE FROM menu WHERE nama = %s", (nama,))
    db.commit()
    
    if cursor.rowcount > 0:
        print("Data berhasil dihapus")
    else:
        print("Data tidak ditemukan")
        
def fetch_item() :
    cursor = db.cursor()
    cursor.execute("SELECT * FROM menu")
    return cursor.fetchall()

def fetch_name(tipe_menu) :
    cursor = db.cursor()
    cursor.execute("SELECT nama FROM menu WHERE tipe_menu = %s", (tipe_menu,))
    items = cursor.fetchall()
    return items

def fetch_price(tipe_menu) :
    cursor = db.cursor()
    cursor.execute("SELECT harga_menu FROM menu WHERE tipe_menu = %s", (tipe_menu,))
    items = cursor.fetchall()
    return items

def fetch_cate(tipe_menu) :
    cursor = db.cursor()
    cursor.execute("SELECT kategori_menu FROM menu WHERE tipe_menu = %s", (tipe_menu,))
    items = cursor.fetchall()
    return items