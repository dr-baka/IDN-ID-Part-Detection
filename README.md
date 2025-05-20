# KTP Part Detector with YOLOv8

Proyek ini adalah aplikasi deteksi objek berbasis [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics), yang digunakan untuk mendeteksi bagian-bagian tertentu dari KTP Indonesia (misalnya: NIK, Nama, TTL, dll) berdasarkan bounding box hasil training kustom.

## 🚀 Fitur
- Menggunakan YOLOv8 untuk deteksi bagian KTP dari gambar.
- Threshold deteksi dapat diatur dengan mudah.
- Menyimpan hasil deteksi ke folder `results/`.
- Mendukung inference dari gambar lokal.

---

## 📦 Struktur Proyek

```
project-root/
├── main.py                # Script utama untuk mendeteksi bagian KTP
├── results/               # Folder output untuk hasil deteksi (hasil akan otomatis disimpan di sini)
├── example/
│   └── dayat.jpg          # Contoh gambar untuk diuji
├── runs/
│   └── detect/train2/     # Folder model hasil training YOLOv8
│       └── weights/
│           └── best.pt    # Model hasil training (checkpoint terbaik)
├── README.md              # Dokumentasi proyek ini
```

---

## 🛠️ Cara Menjalankan

### 1. Instalasi dependensi

Gunakan Python 3.8+ dan virtual environment:

```bash
pip install ultralytics opencv-python
```

### 2. Jalankan script

```bash
python main.py
```

Output akan muncul di terminal:

```
[✔] Hasil deteksi disimpan ke: results/dayat.jpg
```

---

## ⚙️ Konfigurasi

Dalam file `main.py`, kamu bisa ubah parameter berikut:

```python
MODEL_PATH = "runs/detect/train2/weights/best.pt"  # Ganti path model jika perlu
IMAGE_PATH = "example/dayat.jpg"                   # Ganti path gambar uji
OUTPUT_DIR = "results"                             # Folder output hasil deteksi
CONFIDENCE_THRESHOLD = 0.1                         # Minimum confidence untuk menampilkan deteksi
```

---

## 🧠 Catatan

- Model `best.pt` harus sudah dilatih sebelumnya dengan dataset berisi gambar KTP dan label bounding box bagian-bagian yang ingin dideteksi.
- Model harus memiliki anotasi dengan format YOLOv8 dan struktur folder dataset seperti:
  ```
  dataset/
  ├── images/
  │   ├── train/
  │   └── val/
  └── labels/
      ├── train/
      └── val/
  ```

---

## 📸 Contoh Output

Gambar hasil akan memiliki bounding box dan label seperti:

```
+---------------------------+
| NAMA        [0.95]       |
| -----------------------  |
| TTL         [0.87]       |
+---------------------------+
```

---

## 📄 Lisensi

Proyek ini bersifat open-source dan bebas digunakan untuk keperluan pembelajaran dan riset.

---