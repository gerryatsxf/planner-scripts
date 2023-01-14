
import json 

def parseJsonFile(filePath):
    f = open(filePath, 'r')
    fileContent = f.read().replace('\n', '').replace('\r', '')
    f.close()
    return json.loads(fileContent)

def test_env_not_implemented():
        raise Exception("TEST ENVIRONTMENT NOT IMPLEMENTED FOR REQUESTED OBJECT OR MODULE")