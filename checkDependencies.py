def checkDependencies():
    try:
        import SimPEG
    except Exception, e:
        import pip
        pip.main(['install',SimPEG])
    else:
        pass