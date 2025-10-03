menu = {
    "Fried Chiken" :15000,
    "Burger Queen" :25000,
    "French Fries" :10000,
    "Es Teh Hangat" :3000,
    "Coca Cola" :12000,
}
print("=================== Daftar Menu ===================")
for i in menu:
    print("Daftar Menu : ", i,"\t  Harga : ",menu[i])
print("Pembelian di atas Rp100.000,- mendapakan diskon 15%")
print("===================================================")
beli = input("Pilih Menu : ")
jumlah = int(input("Jumlah Pesanan : "))
bayar = jumlah * menu[beli]

if bayar > 100000:
    diskon = bayar * 15/100
    total = bayar - diskon
else:
    total = bayar

print("=================== Detail Pembayaran ===================")
print("Menu yang dipesann       : ",beli)
print("Jumlah yang dipesann     : ",jumlah)
print("Total Biaya              : ",bayar)
print("Total yang harus dibayar : ",total)