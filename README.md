# AI-Biometric-Verification-System 🔒

An AI-powered biometric verification system to ensure only verified, consenting adults can upload sensitive content, protecting users and platforms from misuse.

---

## 🚀 Core Features

✅ **Face Recognition**  
Ensures the uploader matches the ID using DeepFace.

✅ **Liveness Detection**  
Checks for spoof attempts using real-time blinking/movement detection.

✅ **ID Verification**  
Extracts and validates ID details using OCR (Tesseract).

✅ **Firebase Integration**  
Stores user verification data for future validation and audits.

✅ **Consent-Based Uploading**  
Only successful biometric matches allow content to be uploaded, ensuring legal and ethical use.

---

## 🛠️ Tech Stack

| Layer       | Technologies                          |
|-------------|----------------------------------------|
| AI/ML       | DeepFace, OpenCV, Pytesseract          |
| Backend     | Python (Flask), Firebase Admin SDK     |
| Database    | Firestore (NoSQL)                      |
| Others      | Tesseract OCR, Webcam Access, GitHub   |

---

## 📂 Project Structure


---

## 🎯 Real-World Impact

- 🔐 Prevents deepfakes, revenge porn, & non-consensual uploads.
- 🧠 Enforces digital consent for adult platforms.
- 📜 Supports legal compliance & data logging.

---

## ✅ How to Run

1. Clone the repo
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Add your Firebase Admin SDK in the same folder.
4. Run each module step by step:
    - `face_verify.py`
    - `liveness_check.py`
    - `id_match.py`

---

## 📸 Demo Preview

*(You can upload a short screen recording or sample screenshots here)*

---

## 🧠 Future Improvements

- Add more advanced liveness detection with ML
- Integrate front-end portal for user interaction
- Auto content moderation after upload

---

> Built with responsibility, privacy, and consent at its core.


