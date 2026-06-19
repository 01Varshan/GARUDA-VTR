import cv2

IMAGE_PATH = "../data/test.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Could not load image")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(2000)

keypoints, descriptors = orb.detectAndCompute(gray, None)

output = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

print(f"Detected Features: {len(keypoints)}")

cv2.imshow("ORB Features", output)

cv2.waitKey(0)
cv2.destroyAllWindows()