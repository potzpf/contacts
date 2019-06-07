import json
from jsonschema import validate
from .contact_schema import contact_schema

class DbHandler:
    store = [] #an array of objects that confirm the contact schema

    # constructor
    def __init__(self, path):
        with open(path) as file:
            #TODO: validate against schema
            store = json.load(file)

    # add one contact to the database
    def addContact(self, data):
        try:
            validate(instance=data, schema=contact_schema)
        except:
            raise

        self.store.append(data)

    # return indicies and name
    def getContactList(self):
        ret = []

        for i in range(len(self.store)):
            ret.append({"id": i, "name": self.store[i]["name"]})

        return ret

    def getContact(self, id):
        if id < 0 or id >= len(self.store):
            raise ValueError

        return self.store[id]
