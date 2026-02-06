# Definisikan kelas dasar Vehicle
class Vehicle:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

    def tampilkan_info(self):
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")
        print(f"Warna: {self.warna}")

# Definisikan kelas turunan Car yang mewarisi dari Vehicle
class car(Vehicle):
    def __init__(self, merk, tahun, warna, model):
        # Panggil kondtruktor kelas dasar
        super().__init__(merk, tahun, warna)
        self.model = model

    def tampilkan_info(self):
        # Panggil metode kelas dasar untuk menampilkan info kendaaran
        super().tampilkan_info()
        print(f"Model: {self.model}")

# Program Utama
if __name__ == "__main__":
    car = car("Toyota", 2022, "Merah", "Camry")

    print("Info Kendaraan:")
    car.tampilkan_info()