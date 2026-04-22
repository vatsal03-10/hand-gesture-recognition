# 🖐️ Hand Gesture Recognition using MediaPipe

## 📌 Overview

This project implements a **real-time hand gesture recognition system** using computer vision. It detects hand landmarks via webcam and classifies gestures such as 👍 Thumbs Up, ✌️ Peace, and ✋ Open Hand.

---

## 🚀 Features

* 🔍 Real-time hand detection using MediaPipe
* ✋ 21-point hand landmark tracking
* 🧠 Gesture classification (custom logic)
* 🎥 Live webcam processing
* ⚡ Fast and lightweight system

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

---

## 📂 Project Structure

```
HandGestureRecognition/
 ├── gesture_recognition.py   # Main file (camera + detection)
 ├── gestures.py              # Gesture logic (finger states + classification)
 ├── hand_landmarker.task     # Pre-trained model
 ├── .gitignore
 └── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/hand-gesture-recognition.git
cd hand-gesture-recognition
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python mediapipe numpy
```

---

## ▶️ Usage

Run the project:

```bash
python gesture_recognition.py
```

👉 Press **Q** to exit

---

## ✋ Supported Gestures

| Gesture      | Description           |
| ------------ | --------------------- |
| 👍 Thumbs Up | Only thumb raised     |
| ✌️ Peace     | Index + middle finger |
| ✋ Open Hand  | All fingers up        |

---

## 🧠 How It Works

1. Webcam captures video frames
2. MediaPipe detects hand landmarks
3. Landmarks converted into finger states
4. Custom logic classifies gesture
5. Gesture displayed on screen

---

## 📸 Demo (Add Screenshot Here)

👉 Add your screenshot like:

```
![Demo](test.png)
```

---

## 🔮 Future Improvements

* 🖱️ Virtual mouse control
* 🔊 Volume control using gestures
* 🤖 Custom gesture training using ML
* 🎮 Game control integration

---

## 👨‍💻 Author

**Vatsal Patil**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
