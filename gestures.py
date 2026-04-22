def get_finger_states(landmarks):
    """Returns list of [thumb, index, middle, ring, pinky] — 1=up, 0=down"""
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb (compare x-axis, not y)
    if landmarks[tips[0]].x < landmarks[tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other 4 fingers (compare y-axis — lower y = higher on screen)
    for i in range(1, 5):
        if landmarks[tips[i]].y < landmarks[tips[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


def classify_gesture(fingers):
    """Map finger states to gesture name"""
    gestures = {
        (0, 0, 0, 0, 0): "✊ Fist",
        (1, 1, 1, 1, 1): "🖐 Open Hand",
        (0, 1, 0, 0, 0): "☝️ Pointing",
        (0, 1, 1, 0, 0): "✌️ Peace",
        (1, 0, 0, 0, 1): "🤙 Call Me",
        (1, 1, 0, 0, 0): "👌 L-Shape",
        (0, 0, 0, 0, 1): "🤙 Pinky",
        (1, 0, 0, 0, 0): "👍 Thumbs Up",
        (0, 1, 1, 1, 1): "Four Fingers",
    }
    return gestures.get(tuple(fingers), "🤔 Unknown")