# basic tests of the REST interface

# POST contact
curl -d '{"name": "Lemmy Kilmister"}' -H "Content-Type: application/json" localhost:5000/contacts
echo
curl -d '{"name": 123}' -H "Content-Type: application/json" localhost:5000/contacts
echo

# GET Contact list
curl localhost:5000/contacts

# GET Contact
curl localhost:5000/contact/0


