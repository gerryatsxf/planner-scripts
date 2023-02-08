For testing the whole app
python3 -m unittest discover -p '*test.py'

For testing a script directory
python3 -m unittest discover -s app/hello_world -p '*test.py'

Build image
docker image build -t scriptapi .

Run container
docker container run --detach --name gerry_scriptapi --publish 5001:5001 scriptapi
 
See logs
docker container logs --follow gerry_scriptapi