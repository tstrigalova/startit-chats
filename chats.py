from flask import json, jsonify
from datetime import datetime


LOGFAILS = "chats.txt"


def lasi():
    chata_rindas = []
    timestamp = 1545730073
    laiks = datetime.fromtimestamp(timestamp)
    with open(LOGFAILS, "r", encoding="utf-8") as f:
        for rinda in f:
            chata_rindas.append(json.loads(rinda))
    return jsonify({"chats": chata_rindas, laiks})


def pieraksti_zinju(dati):
    with open(LOGFAILS, "a", newline="", encoding="utf-8") as f:
        f.write(json.dumps(dati["chats"]) + "\n")

