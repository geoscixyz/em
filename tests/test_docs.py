import subprocess
import unittest
import os

class Doc_Test(unittest.TestCase):

    @property
    def path_to_docs(self):
        dirname, filename = os.path.split(os.path.abspath(__file__))
        return os.path.sep.join(dirname.split(os.path.sep)[:-1])

    def test_html(self):
        doctrees_path = os.path.sep.join(self.path_to_docs.split(os.path.sep) + ['_build']+['doctrees'])
        html_path = os.path.sep.join(self.path_to_docs.split(os.path.sep) + ['_build']+['html'])

        check = subprocess.call(["sphinx-build", "-nW", "-b", "html", "-d",
            "%s"%(doctrees_path) ,
            "%s"%(self.path_to_docs),
            "%s"%(html_path)])
        assert check == 0


        def test_images(self):
            images_path = os.path.sep.join(self.path_to_docs.split(os.path.sep) + ['_build']+['html']+['_images'])
            for img in os.listdir(images_path):
                assert img[-3:] in ['png', 'jpg', 'gif'], 'Figure file extension must be png, jpg, gif, not %s'%img


    def test_latex(self):
        doctrees_path = os.path.sep.join(self.path_to_docs.split(os.path.sep) + ['_build']+['doctrees'])
        latex_path = os.path.sep.join(self.path_to_docs.split(os.path.sep) + ['_build']+['latex'])

        check = subprocess.call(["sphinx-build", "-nW", "-b", "latex", "-d",
            "%s"%(doctrees_path),
            "%s"%(self.path_to_docs),
            "%s"%(latex_path)])
        assert check == 0

    def test_linkcheck(self):
        doctrees_path = os.path.sep.join(self.path_to_docs.split(os.path.sep) + ['_build']+['doctrees'])
        link_path = os.path.sep.join(self.path_to_docs.split(os.path.sep) + ['_build'])

        check = subprocess.call(["sphinx-build", "-nW", "-b", "linkcheck", "-d",
            "%s"%(doctrees_path),
            "%s"%(self.path_to_docs),
            "%s"%(link_path)])
        assert check == 0


if __name__ == '__main__':
    unittest.main()
