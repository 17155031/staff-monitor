import cv2
import time
import os

def capture_images(interval=200, save_path="captured_images"):
    def capture_and_save_image(image_count):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        ret, frame = cap.read()
        if ret:
            file_name = os.path.join(save_path, f'image_{image_count:03}.jpeg')
            cv2.imwrite(file_name, frame)
            print(f"Fotoğraf başarıyla kaydedildi: {file_name}")
        else:
            print("Fotoğraf yakalanamadı.")
        cap.release()

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    image_count = 0
    while True:
        capture_and_save_image(image_count)
        image_count += 1
        time.sleep(interval)

