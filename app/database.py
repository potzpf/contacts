from jsonschema import validate
from .contact_schema import schema

# add one contact to the database
def addContact(json):
    try:
        validate(instance=json, schema=schema)
    except:
        raise ValueError
