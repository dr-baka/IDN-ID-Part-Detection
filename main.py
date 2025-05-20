from ultralytics import YOLO
import cv2
from pathlib import Path
import os

# === Konfigurasi ===
MODEL_PATH = "runs/detect/train2/weights/best.pt"
IMAGE_PATH = "example/3.jpeg"
OUTPUT_DIR = "results"
CONFIDENCE_THRESHOLD = 0.1

# === Load model YOLO ===
model = YOLO(MODEL_PATH)

# === Load dan deteksi gambar ===
image_file = Path(IMAGE_PATH)
result = model(image_file, conf=CONFIDENCE_THRESHOLD)[0]

# === Gambar bounding box dan label pada hasil deteksi ===
for box in result.boxes:
    cls = int(box.cls[0])
    label = result.names[cls]
    conf = float(box.conf[0])
    x1, y1, x2, y2 = map(int, box.xyxy[0])

    cv2.rectangle(result.orig_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(result.orig_img, f"{label} {conf:.2f}", (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# === Simpan hasil ke file ===
os.makedirs(OUTPUT_DIR, exist_ok=True)
output_path = Path(OUTPUT_DIR) / image_file.name
cv2.imwrite(str(output_path), result.orig_img)
print(f"[✔] Hasil deteksi disimpan ke: {output_path}")
