import firebase_admin,os
from firebase_admin import credentials
from firebase_admin import db , firestore
import json

# Get the firebase config string from environment variables
firebase_json_str = os.getenv("FIREBASE_CONFIG")

# Convert the string to a JSON object
firebase_config = json.loads(firebase_json_str)

cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://comiconuserentry-a72ba-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Replace with your Firebase Realtime Database URL
})