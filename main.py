import cv2
import torch
from transformers import ViTForImageClassification, ViTFeatureExtractor
from gtts import gTTS
import os

# Load the trained model and feature extractor
model = ViTForImageClassification.from_pretrained('./gesture_recognition_model')
feature_extractor = ViTFeatureExtractor.from_pretrained('./gesture_recognition_feature_extractor')

# Define a dictionary for the gestures
gestures = {
    0: "Hello",
    1: "Goodbye",
    2: "Yes",
    3: "No",
    4: "Please",
}

def recognize_gesture(frame):
    inputs = feature_extractor(frame, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax(-1).item()
    return gestures.get(predicted_class, "Unknown")

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("gesture.mp3")
    os.system("mpg321 gesture.mp3")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('Video', frame)
    
    gesture_text = recognize_gesture(frame)
    
    if gesture_text != "Unknown":
        print(f"Recognized Gesture: {gesture_text}")
        text_to_speech(gesture_text)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
