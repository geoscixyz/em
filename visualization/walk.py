import os
import json

BASE_PATH = '/Users/rowan/git/ubcgif/em/'
APP_TITLE = 'Electromagnetics'

# This is what we will populate below
directory_tree = dict(name=APP_TITLE)


def parse_file(path, name):

    if not name.endswith('.rst'):
        name += '.rst'

    title = None
    underconstruction = False
    children = []

    with open(path+os.path.sep + name, 'r') as f:
        previous_line = None
        for line in f:
            # skip over comment lines
            if line.strip().startswith('..') and ':' not in line:
                continue
            if (
                '***' in line or
                '===' in line or
                '---' in line
            ):
                if title is None:
                    title = previous_line.strip()
                else:
                    children += [dict(
                        name=previous_line.strip()
                    )]
            if 'underconstruction.html' in line:
                underconstruction = True
            previous_line = line

    data = dict(
        name=title,
        link=name,
        underconstruction=underconstruction,
        children=children
    )
    return data


def put_child(path, subtree):
    if not subtree:
        return
    spath = path[len(BASE_PATH):].split(os.path.sep)
    # if len(path) == 1:
    print spath
    directory_tree


# for path, dirs, files in os.walk(BASE_PATH):
#     subtree = []
#     for f in files:
#         # print path, f
#         parse_file(subtree, path, f)
#     put_child(path, subtree)

def get_toc_tree(path):

    if not path.endswith('.rst'):
        path += '.rst'

    if not os.path.isfile(path):
        raise Exception('no file found: ' + path)
    toc_tree_started = False
    toc_tree = []

    with open(path, 'r') as f:
        for line in f:
            if ':maxdepth:' in line:
                continue
            if len(line.strip()) == 0:
                continue
            if '.. toctree::' in line:
                toc_tree_started = True
                continue
            if not toc_tree_started:
                continue
            # we are in a toc tree block
            if not line.startswith(' '*4):
                break
            toc_tree += [line.strip()]
    return toc_tree


site = get_toc_tree(BASE_PATH + 'sitemap.rst')

ii = 0
tree = []


def recurse(entry):
    folder = os.path.sep.join(entry.split(os.path.sep)[:-1]) + os.path.sep
    index = entry.split(os.path.sep)[-1]
    print folder, index
    data = parse_file(BASE_PATH + folder, index)
    sub_toc_tree = get_toc_tree(BASE_PATH + folder + index)
    print sub_toc_tree
    children = [recurse(folder + e) for e in sub_toc_tree]
    data['children'] += children
    if len(data['children']) == 0:
        del data['children']
    return data


data = dict(name=APP_TITLE, children=[recurse(e) for e in site])
print json.dumps(data, sort_keys=True, indent=4)

with open('/Users/rowan/Desktop/toctree.json', 'w') as f:
    f.write(json.dumps(data, sort_keys=True, indent=4))
