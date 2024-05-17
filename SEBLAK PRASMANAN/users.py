import db
import pandas as pd
import main
from collections import Counter
from features import menu

def menu_data() :
    pass

def order_data() :

    kerupuk_value = 1    
    item_name = db.fetch_name(kerupuk_value)
    item_price = db.fetch_price(kerupuk_value)
    item_cate = db.fetch_cate(kerupuk_value)
    kerupuk_list = []
    kerupuk_list_cate = []
    for name_item, price_item in zip(item_name, item_price):
        name_list = name_item[0]
        price_list = price_item[0]
        kerupuk_list.append({'Nama': name_list, 'Harga': price_list})
        
    for name_item, price_item, cate_item in zip(item_name, item_price, item_cate):
        name_list = name_item[0]
        price_list = price_item[0]
        cate_list = cate_item[0]
        kerupuk_list_cate.append({'Nama': name_list, 'Harga': price_list, 'Tipe' : cate_list, 'Kategori' : kerupuk_value})
        
    df = pd.DataFrame(kerupuk_list)
    df.index = [f"{i + 1}" for i in range(len(df))]
    print(f"\nKERUPUK : \n{df}\n")
        
    df = pd.DataFrame(kerupuk_list_cate)
    df.index = [f"{i + 1}" for i in range(len(df))]
    # print(f"\nKERUPUK : \n{df}\n")
    
    topping_value = 2
    item_name = db.fetch_name(topping_value)
    item_price = db.fetch_price(topping_value)
    item_cate = db.fetch_cate(topping_value)
    topping_list = []
    topping_list_cate = []
    for name_item, price_item in zip(item_name, item_price):
        name_list = name_item[0]
        price_list = price_item[0]
        topping_list.append({'Nama': name_list, 'Harga': price_list})
        
    for name_item, price_item, cate_item in zip(item_name, item_price, item_cate):
        name_list = name_item[0]
        price_list = price_item[0]
        cate_list = cate_item[0]
        topping_list_cate.append({'Nama': name_list, 'Harga': price_list, 'Tipe' : cate_list, 'Kategori' : topping_value})
        
    df = pd.DataFrame(topping_list)
    df.index = [f"{i + 1}" for i in range(len(df))]
    print(f"\nTOPPING : \n{df}\n")
    
    df = pd.DataFrame(topping_list_cate)
    df.index = [f"{i + 1}" for i in range(len(df))]
    # print(f"\nTOPPING : \n{df}\n")
    
    minuman_value = 3
    item_name = db.fetch_name(minuman_value)
    item_price = db.fetch_price(minuman_value)
    item_cate = db.fetch_cate(minuman_value)
    minuman_list = []
    minuman_list_cate = []
    for name_item, price_item in zip(item_name, item_price):
        name_list = name_item[0]
        price_list = price_item[0]
        minuman_list.append({'Nama': name_list, 'Harga': price_list})
        
    for name_item, price_item, cate_item in zip(item_name, item_price, item_cate):
        name_list = name_item[0]
        price_list = price_item[0]
        cate_list = cate_item[0]
        minuman_list_cate.append({'Nama': name_list, 'Harga': price_list, 'Tipe' : cate_list, 'Kategori' : minuman_value})
        
    df = pd.DataFrame(minuman_list)
    df.index = [f"{i + 1}" for i in range(len(df))]
    print(f"\nMINUMAN : \n{df}\n")
    
    df = pd.DataFrame(minuman_list_cate)
    df.index = [f"{i + 1}" for i in range(len(df))]
    # print(f"\nMINUMAN : \n{df}\n")

    kerupuk_item = []
    kerupuk_item_cate = []
    topping_item = []
    topping_item_cate = []
    minuman_item = []
    minuman_item_cate = []
    all_item = []
    all_item_cate = []
    
    
    debug_price = [
        {'Nama' : '-', 'Harga' : 0}
    ]
    
    debug_price_cate = [
        {'Nama' : '-', 'Harga' : 0, 'Tipe' : 0, 'Kategori' : 0}
    ]
    
    for item in debug_price :
        all_item.append(item)
        
    for item in debug_price_cate :
        all_item_cate.append(item)
    
    while True :
        
        order_list = pd.DataFrame(all_item)
        price_total = order_list['Harga'].sum()
        order_row = pd.DataFrame({'Nama': ['Total Harga'], 'Harga' : [price_total]})
        order_list = pd.concat([order_list ,order_row], ignore_index = True)

        print(f"\nMenu yang dipesan : \n{order_list}\n")
        
        order_list_cate = pd.DataFrame(all_item_cate)

        # print(f"\nMenu yang dipesan : \n{order_list_cate}\n")
        
        change_tipe = input("\nPilihan\n1. Kerupuk(k)\n2. Topping(t)\n3. Minuman(m)\n4. Hapus pesanan(d)\n5. Konfirmasi(v)\n6. Kembali(b)\nPilih kode dalam kurung : ")
        
        
        if change_tipe.lower() == "k" :
            input_pesanan = input("\nPilih kerupuk berdasarkan angka (jika lebih dari 1 pisahkan dengan koma): ")
            pesan_nums = [int(pesan_num.strip()) for pesan_num in input_pesanan.split(',') if pesan_num.strip()]

            for pilih in pesan_nums:
                if pilih <= len(kerupuk_list):
                    item = kerupuk_list[pilih - 1]
                    kerupuk_item.append(item)
                    all_item.append(item)
                    
            for pilih in pesan_nums:
                if pilih <= len(kerupuk_list_cate):
                    item = kerupuk_list_cate[pilih - 1]
                    kerupuk_item_cate.append(item)
                    all_item_cate.append(item)

            # print("\nAnda Memesan :")
            # for item in kerupuk_item :
            #     print(item)
                
            # print("\nTipe pesanan :")
            # for item in kerupuk_item_cate :
            #     print(item)
                
                
        elif change_tipe.lower() == "t" :
            input_pesanan = input("\nPilih topping berdasarkan angka (jika lebih dari 1 pisahkan dengan koma): ")
            pesan_nums = [int(pesan_num.strip()) for pesan_num in input_pesanan.split(',') if pesan_num.strip()]

            for pilih in pesan_nums:
                if pilih <= len(topping_list):
                    item = topping_list[pilih - 1]
                    topping_item.append(item)
                    all_item.append(item)
                    
            for pilih in pesan_nums:
                if pilih <= len(topping_list_cate):
                    item = topping_list_cate[pilih - 1]
                    topping_item_cate.append(item)
                    all_item_cate.append(item)

            # print("\nAnda Memesan :")
            # for item in topping_item :
            #     print(item)

            # print("\nTipe Memesan :")
            # for item in topping_item_cate :
            #     print(item)
                
        elif change_tipe.lower() == "m" :
            input_pesanan = input("\nPilih minuman berdasarkan angka (jika lebih dari 1 pisahkan dengan koma): ")
            pesan_nums = [int(pesan_num.strip()) for pesan_num in input_pesanan.split(',') if pesan_num.strip()]

            for pilih in pesan_nums:
                if pilih <= len(minuman_list):
                    item = minuman_list[pilih - 1]
                    minuman_item.append(item)
                    all_item.append(item)
                    
            for pilih in pesan_nums:
                if pilih <= len(minuman_list_cate):
                    item = minuman_list_cate[pilih - 1]
                    minuman_item_cate.append(item)
                    all_item_cate.append(item)

            # print("\nAnda Memesan :")
            # for item in minuman_item :
            #     print(item)

            # print("\nTipe Memesan :")
            # for item in minuman_item_cate :
            #     print(item)
                
        elif change_tipe.lower() == "d" :
            hapus_pilihan = input("\nPilih item berdasarkan angka yang ingin dihapus (pisahkan angka dengan koma jika ingin menghapus lebih dari 1 item): ")
            hapus_nums = [int(num.strip()) for num in hapus_pilihan.split(',') if num.strip()]
            
            for hapus_num in sorted(hapus_nums, reverse=True):
                if hapus_num - 1 < len(all_item):
                    del all_item[hapus_num]
                    
            for hapus_num in sorted(hapus_nums, reverse=True):
                if hapus_num - 1 < len(all_item_cate):
                    del all_item_cate[hapus_num]

            print("\nPesanan berhasil dihapus!")
            
        elif change_tipe.lower() == "v" :
            confirm_v = input("Pesanan akan dipesan, ketik [v] untuk konfirmasi dan lainnya untuk membatalkan :  ")
            if confirm_v.lower() == "v" :
                df = pd.DataFrame(all_item_cate)
                
                kerupuk_group = df.loc[df['Kategori'] == kerupuk_value]
                topping_group = df.loc[df['Kategori'] == topping_value]
                minuman_group = df.loc[df['Kategori'] == minuman_value]
                
                kerupuk_counter = Counter(kerupuk_group['Tipe'])
                topping_counter = Counter(topping_group['Tipe'])
                minuman_counter = Counter(minuman_group['Tipe'])
                
                all_most_common = []
                
                if kerupuk_counter :
                    most_common_kerupuk_tipe = kerupuk_counter.most_common(1)[0][0]
                    all_most_common.append({'common_kerupuk' : most_common_kerupuk_tipe})
                else :
                    all_most_common.append({'common_kerupuk' : menu.common_random()})
                
                if topping_counter :
                    most_common_topping_tipe = topping_counter.most_common(1)[0][0]
                    all_most_common.append({'common_topping' : most_common_topping_tipe})
                else :
                    all_most_common.append({'common_topping' : menu.common_random()})
            
                if minuman_counter :
                    most_common_minuman_tipe = minuman_counter.most_common(1)[0][0]
                    all_most_common.append({'common_minuman' : most_common_minuman_tipe})
                else :
                    all_most_common.append({'common_minuman' : menu.common_random()})
                
                # print(all_most_common)
                
                common_kerupuk = int(all_most_common[0]['common_kerupuk'])
                common_topping = int(all_most_common[1]['common_topping'])
                common_minuman = int(all_most_common[2]['common_minuman'])
                
                # print(common_kerupuk, common_topping, common_minuman, price_total)
                menu.insert_item(common_kerupuk, common_topping, common_minuman, price_total)
                
                print(f"\nPesanan dikonfirmasi\n{order_list}\n")
                
                main.option_start()
            else :
                pass

        elif change_tipe.lower() == "b" :
            main.option_start()
            
        else :
            print("Inisial tidak ada, masukkan inisial lain!")
      
            
if __name__ == "__main__" :
    order_data()