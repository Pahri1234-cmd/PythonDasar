import tkinter as tk
from tkinter import messagebox

def simpan_data():
    data = {
        "Nama": entry_nama.get(),
        "Tanggal Lahir": entry_ttl.get(),
        "Asal Sekolah": entry_sekolah.get(),
        "NISN": entry_nisn.get(),
        "Nama Ayah": entry_ayah.get(),
        "Nama Ibu": entry_ibu.get(),
        "No HP": entry_hp.get(),
        "Alamat": text_alamat.get("1.0", tk.END).strip()
    }

    if data["Nama"] == "" or data["NISN"] == "":
        messagebox.showwarning("Peringatan", "Nama dan NISN wajib diisi!")
        return

    messagebox.showinfo("Sukses", "Data siswa berhasil disimpan")

def hapus_data():
    entry_nama.delete(0, tk.END)
    entry_ttl.delete(0, tk.END)
    entry_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

# ================= WINDOW =================
root = tk.Tk()
root.title("MainWindow")
root.geometry("700x600")
root.configure(bg="#dddddd")

# ================= HEADER =================
header = tk.Frame(root, bg="#9fe3e6", height=60)
header.pack(fill="x")

tk.Label(
    header,
    text="DATA SISWA BARU",
    bg="#9fe3e6",
    font=("Arial", 18, "bold")
).pack(pady=15)

# ================= FORM =================
form = tk.Frame(root, bg="#dddddd")
form.pack(padx=40, pady=20, fill="x")

def buat_field(label, row):
    tk.Label(form, text=label, bg="#dddddd").grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(form, width=60)
    entry.grid(row=row, column=1, pady=5)
    return entry

entry_nama = buat_field("Nama Lengkap", 0)
entry_ttl = buat_field("Tanggal Lahir", 1)
entry_sekolah = buat_field("Asal Sekolah", 2)
entry_nisn = buat_field("NISN", 3)
entry_ayah = buat_field("Nama Ayah", 4)
entry_ibu = buat_field("Nama Ibu", 5)
entry_hp = buat_field("Nomor Telepon / HP", 6)

# ================= ALAMAT =================
tk.Label(form, text="Alamat", bg="#dddddd").grid(row=7, column=0, sticky="nw", pady=5)
text_alamat = tk.Text(form, width=60, height=5)
text_alamat.grid(row=7, column=1, pady=5)

# ================= FOOTER =================
footer = tk.Frame(root, bg="#8fc5c8", height=60)
footer.pack(fill="x", side="bottom")

tk.Button(
    footer,
    text="Hapus",
    bg="#c96b4a",
    fg="white",
    width=12,
    command=hapus_data
).pack(side="right", padx=10, pady=15)

tk.Button(
    footer,
    text="Simpan",
    bg="#c96b4a",
    fg="white",
    width=12,
    command=simpan_data
).pack(side="right", pady=15)

root.mainloop()