print("selamat datang di parkiran")
print("tarif kendaraan")
print("motor Rp.3.000")
print("mobil Rp.5.000")

def hitung_biaya_parkir (jenis_kendaraan, lama_parkir):
    jenis = jenis_kendaraan
    if jenis == "mobil":
        biaya_perjam = 5000
    elif jenis == "motor":
        biaya_perjam = 3000
    else:
        print("jenis kendaraan tidak dikenal")
        return 0

    total_biaya = biaya_perjam * lama_parkir
    return total_biaya

jenis_kendaraan = input("pilih kendaraan(mobil/motor): ")
jam_masuk = int(input("jam masuk kendaraan (1-24): "))
jam_keluar = int(input("jam keluar kendaraan (1-24): "))

lama_parkir = jam_keluar - jam_masuk

total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

print("BIAYA PARKIR")
print("jenis kendaraan :", jenis_kendaraan)
print("jam masuk       :", jam_masuk)
print("jam keluar      :", jam_keluar) 
print("lama parkir     :", lama_parkir, "jam")
print("total biaya     : Rp", total_biaya) 
print("terima kasih")