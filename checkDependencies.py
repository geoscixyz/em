def checkDependencies():
    try:
        import SimPEG
        pass
    except Exception, e:
        raise Exception('Requirements not installed, run: "pip install -r requirements.txt"')
    else:
        pass

if __name__ == '__main__':
    checkDependencies()