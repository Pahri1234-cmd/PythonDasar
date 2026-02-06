# Input
nama = input("Masukkan nama karyawan: ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

# Proses
tunjangan = 0.20 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

# Output
print("\n=== Slip Gaji ===")
print("Nama          :", nama)
print("Gaji Pokok    :", gaji_pokok)
print("Gaji Bersih   :", gaji_bersih)