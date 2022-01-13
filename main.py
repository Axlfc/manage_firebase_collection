import os
from os import listdir
from os.path import isfile, join
import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("./ServiceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)

logo = "https://raw.githubusercontent.com/Axlfc/icons/master/ico_images/user/Function_a/formula-fx.ico"
name = "test1"
tag = "develop"
nameWindows = "prueba"
nameLinux = "prova"

db = firestore.client()

doc_ref = db.collection("Applications").document()
'''
doc_ref.set({
    'logo': logo,
    'nameDisplay': name,
    'tag': tag,
    'nameWindows': nameWindows,
    'nameLinux': nameLinux
})
'''
transaction = db.transaction()
whatsapp = db.collection(u'Applications').document(u'MmxAhLkWmDtlze4qs4qI')
#print(whatsapp)

onlyfiles = [f for f in listdir("/home/axel/Escritorio/git/icons/ico_images/ico_pool") if isfile(join("/home/axel/Escritorio/git/icons/ico_images/ico_pool", f))]
print(onlyfiles[:3])


# from firebase_admin import auth
# email = input("Enter email address")
# password = input("Enter password")

# user = auth.create_user(email = email, password = password)

# print("user created")
