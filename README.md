## Description

This is the transactions API. It communicates with YNAB to update accounts' transactions. It depends on a bank-movements file being provided in order to achieve this. At the moment this API supports Santander debit and credit files only.

## Testing
Useful unit testing commands

For testing the whole app
python3 -m unittest discover -p '*test.py'

For testing a script directory
python3 -m unittest discover -s app/hello_world -p '*test.py'


## Docker
Here are some useful commands for docker development

Build image:
docker image build -t scriptapi .

Run container:
docker container run --detach --name gerry_scriptapi  --publish 5001:5000 scriptapi

See logs:
docker container logs --follow gerry_scriptapi

Delete container:
docker container rm -f gerry_scriptapi