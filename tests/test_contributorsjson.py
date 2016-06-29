import subprocess
import unittest
import os
import json


class ContribsJson_Test(unittest.TestCase):

    def test_contributorsjson(self):

        print '\nTesting contributors.json validity'

        dirname, filename = os.path.split(os.path.abspath(__file__))
        path2json = os.path.sep.join(dirname.split(os.path.sep)[:-1])

        contribsjson = os.path.abspath(os.path.sep.join([path2json] + ['contributors.json']))
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
