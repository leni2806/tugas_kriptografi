"""Vigenere Cipher (cipher abjad-majemuk) - Tugas Kriptografi

Enkripsi: c_i = (p_i + k_i) mod 26
Dekripsi: p_i = (c_i - k_i) mod 26
Kunci diulang; huruf kunci hanya maju saat plainteks berupa huruf.
"""
import tkinter as tk
from tkinter import ttk, messagebox


def _vigenere(text, key, sign):
    shifts = [ord(c) - ord("A") for c in key.upper()]
    result, i = [], 0
    for ch in text:
        if ch.isascii() and ch.isalpha():
            start = ord("A") if ch.isupper() else ord("a")
            shift = shifts[i % len(shifts)] * sign
            result.append(chr((ord(ch) - start + shift) % 26 + start))
            i += 1
        else:
            result.append(ch)
    return "".join(result)


def vigenere_encrypt(text, key):
    return _vigenere(text, key, 1)


def vigenere_decrypt(text, key):
    return _vigenere(text, key, -1)


def valid_key(key):
    return bool(key) and key.isascii() and key.isalpha()


class VigenereApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vigenere Cipher")
        self.geometry("660x560")
        self.minsize(560, 480)

        ttk.Label(self, text="Vigenere Cipher", font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        ttk.Label(self, text="Enkripsi: c = (p + k) mod 26     Dekripsi: p = (c - k) mod 26").pack(anchor="w", padx=10)

        ttk.Label(self, text="Teks input (plainteks / cipherteks):").pack(anchor="w", padx=10, pady=(10, 2))
        self.inp = tk.Text(self, height=6, wrap="word", font=("Consolas", 11))
        self.inp.pack(fill="x", padx=10)

        row = ttk.Frame(self)
        row.pack(fill="x", padx=10, pady=8)
        ttk.Label(row, text="Kunci (huruf):").pack(side="left")
        self.key = tk.StringVar(value="KEY")
        ttk.Entry(row, textvariable=self.key, width=18).pack(side="left", padx=6)
        ttk.Button(row, text="Enkripsi", command=self.encrypt).pack(side="left", padx=4)
        ttk.Button(row, text="Dekripsi", command=self.decrypt).pack(side="left", padx=4)

        ttk.Label(self, text="Hasil:").pack(anchor="w", padx=10, pady=(4, 2))
        self.out = tk.Text(self, height=10, wrap="word", font=("Consolas", 11))
        self.out.pack(fill="both", expand=True, padx=10)

        row2 = ttk.Frame(self)
        row2.pack(fill="x", padx=10, pady=8)
        ttk.Button(row2, text="Salin Hasil", command=self.copy).pack(side="left", padx=(0, 4))
        ttk.Button(row2, text="Bersihkan", command=self.clear).pack(side="left", padx=4)

    def _inputs(self):
        text, key = self.inp.get("1.0", "end-1c"), self.key.get().strip()
        if not text.strip():
            messagebox.showwarning("Input kosong", "Isi teks terlebih dahulu.")
            return None
        if not valid_key(key):
            messagebox.showerror("Kunci tidak valid", "Kunci harus berupa huruf A-Z saja (tanpa spasi/angka).")
            return None
        return text, key

    def _set_out(self, text):
        self.out.delete("1.0", "end")
        self.out.insert("1.0", text)

    def encrypt(self):
        data = self._inputs()
        if data:
            self._set_out(vigenere_encrypt(*data))

    def decrypt(self):
        data = self._inputs()
        if data:
            self._set_out(vigenere_decrypt(*data))

    def copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.out.get("1.0", "end-1c"))

    def clear(self):
        self.inp.delete("1.0", "end")
        self.out.delete("1.0", "end")


if __name__ == "__main__":
    VigenereApp().mainloop()
