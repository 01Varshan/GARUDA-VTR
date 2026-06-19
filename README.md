# GARUDA-VTR

Visual Teach-and-Repeat Navigation for GPS-Denied UAVs

## Overview

GARUDA-VTR is a vision-based UAV navigation framework designed for operation in GPS-denied environments.

The system learns a route during a teaching phase and autonomously repeats the same route using visual localization during the repeat phase.

## Hardware

- Cube Orange Flight Controller
- Jetson Nano Companion Computer
- SIYI A8 Mini Gimbal Camera
- RPLidar

## Current Pipeline

1. Image Acquisition
2. ORB Feature Extraction
3. Keyframe Database Creation
4. Visual Localization
5. Route Matching
6. Autonomous Route Repetition

## Future Work

- Visual-Inertial Odometry
- Confidence-Aware Localization
- Terrain-Referenced Navigation
- Satellite-to-Drone Cross-View Matching

## Author

Varshan Chaubey
Shiv Nadar University
