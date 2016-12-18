import os
import shutil

def copyImages():
    # get relevant directories
    cwd = os.getcwd()
    contentdir = cwd+'/content'
    buildimagesdir = cwd+'/_build/html/_images'

    # check if images directory exists
    if not os.path.isdir(buildimagesdir):
        os.mkdir(buildimagesdir)

    # images that have been copied
    imnames = os.listdir(buildimagesdir)

    # search for images that have been missed
    for root, dirList, fileList in os.walk(contentdir):
        if root.endswith('images'):
            for filename in fileList:
                if filename not in imnames:
                    shutil.copy(os.path.join(root, filename),buildimagesdir)
    return


if __name__ == "__main__":
    copyImages()
