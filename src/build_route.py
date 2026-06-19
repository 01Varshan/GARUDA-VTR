import cv2
import os

from route_database import RouteDatabase

KEYFRAME_DIR = "../data/keyframes"
DB_FILE = "../route_database/route.pkl"

orb = cv2.ORB_create(2000)

db = RouteDatabase()

images = sorted(os.listdir(KEYFRAME_DIR))

for idx, image_name in enumerate(images):

    image_path = os.path.join(KEYFRAME_DIR, image_name)

    image = cv2.imread(image_path)

    kp, des = orb.detectAndCompute(image, None)

    if des is None:
        continue

    db.add_keyframe(idx, des)

    print(f"Processed {image_name}")

db.save(DB_FILE)

print("Route database saved.")