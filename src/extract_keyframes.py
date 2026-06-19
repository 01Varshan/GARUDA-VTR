import cv2
import os

VIDEO_PATH = "../data/route_video.mp4"
OUTPUT_DIR = "../data/keyframes"

os.makedirs(OUTPUT_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print(f"ERROR: Cannot open {VIDEO_PATH}")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Video FPS: {fps}")

frame_interval = int(fps)  # save 1 frame/sec

frame_count = 0
saved_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % frame_interval == 0:

        filename = os.path.join(
            OUTPUT_DIR,
            f"frame_{saved_count:04d}.jpg"
        )

        cv2.imwrite(filename, frame)

        print(f"Saved {filename}")

        saved_count += 1

    frame_count += 1

cap.release()

print()
print("Finished")
print(f"Frames saved: {saved_count}")