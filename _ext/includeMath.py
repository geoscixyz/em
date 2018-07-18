
"""
    Adapted from sphinx.ext.purpose

    https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/purpose.py

    Allow purposes to be inserted into your documentation.  Inclusion of purposes can
    be switched of by a configuration variable.  The purposelist directive collects
    all purposes of your project and lists them along with a backlink to the
    original location.
    :copyright: Copyright 2007-2016 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes
from docutils.parsers.rst import directives

import sphinx
# from sphinx.locale import _
# from sphinx.environment import NoUri
# from sphinx.util.nodes import set_source_info
# from docutils.parsers.rst import Directive
# from docutils.parsers.rst.directives.admonitions import BaseAdmonition

from docutils.parsers.rst.directives.misc import Include

from sphinx.ext.mathbase import setup_math

class IncludeMath(setup_math):
    """
    Includes equations and allows them to be labeled
    """

    def run(self):
        # type: () -> List[nodes.Node]
        print(self.options)
        env = self.state.document.settings.env
        # if self.arguments[0].startswith('<') and \
        #    self.arguments[0].endswith('>'):
        #     # docutils "standard" includes, do not do path processing
        #     return Include.run(self)
        rel_filename, filename = env.relfn2path(self.arguments[0])
        self.arguments[0] = filename
        print(dir(env))
        env.note_included(filename)
        nodes = Include.run(self)
        print(dir(nodes))
        return nodes


def setup(app):
    directives.register_directive('includemath', IncludeMath)
