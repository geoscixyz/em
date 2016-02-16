import shutil, os


def make_formula_sheet():

    # Create the examples dir in the docs folder.
    fName = os.path.realpath(__file__)
    EquationSheetDir = os.path.sep.join(fName.split(os.path.sep)[:-1] + ['content', 'equation_bank'])

    files = os.listdir(EquationSheetDir)

    rst = os.path.sep.join((fName.split(os.path.sep)[:-1] + ['content', 'equation_bank' + '.rst']))

    out = """.. _equation_bank:

.. --------------------------------- ..
..                                   ..
..    THIS FILE IS AUTO GENEREATED   ..
..                                   ..
..    autodoc.py                     ..
..                                   ..
.. --------------------------------- ..


Equation Bank
=============

"""

    print 'Creating: equation_bank.rst'
    f = open(rst, 'w')
    f.write(out)

    for name in files:
        out = """

 - %s

    .. include:: equation_bank/%s

        """%(name.rstrip('.rst'),name)
        f.write(out)

    f.close()


if __name__ == '__main__':
    """
        Run the following to create the formula sheet.
    """

    make_formula_sheet() 