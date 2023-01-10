
import json 
def parseJsonFile(filePath):
    f = open(filePath, 'r')
    fileContent = f.read().replace('\n', '').replace('\r', '')
    f.close()
    return json.loads(fileContent)