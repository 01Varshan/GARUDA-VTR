import cv2
import os
import pickle

class RouteDatabase:

    def __init__(self):
        self.keyframes = []

    def add_keyframe(self, frame_id, descriptors):
        self.keyframes.append({
            "frame_id": frame_id,
            "descriptors": descriptors
        })

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.keyframes, f)

    def load(self, filename):
        with open(filename, "rb") as f:
            self.keyframes = pickle.load(f)