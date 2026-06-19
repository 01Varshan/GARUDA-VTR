import cv2

from route_database import RouteDatabase

DB_FILE = "../route_database/route.pkl"

orb = cv2.ORB_create(2000)

db = RouteDatabase()
db.load(DB_FILE)

bf = cv2.BFMatcher(cv2.NORM_HAMMING)

def find_best_match(image):

    kp, des = orb.detectAndCompute(image, None)

    best_score = 0
    best_frame = -1

    for frame in db.keyframes:

        matches = bf.match(des, frame["descriptors"])

        score = len(matches)

        if score > best_score:
            best_score = score
            best_frame = frame["frame_id"]

    return best_frame, best_score