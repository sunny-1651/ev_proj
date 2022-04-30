
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("/home/hemant/ev_proj/ev/ev-proj-c383e-firebase-adminsdk-cwgjk-208f6f4516.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://ev-proj-c383e-default-rtdb.asia-southeast1.firebasedatabase.app/'})

ref = db.reference("/")


def dbvalue(x):
    ref.set({"dir": x})