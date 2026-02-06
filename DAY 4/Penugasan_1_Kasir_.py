import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        harga = float(entry_harga.get())
        qty = int(entry_qty.get())
        total = harga * qty
        label_total.config(text=f"Total: Rp {total:,.0f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Window utama
root = tk.Tk()
root.title("Program Kasir")
root.geometry("300x200")

# Label & Entry Harga
tk.Label(root, text="Harga:").pack()
entry_harga = tk.Entry(root)
entry_harga.pack()

# Label & Entry Kuantitas
tk.Label(root, text="Kuantitas:").pack()
entry_qty = tk.Entry(root)
entry_qty.pack()

# Tombol Hitung
tk.Button(root, text="Hitung Total", command=hitung_total).pack(pady=10)

# Label Total
label_total = tk.Label(root, text="Total: Rp 0")
label_total.pack()

root.mainloop()