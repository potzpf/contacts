from flask import Flask, render_template, request, abort, jsonify
from app.database import DbHandler
from app.routes import *

app = Flask(__name__)
db = DbHandler("data/store.json")

@app.route("/")
def hello():
    return render_template("contacts.html")

# Returns a list of all contacts with basic information
@app.route("/contacts", methods=["GET"])
def getContacts():
    try:
        list = db.getContactList()
    except Exception as e:
        app.logger.warn(f"Unknown Exception: {e}")
        abort(500)

    return jsonify(list)


# Adds a new contact
@app.route("/contacts", methods=["POST"])
def postContact():
    try:
        db.addContact(request.json)
    except ValueError:
        abort(400)
    except Exception as e:
        app.logger.warn(f"Unknown Exception: {e}")
        abort(500)

    return "OK"

# Returns full information on a given contact
@app.route("/contact/<int:id>", methods=["GET"])
def getContact(id):
    try:
        contact = db.getContact(id)
    except ValueError:
        abort(400)
    except Exception as e:
        app.logger.warn(f"Unknown Exception: {e}")
        abort(500)

    return jsonify(contact)

# Updates contact information
@app.route("/contact/<id>", methods=["UPDATE"])
def putContact(id):
    return "contact updated"

# Deletes contact
@app.route("/contact/<id>", methods=["DELETE"])
def deleteContact(id):
    return "contact deleted"
