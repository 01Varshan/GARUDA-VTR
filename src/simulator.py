import cv2
import os

KEYFRAME_DIR = "../data/keyframes"

images = sorted(os.listdir(KEYFRAME_DIR))

for image_name in images:

    path = os.path.join(KEYFRAME_DIR, image_name)

    frame = cv2.imread(path)

    cv2.putText(
        frame,
        image_name,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Route Playback", frame)

    key = cv2.waitKey(100)

    if key == 27:
        break

