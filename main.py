import os
from os import listdir
from os.path import isfile, join
import firebase_admin
from firebase_admin import credentials, firestore
import subprocess


def bash_command(cmd):
    sp = subprocess.Popen(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE)
    return sp.stdout.readlines()


def get_program_list():
    test = str(bash_command("customizer-install --commands")).split()
    test.pop(0)
    test[-1] = test[-1][:-4]

    trimmed = []
    for i in range(len(test)):
        if len(test[i]) > 0:
            if test[i][0] != "-" or (test[i][0] != "-" and test[i][1] != "-"):
                trimmed.append(test[i])
    return trimmed


def sew_url(collection):
    return "https://raw.githubusercontent.com/Axlfc/icons/master/ico_images/ico_pool/" + collection + "_icon.ico"


# PROGRAMS
def set_new_collection(collection, program):
    print(program)
    collection.set(program)


def get_db_pointer():
    cred = credentials.Certificate("./ServiceAccountKey.json")
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    transaction = db.transaction()
    return db


programs = {}
for i in get_program_list():
    programs[i] = {"logo": sew_url(i), "nameDisplay": i, "tag": "develop", "system": 2, "nameLinux": i, "nameWindows": i}
#print(programs)

db = get_db_pointer()
for program in programs.values():
    doc_ref = db.collection("Applications").document()
    set_new_collection(doc_ref, program)
