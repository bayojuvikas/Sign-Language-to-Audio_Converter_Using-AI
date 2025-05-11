# 🤖 Real-Time Gesture Recognition with Audio Feedback

This project demonstrates **real-time hand gesture recognition** using a fine-tuned [Vision Transformer (ViT)](https://huggingface.co/transformers/model_doc/vit.html) model, paired with **text-to-speech** audio feedback using Google's Text-to-Speech API. The application captures video from your webcam, classifies recognized gestures, and speaks them aloud.

## 🧠 Features

* 🔍 **Gesture Recognition** using a fine-tuned ViT model
* 🗣️ **Text-to-Speech Output** for recognized gestures
* 🎥 **Real-Time Webcam Integration** using OpenCV
* 🧰 Simple, portable Python implementation

## ✋ Supported Gestures

The model currently supports recognition for the following hand gestures:

| Class ID | Gesture |
| -------- | ------- |
| 0        | Hello   |
| 1        | Goodbye |
| 2        | Yes     |
| 3        | No      |
| 4        | Please  |

## 🧱 Project Structure

* `gesture_recognition_model/`: Directory containing your fine-tuned ViT model
* `gesture_recognition_feature_extractor/`: Directory for the corresponding ViT feature extractor
* `main.py`: The main Python script (code shown above)

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bayojuvikas/Sign-Language-to-Audio_Converter_Using-AI.git
   cd Sign-Language-to-Audio_Converter_Using-AI
   ```

2. Install dependencies:

   ```bash
   pip install torch torchvision transformers opencv-python gtts
   sudo apt-get install mpg321  # For playing audio (Linux)
   ```

3. Make sure your webcam is connected and working.

## 🏃‍♂️ Run the Application

```bash
python main.py
```

Press `q` to exit the webcam stream.

## 💡 How It Works

1. Captures a frame from webcam.
2. Processes it through the ViT model for gesture classification.
3. Converts the predicted gesture into speech.
4. Plays the audio file instantly.

## 📦 Requirements

* Python 3.7+
* [PyTorch](https://pytorch.org/)
* [Transformers](https://huggingface.co/transformers/)
* [OpenCV](https://opencv.org/)
* [gTTS](https://pypi.org/project/gTTS/)
* `mpg321` or any MP3 player installed (for Linux)

## 📌 Notes

* This is a prototype for basic gesture interaction. Future improvements can include more gesture classes, better frame preprocessing, or a UI overlay.
* Model and feature extractor should be saved locally as Hugging Face-compatible directories.

## 📄 License

This project is licensed under the MIT License.
