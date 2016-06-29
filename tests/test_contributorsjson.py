import subprocess
import unittest
import os
import json

PATH2JSON = '..'

class ContribsJson_Test(unittest.TestCase):

    def test_contributorsjson(self):

        print '\nTesting contributors.json validity'

        contribsjson = os.path.abspath(os.path.sep.join([PATH2JSON] + ['contributors.json']))
        contribs = open(contribsjson)

        try:
            json.load(contribs)

        except Exception as err:
            print("<<<<< FAILED: contributors.json invalid >>>>> \n Error: {0}".format(err))
            raise

        print '... ok'
        return True


if __name__ == '__main__':
    unittest.main()
