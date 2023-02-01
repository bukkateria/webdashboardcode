import pyrebase

# firebaseConfig = {
#     "apiKey": "AIzaSyBWngtLdOlKlGzeUjuut5IbGJnuGCW6vsw",
#     "authDomain": "pyrebase-887c5.firebaseapp.com",
#     "projectId": "pyrebase-887c5",
#     "databaseURL": "https://pyrebase-887c5-default-rtdb.firebaseio.com",
#     "storageBucket": "pyrebase-887c5.appspot.com",
#     "messagingSenderId": "681113141632",
#     "appId": "1:681113141632:web:20b86cf363956b500d4165"
# }


firebaseConfig = {
    "apiKey": "AIzaSyDmfS634Axd2TDwDaa9leJgFub6v_wtFlI",
    "authDomain": "bukkateria-app-be22a.firebaseapp.com",
    "projectId": "bukkateria-app-be22a",
    "databaseURL": "https://bukkateria-app-be22a.firebaseio.com",
    "storageBucket": "bukkateria-app-be22a.appspot.com",
    "messagingSenderId": "294359979569",
    "appId": "1:294359979569:web:433e3b73e65b2373f7e710",
    "measurementId": "G-RBXBSH1Z5C"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()
