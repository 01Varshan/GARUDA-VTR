import cv2

IMAGE1 = "../data/test.jpg"
IMAGE2 = "../data/test.jpg"

img1 = cv2.imread(IMAGE1)
img2 = cv2.imread(IMAGE2)

orb = cv2.ORB_create(2000)

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda x: x.distance)

print(f"Total Matches: {len(matches)}")

matched_image = cv2.drawMatches(
    img1,
    kp1,
    img2,
    kp2,
    matches[:100],
    None,
    flags=2
)

cv2.imwrite(
    "../results/orb_matches.jpg",
    matched_image
)

print("Saved: ../results/orb_matches.jpg")