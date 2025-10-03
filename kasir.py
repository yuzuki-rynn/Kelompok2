print("===== KASIR IAN =====")
print(" === SELAMAT BERBELANJA ===")

harga = []
barang = []
total_harga = 0
while True:
    print(""""
    ========== MENU TOKO ==========
    -----------------------------------
    |KODE| NAMA MAKANAN | HARGA |
    -----------------------------------
    | 1 | MIE INSTAN   | Rp. 3.000,00  |
    | 2 | NASI GORENG  | Rp. 10.000,00 |
    | 3 | NASI PADANG  | Rp. 15.000,00 |
    | 4 | ES JERUK     | Rp. 5.000,00  |
    | 5 | PECEL LELE   | Rp. 8.000,00  |
    | 6 | ES TEH MANIS | Rp. 3.000,00  |
    | 7 | CORNETO      | Rp. 15.000,00 |
    | 8 | CHITATO      | Rp. 9.000,00  |
    | 9 | LAYS         | Rp. 8.000,00  |
    | 10| BROWNIES     | Rp. 15.000,00 |
    | 11| ULTRAMILK    | Rp. 8.000,00  |
    | 12| COKLAT       | Rp. 6.000,00  |
    | 13| KUSUKA       | Rp. 7.000,00  |
    -----------------------------------
    """)

    KODE = int(input("Masukkan Kode Barang : "))
    if KODE == 1:
        barang.append("MIE INSTAN")
        harga.append(3000)
        total_harga += 3000
    elif KODE == 2:
        barang.append("NASI GORENG")
        harga.append(10000)
        total_harga += 10000
    elif KODE == 3:
        barang.append("NASI PADANG")
        harga.append(15000)
        total_harga += 15000
    elif KODE == 4:
        barang.append("ES JERUK")
        harga.append(5000)
        total_harga += 5000
    elif KODE == 5:
        barang.append("PECEL LELE")
        harga.append(8000)
        total_harga += 8000
    elif KODE == 6:
        barang.append("ES TEH MANIS")
        harga.append(3000)
        total_harga += 3000
    elif KODE == 7:
        barang.append("CORNETO")
        harga.append(15000)
        total_harga += 15000
    elif KODE == 8:
        barang.append("CHITATO")
        harga.append(9000)
        total_harga += 9000
    elif KODE == 9:
        barang.append("LAYS")
        harga.append(8000)
        total_harga += 8000
    elif KODE == 10:
        barang.append("BROWNIES")
        harga.append(15000)
        total_harga += 15000
    elif KODE == 11:
        barang.append("ULTRA MILK")
        harga.append(8000)
        total_harga += 8000
    elif KODE == 12:
        barang.append("COKLAT")
        harga.append(6000)
        total_harga += 6000
    elif KODE == 13:
        barang.append("KUSUKA")
        harga.append(7000)
        total_harga += 7000
    else:
        print("Barang Tidak Terdaftar !!!")

    beli_barang_lain = input("Beli barang lain ?\nTekan (YES/NO) : ").upper()
    if beli_barang_lain == "NO" :
        print("")
        break

print(f"""
Barang : {barang}
Harga : Rp.{harga}
Jumlah Total Harga : Rp.{total_harga}
""")

bayar = int(input("Bayar Rp. "))
if bayar > total_harga - bayar:
    print("Sisa uang kembali :Rp. ", bayar - total_harga)
elif bayar == total_harga:
    print("Anda membayar dengan uang pas tidak ada kembalian !")
else:
    print("Uang yang anda bayarkan kurang :Rp. ", total_harga - bayar)
