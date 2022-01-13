import os
from os import listdir
from os.path import isfile, join
import firebase_admin
from firebase_admin import credentials, firestore


def sew_url(collection):
    prefix = "https://raw.githubusercontent.com/Axlfc/icons/master/ico_images/ico_pool/"
    url_list = []
    for i in collection:
        url_list.append(prefix + i)
    return url_list


def set_new_collection(collection, logo_url, name, tag, win, lin):
    collection.set({
        'logo': logo_url,
        'nameDisplay': name,
        'tag': tag,
        'nameWindows': win,
        'nameLinux': lin
    })

cred = credentials.Certificate("./ServiceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
transaction = db.transaction()


whatsapp = db.collection(u'Applications').document(u'MmxAhLkWmDtlze4qs4qI')
#print(whatsapp)

onlyfiles = [f for f in listdir("/home/axel/Escritorio/git/icons/ico_images/ico_pool") if isfile(join("/home/axel/Escritorio/git/icons/ico_images/ico_pool", f))]
#print(onlyfiles)
'''
for i in sew_url(onlyfiles):
    print(i)
'''

# from firebase_admin import auth
# email = input("Enter email address")
# password = input("Enter password")

# user = auth.create_user(email = email, password = password)

# print("user created")


## CUSTOMIZER

import subprocess


def bash_command(cmd):
    sp = subprocess.Popen(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE)
    return sp.stdout.readlines()


test = str(bash_command("customizer-install --commands")).split()
test.pop(0)
test[-1] = test[-1][:-4]

trimmed = []
for i in range(len(test)):
    if len(test[i]) > 0:
        if test[i][0] != "-" or (test[i][0] != "-" and test[i][1] != "-"):
            trimmed.append(test[i])

tag = "develop"
nameWindows = "prueba"
nameLinux = "prova"

imagelist = []
#print(onlyfiles)

for i in sew_url(trimmed):
    imagelist.append(i + "_icon.ico")

print(imagelist)
doc_ref = db.collection("Applications").document()

#set_new_collection(doc_ref, logo, trimmed[i], tag, nameWindows, nameLinux)

