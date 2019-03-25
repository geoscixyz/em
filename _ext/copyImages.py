import os
import shutil

def copyImages():
    # get relevant directories
    cwd = os.getcwd()
    contentdir = os.path.sep.join(cwd.split(os.path.sep) + ['content'])
    buildimagesdir = os.path.sep.join(cwd.split(os.path.sep) + ['_build','html','_images'])

    # check if images directory exists
    if not os.path.isdir(buildimagesdir):
        # check if html directory exists
        split_path = buildimagesdir.split(os.path.sep)
        build_dir = os.path.sep.join(split_path[:-2])
        html_dir = os.path.sep.join(split_path[:-1])
        if not os.path.isdir(build_dir):
            os.mkdir(build_dir)
        if not os.path.isdir(html_dir):
            os.mkdir(html_dir)
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
