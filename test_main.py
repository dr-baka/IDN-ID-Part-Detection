import unittest
from ultralytics import YOLO
from pathlib import Path
import os

class TestKTPDetection(unittest.TestCase):
    MODEL_PATH = "runs/detect/train2/weights/best.pt"
    TEST_IMAGE = "example/dayat.jpg"
    CONFIDENCE_THRESHOLD = 0.1

    def setUp(self):
        self.model = YOLO(self.MODEL_PATH)
        self.image_file = Path(self.TEST_IMAGE)
        self.assertTrue(self.image_file.exists(), f"Test image not found: {self.image_file}")

    def test_detection(self):
        result = self.model(self.image_file, conf=self.CONFIDENCE_THRESHOLD)[0]
        detections = result.boxes

        # Pastikan setidaknya ada 1 deteksi
        self.assertGreater(len(detections), 0, "No detection found.")

        # Validasi setiap deteksi memiliki label dan confidence yang valid
        for box in detections:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            self.assertIn(cls, result.names, "Invalid class label.")
            self.assertGreaterEqual(conf, self.CONFIDENCE_THRESHOLD, "Confidence below threshold.")

if __name__ == '__main__':
    unittest.main()
