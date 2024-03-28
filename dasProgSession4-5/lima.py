#daftar barang
barang = {
    "Buku": {"harga": 10000, "stok":15},
    "Pensil": {"harga": 2000, "stok": 20},
    "Penggaris": {"harga": 3000, "stok": 10},
}
#menampilkan daftar barang
while True:
    print("Daftar Barang:")
    for nama, info in barang.items():
        print(f"- {nama}: {info['harga']} (stok: {info['stok']})")
    print()

    #memilih barang
    nama_barang = input("Masukan nama barang:").strip()
    if nama_barang not in barang:
        print("Barang tidak ditemukan!")
        continue

    #menentukan jumlah barang
    while True:
        try:
            jumlah = int(input("Masukan jumlah barang:"))
            if jumlah <= 0 or jumlah > barang[nama_barang]["stok"]:
                raise valueError:
            break
        except valueError:
            print("Jumlah barang tidak valid!")
    #menghitung total harga
    total_harga = jumlah * barang[nama_barang]["harga"]
    #menampilkan detail transaksi
    print(f"\nDetail Transaksi:")
    print(f"- Barang: {nama_barang}")
    print(f"- Jumlah: {jumlah}")
    print(f"- Harga: {barang[nama_barang]['harga']}")
    print(f"- Total Harga: {total_harga}")
    #menghitung keuntungan
    keuntungan = total_harga - (jumlah * barang[nama_barang]["harga_beli"])
    print(f"- Keuntungan: {keuntungan}")
    #menanyakan transaksi berikutnya
    lagi = input("\nApakah ingin melakukan transaksi lagi? (y/n)").strip().lower()
    if lagi != "y":
        break
    #menampilkan total keuntungan
    total_keuntungan = 0
    for nama, info in barang.items():
        total_keuntungan +=(info["stok"] * info["harga"]) - (info["stok"]) - (info["harga_beli"])
    print(f"\nTotal Keuntungan: {total_keuntungan}")