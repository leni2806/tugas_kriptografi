# Vigenere Cipher

Aplikasi GUI (Python + tkinter) untuk enkripsi & dekripsi **Vigenere Cipher** (cipher abjad-majemuk), dibuat untuk tugas Kriptografi (Cipher Klasik).

- Enkripsi: `c_i = (p_i + k_i) mod 26`
- Dekripsi: `p_i = (c_i - k_i) mod 26`
- Kunci berupa kata (huruf A-Z), diulang sepanjang pesan. Huruf kunci hanya maju saat karakter pesan berupa huruf.
- Contoh: `she sells sea shells by the seashore` + kunci `KEY` -> `CLC CIJVW QOE QRIJVW ZI XFO WCKWFYVC`

## Cara menjalankan
```
python vigenere_cipher.py
```
