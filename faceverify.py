from deepface import DeepFace

def verify_face(image1_path, image2_path):
    try:
        result = DeepFace.verify(img1_path=image1_path, img2_path=image2_path)
        return result['verified']
    except Exception as e:
        return f"Verification error: {e}"

# Example
# print(verify_face("selfie.jpg", "id_photo.jpg"))
