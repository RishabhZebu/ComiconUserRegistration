import firebase_admin,os
from firebase_admin import credentials
from firebase_admin import db , firestore
import json
import base64

# Initialize Firebase Admin SDK
# Get the base64 encoded Firebase config from environment variable
firebase_config_base64 = os.getenv('FIREBASE_CONFIG')

# Decode the base64 string into the original JSON configuration
firebase_config_json = base64.b64decode(firebase_config_base64).decode('utf-8')

# Parse the JSON
firebase_config = json.loads(firebase_config_json)

cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://comiconuserentry-a72ba-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Replace with your Firebase Realtime Database URL
})