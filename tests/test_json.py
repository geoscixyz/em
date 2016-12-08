import subprocess
import unittest
import os
import json

# relative to em/
jsonFiles = ['contributors.json', 'content/case_histories/case_histories.json']

def getFile(jsonFile):
    dirname, filename = os.path.split(os.path.abspath(__file__))
    path2root = dirname.split(os.path.sep)[:-1]

    if '/' in jsonFile:
        path2json = jsonFile.split(os.path.sep)
    else:
        path2json = [jsonFile]

    name = path2json[-1].split('.')[0]
    jsonfile = os.path.abspath(os.path.sep.join(path2root + path2json))

    return name, jsonfile

def get(name, jsonFile):
    def test_func(self):
        print('\nTesting {0!s} Validity \n'.format(name))

        openJson = open(jsonFile)

        try:
            json.load(openJson)
        except Exception as err:
            print(
                "<<<<< FAILED: {0!s}.json invalid >>>>> \n Error: {1}".format(
                    name, err))
            raise err

        print('... ok')
        return True

    return test_func

attrs = dict()

for test in jsonFiles:
    name, jsonfile = getFile(test)
    attrs['test_'+name] = get(name, jsonfile)

TestJson = type('TestJSON', (unittest.TestCase,), attrs)

if __name__ == '__main__':
    unittest.main()
