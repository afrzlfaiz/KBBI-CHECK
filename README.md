# KBBI Word Checker 📚

Web application untuk memeriksa kata baku sesuai Kamus Besar Bahasa Indonesia (KBBI).

## ✨ Fitur

- ✅ Cek kata baku sesuai KBBI
- 📝 Input kata dengan pemisah newline atau koma
- 🚀 Proses paralel untuk hasil cepat
- 📱 Responsive design
- 🎨 UI modern dan user-friendly

## 🚀 Cara Menjalankan Lokal

### Prasyarat

- Python 3.7+
- pip

### Instalasi

```bash
# Clone repository
git clone https://github.com/afrzlfaiz/KBBI-CHECK.git
cd KBBI-CHECK

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
python app.py
```

Buka browser dan akses `http://localhost:5000`

## 🌐 Demo Online

Coba langsung: **[https://kbbi-check.onrender.com/](https://kbbi-check.onrender.com/)**

## 📁 Struktur Project

```
KBBI LIST/
├── app.py              # Flask backend
├── requirements.txt    # Dependencies
├── render.yaml         # Render.com config
├── README.md           # Dokumentasi
└── templates/
    └── index.html      # Frontend UI
```

## 🔧 Teknologi

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **API**: KBBI Web (kbbi.web.id)
- **Deployment**: Render.com

## 📝 Cara Menggunakan

1. Masukkan kata-kata yang ingin diperiksa di textarea
2. Pisahkan dengan **newline** (Enter) atau **koma** (,)
3. Klik tombol **Periksa Kata**
4. Tunggu hasil pemeriksaan muncul di 2 kolom:
   - ✅ **Kata Baku** - kata yang ditemukan di KBBI
   - ❌ **Tidak Ditemukan** - kata yang tidak ditemukan

**Tips**: Gunakan `Ctrl+Enter` untuk langsung memeriksa kata.

## ⚠️ Catatan

- Aplikasi ini menggunakan API dari kbbi.web.id
- Pastikan koneksi internet stabil saat menjalankan aplikasi
- Jumlah kata yang diperiksa secara paralel dibatasi 20 concurrent requests

## 📄 License

MIT License
