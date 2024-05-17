import mysql.connector
import random
import pandas as pd
from collections import Counter

tipe_index = {
    1 : "Kerupuk",
    2 : "Topping",
    3 : "Minuman"
}
    
kategori_index = {
    0 : "Basic",
    1 : "Regular",
    2 : "Seafood",
    3 : "Creamy and Juice",
    4 : "Coffee"
}

def common_random() :
    common_random = random.randint(min(list(kategori_index.keys())), max(list(kategori_index.keys())))
    return common_random

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "seblak_prasmanan"
)

def insert_item(common_kerupuk, common_topping, common_minuman, value_price):
    cursor = db.cursor()
    
    common_kerupuk = int(common_kerupuk)
    common_topping = int(common_topping)
    common_minuman = int(common_minuman)
    value_price = float(value_price)
    
    cursor.execute(
        "INSERT INTO pesanan (common_kerupuk, common_topping, common_minuman, value_price) VALUES (%s, %s, %s, %s)",
        (common_kerupuk, common_topping, common_minuman, value_price)
    )
    
    db.commit()

    if cursor.rowcount > 0:
        print("Data berhasil masuk")
    else:
        print("Data gagal masuk")
        
def fetch_item() :
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pesanan")
    return cursor.fetchall()

dbMain = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "menu_seblak"
)

def fetch_name(kategori_menu) :
    cursor = dbMain.cursor()
    cursor.execute("SELECT nama FROM menu WHERE kategori_menu = %s", (kategori_menu,))
    items = cursor.fetchall()
    return items

def recommend() :
    
    pesanan_list = fetch_item()
    data_pesanan = pd.DataFrame(pesanan_list)
    orderKerupuk_most = int((Counter(data_pesanan[1])).most_common(1)[0][0])
    orderTopping_most = int((Counter(data_pesanan[2])).most_common(1)[0][0])
    orderMinuman_most = int((Counter(data_pesanan[3])).most_common(1)[0][0])
    orderPrice_average = float((data_pesanan[4].sum()) / len(data_pesanan))
    
    most_all = [{'Kerupuk' : orderKerupuk_most, 'Topping' : orderTopping_most, 'Minuman' : orderMinuman_most, 'Harga' : orderPrice_average}]
    most_list = pd.DataFrame(most_all)
    
    
    rec_kerupuk = fetch_name(int(most_list['Kerupuk'][0]))
    recK_list = pd.DataFrame({'Nama' : rec_kerupuk})
    recK_list['Nama'] = recK_list['Nama'].str[0]
    
    rec_topping = fetch_name(int(most_list['Topping'][0]))
    recT_list = pd.DataFrame({'Nama' : rec_topping})
    recT_list['Nama'] = recT_list['Nama'].str[0]
    
    rec_minuman = fetch_name(int(most_list['Minuman'][0]))
    recM_list = pd.DataFrame({'Nama' : rec_minuman})
    recM_list['Nama'] = recM_list['Nama'].str[0]
    
    rec_averagePrice = most_list['Harga'][0]
    
    rec_all = pd.DataFrame({'Rekomendasi' : rec_kerupuk + rec_topping + rec_minuman})
    rec_all['Rekomendasi'] = rec_all['Rekomendasi'].str[0]

    print(rec_all)
    # print(f"{recK_list}\n{recT_list}\n{recM_list}\n")

    
if __name__ == '__main__' :
    recommend()

