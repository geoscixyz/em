def checkDependencies():
    try:
        import numpy, scipy, matplotlib, sphinxcontrib.bibtex
        pass
    except Exception, e:
        raise Exception('Requirements not installed, run: "pip install -r requirements.txt" to install requirements')
    else:
        pass

if __name__ == '__main__':
    checkDependencies()