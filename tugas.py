tugas = []

while True:
    print("\n=== MENU TO-DO LIST ===")
    print("1. Lihat daftar tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        if len(tugas) == 0:
            print("Santai ae lu kgak ada tugas")
        else:
            print("\nDaftar Tugas:")
            for i in range(len(tugas)):
                print(f"{i+1}. {tugas[i]}")

    elif pilihan == "2":
        tambah = input("Masukkan tugas baru: ")
        tugas.append(tambah)
        print("Wkwk tugas baru yak, udh gw tambahin ni")

    elif pilihan == "3":
        if len(tugas) == 0:
            print("Lu gada tugas kocak, apa yang mau dihapus")
        else:
            for i in range(len(tugas)):
                print(f"{i+1}. {tugas[i]}")
            hapus = int(input("Pilih nomor tugas yang mau dihapus: "))
            if 1 <= hapus <= len(tugas):
                tugas.pop(hapus-1)
                print("Tugas berhasil dihapus")
            else:
                print("Nomor gak valid!")

    elif pilihan == "4":
        print("Bye")
        break

    else:
        print("Pilihan gak valid, coba lagi!")