"""Rail Fence Cipher (cipher transposisi) - Tugas Kriptografi

Plainteks ditulis zig-zag pada k baris, cipherteks dibaca baris demi baris.
Spasi dibuang sebelum enkripsi (seperti contoh di materi).
"""
import tkinter as tk
from tkinter import ttk, messagebox


def _pattern(n, k):
    if k == 1:
        return [0] * n
    cycle = list(range(k)) + list(range(k - 2, 0, -1))
    return [cycle[i % len(cycle)] for i in range(n)]


def _order(n, k):
    pat = _pattern(n, k)
    return sorted(range(n), key=lambda i: (pat[i], i))


def railfence_encrypt(text, k):
    text = "".join(text.split())
    return "".join(text[i] for i in _order(len(text), k))


def railfence_decrypt(cipher, k):
    cipher = "".join(cipher.split())
    plain = [""] * len(cipher)
    for pos, i in enumerate(_order(len(cipher), k)):
        plain[i] = cipher[pos]
    return "".join(plain)


def railfence_grid(text, k):
    """Tampilan zig-zag seperti di slide."""
    text = "".join(text.split())
    pat = _pattern(len(text), k)
    rows = [[" "] * len(text) for _ in range(k)]
    for i, ch in enumerate(text):
        rows[pat[i]][i] = ch
    return "\n".join(" ".join(r) for r in rows)


class RailFenceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rail Fence Cipher")
        self.geometry("700x640")
        self.minsize(560, 520)

        ttk.Label(self, text="Rail Fence Cipher", font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
        ttk.Label(self, text="Cipher transposisi: teks disusun zig-zag pada k baris").pack(anchor="w", padx=10)

        ttk.Label(self, text="Teks input (plainteks / cipherteks):").pack(anchor="w", padx=10, pady=(10, 2))
        self.inp = tk.Text(self, height=5, wrap="word", font=("Consolas", 11))
        self.inp.pack(fill="x", padx=10)

        row = ttk.Frame(self)
        row.pack(fill="x", padx=10, pady=8)
        ttk.Label(row, text="Jumlah baris (k):").pack(side="left")
        self.key = tk.StringVar(value="3")
        ttk.Spinbox(row, from_=2, to=20, width=5, textvariable=self.key).pack(side="left", padx=6)
        ttk.Button(row, text="Enkripsi", command=self.encrypt).pack(side="left", padx=4)
        ttk.Button(row, text="Dekripsi", command=self.decrypt).pack(side="left", padx=4)

        ttk.Label(self, text="Hasil:").pack(anchor="w", padx=10, pady=(4, 2))
        self.out = tk.Text(self, height=4, wrap="word", font=("Consolas", 11))
        self.out.pack(fill="x", padx=10)

        ttk.Label(self, text="Visualisasi zig-zag:").pack(anchor="w", padx=10, pady=(8, 2))
        self.viz = tk.Text(self, height=8, wrap="none", font=("Consolas", 11))
        self.viz.pack(fill="both", expand=True, padx=10)

        row2 = ttk.Frame(self)
        row2.pack(fill="x", padx=10, pady=8)
        ttk.Button(row2, text="Salin Hasil", command=self.copy).pack(side="left", padx=(0, 4))
        ttk.Button(row2, text="Bersihkan", command=self.clear).pack(side="left", padx=4)

    def _inputs(self):
        text = self.inp.get("1.0", "end-1c")
        if not text.strip():
            messagebox.showwarning("Input kosong", "Isi teks terlebih dahulu.")
            return None
        try:
            k = int(self.key.get())
            if k < 2:
                raise ValueError
        except ValueError:
            messagebox.showerror("Kunci tidak valid", "Jumlah baris harus bilangan bulat >= 2.")
            return None
        return text, k

    def _show(self, widget, text):
        widget.delete("1.0", "end")
        widget.insert("1.0", text)

    def encrypt(self):
        data = self._inputs()
        if data:
            text, k = data
            self._show(self.out, railfence_encrypt(text, k))
            self._show(self.viz, railfence_grid(text, k))

    def decrypt(self):
        data = self._inputs()
        if data:
            cipher, k = data
            plain = railfence_decrypt(cipher, k)
            self._show(self.out, plain)
            self._show(self.viz, railfence_grid(plain, k))

    def copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.out.get("1.0", "end-1c"))

    def clear(self):
        for w in (self.inp, self.out, self.viz):
            w.delete("1.0", "end")


if __name__ == "__main__":
    RailFenceApp().mainloop()
