#Yehemia Gauand Rizki Mihing Sera (682024031)
#Kalkulator pajak

lebar = 80
print("="* lebar)
print("KULATOR PERHITUNGAN PAJAK".center(lebar))
print("="* lebar)

data_diri = []

data_diri.append(input(f"{"Masukkan Nama":<{40}} : ")) #data diri[0]
data_diri.append(int(input(f"{"Masukkan NIK Anda":<{40}} : "))) #data diri[1]
data_diri.append(input(f"{"Masukkan Tempat Tanggal Lahir Anda":<{40}} : ")) #data diri[2]
data_diri.append(int(input(f"{"Masukkan Usia Anda":<{40}} : "))) #data diri[3]
data_diri.append(input(f"{"Masukkan jenis Kelamin Anda (l/p)":<{40}} : "))#data diri[4]

print("-"* lebar)

data_diri.append(int(input(f"{"Masukkan Pendapatan Tahunan Anda":<{40}} : ")))#data diri[5]
data_diri.append(input(f"{"Apakah Anda sudah Menikah? (ya/tidak)":<{40}} : "))#data diri[6]
data_diri.append(int(input(f"{"Masukkan Jumlah Anak Anda (maksimal 3)":<{40}} : ")))#data diri[7]
data_diri.append(int(input(f"{"Masukkan Pendapatan Tambahan Anda":<{40}} : ")))#data diri[8]

print("\n")
print("="* lebar)
print("RINGKASAN PAJAK ANDA".center(lebar))
print("="* lebar)

print(f"{'Nama lengkap':<{30}} : {data_diri[0]}")
print(f"{'Nomor NIK':<{30}} : {data_diri[1]}")
print(f"{'Tempat, Tanggal lahir':<{30}} : {data_diri[2]}")
print(f"{'Usia':<{30}} : {data_diri[3]} Tahun")
if data_diri[4] == "l":
    print(f"{'Jenis Kelamin':<{30}} : Laki-laki")
elif data_diri[4] == "p":
    print(f"{'Jenis Kelamin':<{30}} : Perempuan")
else:
    print("Input Tidak valid")
    
print("="* lebar)        
pendapatan_bruto = data_diri[5]
data = []
#data[0]
if pendapatan_bruto < 10000000:
    data.append(pendapatan_bruto * 0.02)
elif 10000000 <= pendapatan_bruto < 100000000:
    data.append(pendapatan_bruto * 0.05)
elif 100000000 <= pendapatan_bruto < 250000000:
    data.append(pendapatan_bruto * 0.1) 
else:
    data.append(pendapatan_bruto * 0.15) 

potongan_keluarga = 0
status = data_diri[6]
if status == "ya":
    potongan_menikah = pendapatan_bruto * 0.05
else:
    potongan_menikah = 0    

potongan_anak = min(data_diri[7] * 0.02 * pendapatan_bruto, 0.06 * pendapatan_bruto)
potongan_keluarga += (potongan_menikah + potongan_anak)
data.append(potongan_keluarga) #data[1]

pendapatan_netto_keluarga = pendapatan_bruto - data[1]
data.append(pendapatan_netto_keluarga)#data[2]

pendapatan_netto = pendapatan_bruto - (data[0]+ data[1])
data.append(pendapatan_netto)#data[3]
#data[4]
if data[3] < 10000000:
    data.append(data[3] * 0.02)
elif 10000000 <= data[3] < 100000000:
    data.append(data[3] * 0.05)
elif 100000000 <= data[3] < 250000000:
    data.append(data[3] * 0.1) 
else:
    data.append(data[3] * 0.15) 
    
pajak_pendapatan_tmbhn = (data_diri[8] * 0.5) * 0.1
data.append(pajak_pendapatan_tmbhn) #data[5]  

total_pajak = data[4] + data[5]
data.append(total_pajak) #data[6]

print(f"{'Pendapatan Bruto sebelum potongan':<{50}} : Rp{data_diri[5]:,.2f}")
print(f"{'Diskon dari potongan keluarga (pernikahan & anak)':<{50}} : Rp{data[1]:,.2f}")
print(f"{'Pendapatan bersih setelah potongan':<{50}} : Rp{data[2]:,.2f}")
print(f"{'Pendapatan penghasilan tambahan':<{50}} : Rp{data_diri[8]:,.2f}")
print(f"{'Total pajak penghasilan bersih':<{50}} : Rp{data[4]:,.2f}")
print(f"{'Total pajak penghasilan tambahan':<{50}} : Rp{data[5]:,.2f}")
print("-"* lebar)

print(f"{'Total pajak yang harus dibayarkan':<{50}} : Rp{data[6]:,.2f}")
