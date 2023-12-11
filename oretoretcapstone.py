from tabulate import tabulate

daftarBarang = [
    [223001, 'Pensil', 20, 1000, 'PT Sakti'],
    [223002, 'Spidol', 15, 2500, 'PT ASD'],
    [223003, 'Batre', 25, 5000,'PT PintarOYE']
]

def tabel_data(data):
    headers = ["Kode Barang", "Nama", "Stock", "Harga", "Supplier"]
    return tabulate(data, headers=headers, tablefmt="pretty")

def showstock():
    while True:
        print('Daftar Barang')
        print(tabel_data(daftarBarang))
        cariBarang = input("Ingin mencari barang berdasarkan nama? atau ketik 'n' untuk kembali ke menu utama (y/n): ").lower()
        if cariBarang == 'y':
            cariNama = input("Masukkan nama barang yang ingin dicari: ").lower()
            hasilpencarian = [i for i in daftarBarang if cariNama in i[1].lower()]
            if hasilpencarian:
                print('\nHasil Pencarian:')
                print(tabel_data(hasilpencarian))
            else:
                print(f'Tidak ditemukan barang dengan nama "{cariNama}"')
        elif cariBarang == 'n':
            break
        else:
            print("Input tidak valid. Harap masukkan 'y' atau 'n'.")

def tambah_barang():
    try:
        barang = str(input("Masukkan Nama Barang : ").title())
        stok = int(input("Masukkan Stock Persediaan Barang : "))
        harga = int(input("Masukkan Harga Barang : "))
        supplier = str(input("Masukkan Supplier Barang : "))
        kode = daftarBarang[-1][0] + 1
        daftarBaru = [kode, barang, stok, harga, supplier]
        daftarBarang.append(daftarBaru)        
        print('Daftar Barang setelah penambahan:')
        print(tabel_data(daftarBarang))
        print('\n')
    except ValueError:
        print('Input tidak valid, pastikan anda memasukan angka pada harga dan jumlah barang')

def delete_barang():
    try:
        print('Daftar Barang sebelum penghapusan:')
        print(tabel_data(daftarBarang))
        while True:
            delete_kode = int(input("Masukkan Kode Barang yang Ingin Dihapus : "))
            for i in range(len(daftarBarang)):
                if daftarBarang[i][0] == delete_kode:
                    daftarBarang.pop(i)
                    print('Barang berhasil dihapus.')
                    print('Daftar Barang setelah penghapusan:')
                    print(tabel_data(daftarBarang))
                    print('\n')
                    break            
            else:
                print('Kode tidak ditemukan')
            break 
    except ValueError:
        print('Input tidak valid, pastikan anda memasukan angka pada kode barang')

def update_barang():
    try:
        print('Daftar Barang sebelum pembaruan:')
        print(tabel_data(daftarBarang))
        update_kode = int(input("Masukkan Kode Barang yang Ingin Diupdate : "))
        for i in range(len(daftarBarang)):
            if daftarBarang[i][0] == update_kode:
                stokBaru = int(input("Masukkan Jumlah Stok yang Baru : "))
                daftarBarang[i][2] = stokBaru
                hargaBaru = int(input("Masukkan Harga yang Baru : "))
                daftarBarang[i][3] = hargaBaru

                print('Barang berhasil diupdate.')
                print('Daftar Barang setelah pembaruan:')
                print(tabel_data(daftarBarang))
                print('\n')
                break
        else:
            print('Kode tidak valid. Pastikan kode yang Anda input sesuai.')
    except ValueError:
        print('Input tidak valid, pastikan anda memasukan angka pada harga dan jumlah barang')

while True:
    print(f'\nSelamat Datang di Inventory Management System PT Purwadhika')
    print('''List Menu :
          1. Menampilkan Daftar Ketersediaan Barang
          2. Menambah Jenis Barang
          3. Menghapus Jenis Barang
          4. Update Barang (Stock, Harga)
          5. Exit Program  
      ''')
    menu = int(input("Masukkan Angka Menu yang Dijalankan (1-5) : "))

    if menu == 1:
        showstock()
    elif menu == 2:
        tambah_barang()
    elif menu == 3:
        delete_barang()
    elif menu == 4:
        update_barang()
    elif menu == 5:
        print('Terimakasih telah menggunakan Inventory Management System PT Purwadhika')
        break
    else :
        print('Masukkan Angka 1-5')