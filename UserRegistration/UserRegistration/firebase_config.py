import firebase_admin,os
from firebase_admin import credentials
from firebase_admin import db , firestore

# Initialize Firebase Admin SDK
path = r"Q:\pipelines\zas_tools\workspaces\rishabh.g\firebase\firebase.json"
print(path)
cred = credentials.Certificate(path) # Path to your Firebase Admin SDK JSON file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://comiconuserentry-a72ba-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Replace with your Firebase Realtime Database URL
})