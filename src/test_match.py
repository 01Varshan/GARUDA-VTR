import cv2

from localize import find_best_match

image = cv2.imread("../data/test.jpg")

frame, score = find_best_match(image)

print("Matched Route Frame:", frame)
print("Score:", score)