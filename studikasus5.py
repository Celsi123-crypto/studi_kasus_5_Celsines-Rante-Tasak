def hitung_parkir(jenis, lama):
    if jenis == "mobil":
        tarif = 5000
    elif jenis == "motor":
        tarif = 3000

    total = tarif * lama
    return total


jenis = input("Jenis kendaraan (mobil/motor): ")
jam_masuk = int(input("Jam masuk: "))
jam_keluar = int(input("Jam keluar: "))

lama_parkir = jam_keluar - jam_masuk

biaya = hitung_parkir(jenis, lama_parkir)

print("=== Data Parkir ===")
print("Jenis kendaraan :", jenis)
print("Jam masuk       :", jam_masuk)
print("Jam_keluar      :", jam_keluar)
print("Lama_parkir     :", lama_parkir, "jam")
print("Total biaya     : Rp", biaya)