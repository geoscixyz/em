import os
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.images import Figure


class simpegFig(Figure):

    def run(self):
	# Assume all names are in HTML raw: format:
	if self.arguments[0].startswith('.. raw:: html') :
            relFileBase = self.arguments[0][1:]
        else:
	    relFileBase = '.. raw:: html ' + self.arguments[0]

        self.arguments[0] = '.. raw:: html ' + self.arguments[0]

        return Figure.run(self)


def setup(app):
    app.add_directive('simpegFig', simpegFig)
    app.add_node(simpegFig)

    return {'version': '0.1'}

