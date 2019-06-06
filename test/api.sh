# basic tests of the REST interface

curl -d '{"name": "Lemmy Kilmister"}' -H "Content-Type: application/json" localhost:5000/contacts
echo
curl -d '{"name": 123}' -H "Content-Type: application/json" localhost:5000/contacts
echo


