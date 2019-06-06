from flask import Flask, redirect, url_for, request, abort
from app.database import addContact
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect(url_for('static', filename="contacts.html"))

# Returns a list of all contacts with basic information
@app.route("/contacts", methods=["GET"])
def getContacts():
    return "contacts"

# Adds a new contact
@app.route("/contacts", methods=["POST"])
def postContact():
    try:
        addContact(request.json)
    except ValueError:
        abort(400)
    except Exception as e:
        app.logger.warn("Unknown Exception")
        abort(500)

    return "OK"

# Returns full information on a given contact
@app.route("/contact/<id>", methods=["GET"])
def getContact(id):
    return "contact"

# Updates contact information
@app.route("/contact/<id>", methods=["UPDATE"])
def putContact(id):
    return "contact updated"

# Deletes contact
@app.route("/contact/<id>", methods=["DELETE"])
def deleteContact(id):
    return "contact deleted"
