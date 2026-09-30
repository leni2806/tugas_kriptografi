# Cipher Klasik

Tiga aplikasi cipher klasik (Python + tkinter) untuk tugas Kriptografi

| File | Cipher | Jenis | Kunci |
|---|---|---|---|
| `caesar_cipher.py` | Caesar | Substitusi | angka `k` (ada Brute Force) |
| `vigenere_cipher.py` | Vigenere | Substitusi abjad-majemuk | kata (huruf A-Z) |
| `railfence_cipher.py` | Rail Fence | Transposisi | jumlah baris (min. 2) |

## Cara Menjalankan
python caesar_cipher.py
python vigenere_cipher.py
python railfence_cipher.py
```

## Cara Menggunakan
1. Ketik teks di kolom **Teks input**.
2. Isi kunci: angka untuk Caesar (misal `3`), kata untuk Vigenere (misal `KEY`), jumlah baris untuk Rail Fence (misal `3`).
3. Klik **Enkripsi** atau **Dekripsi** (pakai kunci yang sama).
4. Hasil muncul di kolom **Hasil**, bisa disalin dengan **Salin Hasil**.
5. Khusus Caesar: klik **Brute Force** untuk mencoba semua kunci 0-25.

## Contoh
- Caesar, k = 3: `awasi asterix dan temannya obelix` -> `dzdvl dvwhula gdq whpdqqbd rehola`
- Vigenere, kunci `KEY`: `she sells sea shells by the seashore` -> `clc cijvw qoe qrijvw zi xfo wckwfyvc`
- Rail Fence, k = 3: `CRYPTOGRAPHY AND DATA SECURITY` -> `CTAAAEIRPORPYNDTSCRTYGHDAUY`

Catatan: Rail Fence membuang spasi, jadi hasil dekripsinya tanpa spasi.

