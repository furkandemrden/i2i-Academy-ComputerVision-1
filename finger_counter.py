"""
Finger Counter Project i2i Academy Computer Vision Furkan Remzi Demirden - Intern Homework 1
"""

import cv2
import mediapipe as mp


# Setup for MediaPipe is done with these codes:
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
mpStyles = mp.solutions.drawing_styles


# The indices and the joints used for comparison
tipIds = [4, 8, 12, 16, 20]
jointIds = [3, 6, 10, 14, 18]


def countFingers(handLandmarks, handType):
    """
    It counts how many fingers are open on one hand 
    Thumb is checked using the x-axis because it moves sideways and 
    the other fingers are checked using the y-axis.
    """

    landmarks = handLandmarks.landmark
    openFingers = []

    # Check of thumb
    if handType == "Right":
        thumbOpen = landmarks[4].x < landmarks[3].x
    else:
        thumbOpen = landmarks[4].x > landmarks[3].x

    openFingers.append(thumbOpen)

    # Remaining fingers
    for tip, joint in zip(tipIds[1:], jointIds[1:]):
        openFingers.append(landmarks[tip].y < landmarks[joint].y)

    return sum(openFingers)


def main():

    camera = cv2.VideoCapture(0)
    # Puts in a message if the camera couldn't open
    if not camera.isOpened():
        print("Webcam could not be opened.")
        return

    with mpHands.Hands(
        model_complexity=0,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5,
        max_num_hands=2,
    ) as hands:

        while camera.isOpened():

            success, frame = camera.read()

            if not success:
                continue

            
            frame = cv2.flip(frame, 1)

            rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgbFrame)

            fingerCount = 0

            if result.multi_hand_landmarks and result.multi_handedness:

                for hand, handInfo in zip(
                    result.multi_hand_landmarks,
                    result.multi_handedness
                ):

                    handType = handInfo.classification[0].label

                    # Drawing the hand landmarks
                    mpDraw.draw_landmarks(
                        frame,
                        hand,
                        mpHands.HAND_CONNECTIONS,
                        mpStyles.get_default_hand_landmarks_style(),
                        mpStyles.get_default_hand_connections_style(),
                    )

                    fingerCount += countFingers(hand, handType)

            # Show the total as a text 
            cv2.putText(
                frame,
                f"Fingers: {fingerCount}",
                (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (0, 255, 0),
                3,
                cv2.LINE_AA,
            )

            cv2.imshow("Finger Counter", frame)

            if cv2.waitKey(5) & 0xFF == ord("q"):
                break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

