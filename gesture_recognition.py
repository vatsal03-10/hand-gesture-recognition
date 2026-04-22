import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import urllib.request, os
from gestures import get_finger_states, classify_gesture

model_path = "/Users/vatsalpatil/Downloads/miniskill image/hand_landmarker.task"
if not os.path.exists(model_path):
    print("Downloading hand landmark model (~10MB)...")
    urllib.request.urlretrieve(
        "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task",
        model_path
    )
    print("Download complete!")

options = vision.HandLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=model_path),
    running_mode=vision.RunningMode.IMAGE,
    num_hands=2,
    min_hand_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)
print("✅ Camera opened! Press Q to quit")

with vision.HandLandmarker.create_from_options(options) as landmarker:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        result = landmarker.detect(mp_image)

        if result.hand_landmarks:
            for hand in result.hand_landmarks:
                h, w, _ = frame.shape
                points = [(int(lm.x * w), int(lm.y * h)) for lm in hand]
                for (cx, cy) in points:
                    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
                fingers = get_finger_states(hand)
                gesture = classify_gesture(fingers)
                cv2.putText(frame, gesture, (max(0, points[0][0]-60), max(30, points[0][1]-20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)

        cv2.imshow("Hand Gesture Recognition - Press Q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
