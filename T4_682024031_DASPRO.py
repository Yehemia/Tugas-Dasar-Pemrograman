#Yehemia Gauand Rizki Mihing Sera (682024031)
# Struk kasir

print('Selamat datang di Kupi')
print('Get discount 30% for minimum order 50K')
print("--------------------------------------")

nama = input('silahkan masukan Nama anda = ') #input nama pembeli

# Dictionary menu 
menu = {
    "Salad": 15000,
    "Americano": 20000,
    "Latte": 18000,
    "Cappucino": 22000,
    "Nasgor": 15000,
}    
print("=========================================")
print('==================Menu===================')
print("=========================================")

for i in menu:
    print("daftar menu : ", i,"\t harga : Rp.", menu[i])

pesanan = [] #List untuk menyimpan pesanan
total_bayar = 0 #variabel untuk menyimpan total harga pembelian

#untuk membuat lebih dari 1 pesanan
while True:
    try:
        beli = input("Masukkan menu yang ingin anda beli: ").title()
        #untuk mengecek apakah menu ada
        if beli not in menu:
            print("Maaf menu tidak ada")
            continue
        
        jumlah = int(input(f"Masukkan jumlah pembelian {beli}: "))
        bayar = menu[beli] * jumlah
        total_bayar += bayar
        
        pesanan.append({
            "menu": beli,
            "jumlah": jumlah,
            "subtotal": bayar 
        })
        
        lanjut = input("Apakah ingin menambah pesanan lain? (y/n): ").lower()
        if lanjut == 'y':
            continue
        elif lanjut == 'n':
            break

    except ValueError:
        print("Input yang dimasukkan bukan angka")
        
#untuk mengecek diskon
if total_bayar > 50000:
    diskon = total_bayar * 30/100
    total_setelah_diskon = total_bayar - diskon
else:
    diskon = 0
    total_setelah_diskon= total_bayar   

# Cetak struk pemjualan
print("==========Detail Pembayaran===========")
print("--------------------------------------")
print('HAI KUPIERS!!!')           
print("Jalan Terbaik No. 1, Salatiga")
print("--------------------------------------")

for x in pesanan:
    print(f"{x['menu']} x {x['jumlah']} = Rp. {x['subtotal']}")

print("--------------------------------------")
print(f"Subtotal = Rp. {total_bayar}")
print(f"Diskon = Rp. {diskon}")
print(f"Total = Rp. {total_setelah_diskon}")
print("**************************************")
print("Terimakasih telah berbelanja di Kupi!")
print(f"Have a great day, {nama}!")


