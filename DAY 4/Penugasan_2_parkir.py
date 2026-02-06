import tkinter as tk
from tkinter import messagebox

BIAYA_PER_JAM = 2000

def hitung_biaya():
    try:
        nopol = entry_nopol.get()
        masuk = int(entry_masuk.get())
        keluar = int(entry_keluar.get())

        if keluar <= masuk:
            messagebox.showerror("Error", "Waktu keluar harus lebih besar")
            return

        lama = keluar - masuk
        biaya = lama * BIAYA_PER_JAM

        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, biaya)

        list_keluar.insert(
            tk.END,
            f"{nopol}\t{masuk}\t{keluar}\tRp {biaya:,}"
        )
        list_bayar.insert(
            tk.END,
            f"{nopol}\t{masuk}\t{keluar}\tRp {biaya:,}"
        )

    except ValueError:
        messagebox.showerror("Error", "Input harus angka!")

# ================= WINDOW =================
root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("800x450")

# ================= JUDUL =================
tk.Label(
    root,
    text="Aplikasi Parkir Kelompok 6",
    font=("Arial", 14, "bold")
).place(x=20, y=10)

# ================= FORM KIRI =================
tk.Label(root, text="Cari NoPol").place(x=20, y=50)
tk.Entry(root).place(x=120, y=50)
tk.Button(root, text="Cari").place(x=260, y=47)

tk.Label(root, text="No Plat Polisi").place(x=20, y=90)
entry_nopol = tk.Entry(root)
entry_nopol.place(x=120, y=90)

tk.Label(root, text="Waktu Masuk").place(x=20, y=130)
entry_masuk = tk.Entry(root)
entry_masuk.place(x=120, y=130)

tk.Label(root, text="Waktu Keluar").place(x=20, y=170)
entry_keluar = tk.Entry(root)
entry_keluar.place(x=120, y=170)

tk.Label(root, text="Biaya").place(x=20, y=210)
entry_biaya = tk.Entry(root)
entry_biaya.place(x=120, y=210)

tk.Button(root, text="Button", width=15, command=hitung_biaya).place(x=120, y=250)

# ================= BIAYA KANAN =================
tk.Label(
    root,
    text="Biaya Per Jam",
    fg="red",
    font=("Arial", 14, "bold")
).place(x=520, y=80)

tk.Label(
    root,
    text="Rp. 2.000",
    fg="red",
    font=("Arial", 24, "bold")
).place(x=520, y=110)

# ================= LIST BAWAH =================
tk.Label(
    root,
    text="List Pelanggan Urut Terakhir Keluar",
    fg="blue"
).place(x=20, y=300)

tk.Label(
    root,
    text="No Plat Polisi   Masuk   Keluar   Biaya"
).place(x=20, y=320)

list_keluar = tk.Listbox(root, width=45, height=5)
list_keluar.place(x=20, y=340)

tk.Label(
    root,
    text="List Pelanggan Banyak Bayar",
    fg="blue"
).place(x=420, y=300)

tk.Label(
    root,
    text="No Plat Polisi   Masuk   Keluar   Biaya"
).place(x=420, y=320)

list_bayar = tk.Listbox(root, width=45, height=5)
list_bayar.place(x=420, y=340)

root.mainloop()