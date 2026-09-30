"""Caesar Cipher - Tugas Kriptografi (Cipher Klasik)

Enkripsi: c = (p + k) mod 26
Dekripsi: p = (c - k) mod 26
Hanya huruf alfabet yang diproses; angka, spasi, dan tanda baca dibiarkan.
"""
import tkinter as tk
from tkinter import ttk, messagebox


def caesar_encrypt(text, k):
    result = []
    for ch in text:
        if ch.isascii() and ch.isalpha():
            start = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - start + k) % 26 + start))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)


def brute_force(text):
    """Exhaustive key search: coba semua kunci 0..25."""
    return [(k, caesar_decrypt(text, k)) for k in range(26)]


class CaesarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Caesar Cipher")
        self.geometry("660x600")
        self.minsize(560, 500)

        ttk.Label(self, text="Caesar Cipher", font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        ttk.Label(self, text="Enkripsi: c = (p + k) mod 26     Dekripsi: p = (c - k) mod 26").pack(anchor="w", padx=10)

        ttk.Label(self, text="Teks input (plainteks / cipherteks):").pack(anchor="w", padx=10, pady=(10, 2))
        self.inp = tk.Text(self, height=6, wrap="word", font=("Consolas", 11))
        self.inp.pack(fill="x", padx=10)

        row = ttk.Frame(self)
        row.pack(fill="x", padx=10, pady=8)
        ttk.Label(row, text="Kunci (k):").pack(side="left")
        self.key = tk.StringVar(value="3")
        ttk.Spinbox(row, from_=0, to=25, width=5, textvariable=self.key).pack(side="left", padx=6)
        ttk.Button(row, text="Enkripsi", command=self.encrypt).pack(side="left", padx=4)
        ttk.Button(row, text="Dekripsi", command=self.decrypt).pack(side="left", padx=4)
        ttk.Button(row, text="Brute Force", command=self.brute).pack(side="left", padx=4)

        ttk.Label(self, text="Hasil:").pack(anchor="w", padx=10, pady=(4, 2))
        self.out = tk.Text(self, height=14, wrap="word", font=("Consolas", 11))
        self.out.pack(fill="both", expand=True, padx=10)

        row2 = ttk.Frame(self)
        row2.pack(fill="x", padx=10, pady=8)
        ttk.Button(row2, text="Salin Hasil", command=self.copy).pack(side="left", padx=(0, 4))
        ttk.Button(row2, text="Bersihkan", command=self.clear).pack(side="left", padx=4)

    def _get_key(self):
        try:
            return int(self.key.get())
        except ValueError:
            messagebox.showerror("Kunci tidak valid", "Kunci harus berupa bilangan bulat.")
            return None

    def _get_text(self):
        text = self.inp.get("1.0", "end-1c")
        if not text.strip():
            messagebox.showwarning("Input kosong", "Isi teks terlebih dahulu.")
            return None
        return text

    def _set_out(self, text):
        self.out.delete("1.0", "end")
        self.out.insert("1.0", text)

    def encrypt(self):
        k, text = self._get_key(), self._get_text()
        if k is not None and text is not None:
            self._set_out(caesar_encrypt(text, k))

    def decrypt(self):
        k, text = self._get_key(), self._get_text()
        if k is not None and text is not None:
            self._set_out(caesar_decrypt(text, k))

    def brute(self):
        text = self._get_text()
        if text is not None:
            self._set_out("\n".join(f"k = {k:2d} : {p}" for k, p in brute_force(text)))

    def copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.out.get("1.0", "end-1c"))

    def clear(self):
        self.inp.delete("1.0", "end")
        self.out.delete("1.0", "end")


if __name__ == "__main__":
    CaesarApp().mainloop()
