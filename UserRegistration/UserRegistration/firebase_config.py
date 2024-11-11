import firebase_admin,os
from firebase_admin import credentials
from firebase_admin import db , firestore
import json

# Initialize Firebase Admin SDK
firebase_config = json.loads(os.getenv('FIREBASE_CONFIG', '{}'))
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://comiconuserentry-a72ba-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Replace with your Firebase Realtime Database URL
})