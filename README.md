# i2i-Academy-ComputerVision-1

This repository contains a real-time computer vision application developed as part of the i2i Academy training program. The application captures live video from a webcam, detects human hands, and accurately counts the number of fingers held up in real time.

## Project Scope & Objective
The primary objective of this project is to implement fundamental Computer Vision (CV) concepts and algorithmic logic by tracking hand landmarks without relying on from-scratch heavy deep learning models. 

## Key Features
*   **Live Video Processing:** Captures and processes the webcam feed frame by frame using OpenCV.
*   **Hand Tracking:** Utilizes a pre-trained computer vision framework (MediaPipe) to efficiently extract hand landmarks and coordinate joints.
*   **Finger Counting Logic:** Implements a custom conditional algorithm to determine whether each finger is "open" or "closed" based on landmark coordinates.
*   **Real-Time Overlay:** Displays the live finger count dynamically as text on the video window.

## Built With
*   Python 3
*   OpenCV (cv2)
*   MediaPipe

## Developer
*   **Furkan Demirden** - [@furkandemrdn](https://github.com/furkandemrdn)

---
*Note: Homework instructions, documentation templates, and personal evaluation materials are excluded from this repository in compliance with the portfolio building standards of i2i Academy.*