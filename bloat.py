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


def get_bloat_program_list():
    return ["Microsoft.ZuneMusic", "Microsoft.Music.Preview", "Microsoft.XboxGameCallableUI", "Microsoft.XboxIdentityProvider", "Microsoft.BingTravel", "Microsoft.BingHealthAndFitness", "Microsoft.BingFoodAndDrink", "Microsoft.People", "Microsoft.BingFinance", "Microsoft.3DBuilder", "Microsoft.WindowsCalculator", "Microsoft.BingNews", "Microsoft.XboxApp", "Microsoft.BingSports", "Microsoft.WindowsCamera", "Microsoft.Getstarted", "Microsoft.Office.OneNote", "Microsoft.WindowsMaps", "Microsoft.MicrosoftSolitaireCollection", "Microsoft.MicrosoftOffi1ceHub", "Microsoft.BingWeather", "Microsoft.BioEnrollment", "Microsoft.WindowsStore", "Microsoft.Windows.Photos", "Microsoft.WindowsPhone"]


def sew_url(collection):
    return "https://firebasestorage.googleapis.com/v0/b/scriptsstudio-axlfcxrppy.appspot.com/o/Bloatware%2F" + collection + "?alt=media"


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
syst = ["Windows"]

for i in get_bloat_program_list():
    programs[i] = {"logo": sew_url(i), "nameDisplay": i.capitalize(),  "system": syst, "nameSystem": i}
#print(programs)

db = get_db_pointer()
for program in programs.values():
    doc_ref = db.collection("Bloatware").document()
    set_new_collection(doc_ref, program)

