import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_verification_result(user_id, result):
    doc_ref = db.collection('users').document(user_id)
    doc_ref.set(result)

