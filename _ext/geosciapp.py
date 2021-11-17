
"""
    Adapted from sphinx.ext.geosciapp

    https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/geosciapp.py

    Allow geosciapps to be inserted into your documentation.  Inclusion of geosciapps can
    be switched of by a configuration variable.  The geosciapplist directive collects
    all geosciapps of your project and lists them along with a backlink to the
    original location.
    :copyright: Copyright 2007-2016 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes
from docutils.parsers.rst import directives

import sphinx
from sphinx.locale import _
from sphinx.errors import NoUri
from sphinx.util.nodes import set_source_info
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition


class geosciapp_node(nodes.Admonition, nodes.Element):
    pass


class geosciapplist(nodes.General, nodes.Element):
    pass


class Geosciapp(BaseAdmonition):
    """
    A geosciapp entry, displayed (if configured) in the form of an admonition.
    """

    node_class = geosciapp_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }

    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-geosciapp']

        (geosciapp,) = super(Geosciapp, self).run()
        if isinstance(geosciapp, nodes.system_message):
            return [geosciapp]

        geosciapp.insert(0, nodes.title(text=_('GeoSci App')))
        set_source_info(self, geosciapp)

        env = self.state.document.settings.env
        targetid = 'geosciapp'
        targetnode = nodes.target('', '', ids=[targetid])
        return [targetnode, geosciapp]


def process_geosciapps(app, doctree):
    # collect all geosciapps in the environment
    # this is not done in the directive itself because it some transformations
    # must have already been run, e.g. substitutions
    env = app.builder.env
    if not hasattr(env, 'geosciapp_all_geosciapps'):
        env.geosciapp_all_geosciapps = []
    for node in doctree.traverse(geosciapp_node):
        app.emit('geosciapp-defined', node)

        try:
            targetnode = node.parent[node.parent.index(node) - 1]
            if not isinstance(targetnode, nodes.target):
                raise IndexError
        except IndexError:
            targetnode = None
        newnode = node.deepcopy()
        del newnode['ids']
        env.geosciapp_all_geosciapps.append({
            'docname': env.docname,
            'source': node.source or env.doc2path(env.docname),
            'lineno': node.line,
            'geosciapp': newnode,
            'target': targetnode,
        })



class GeosciappList(Directive):
    """
    A list of all geosciapp entries.
    """

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        # Simply insert an empty geosciapplist node which will be replaced later
        # when process_geosciapp_nodes is called
        return [geosciapplist('')]


def process_geosciapp_nodes(app, doctree, fromdocname):
    if not app.config['geosciapp_include_geosciapps']:
        for node in doctree.traverse(geosciapp_node):
            node.parent.remove(node)

    # Replace all geosciapplist nodes with a list of the collected geosciapps.
    # Augment each geosciapp with a backlink to the original location.
    env = app.builder.env

    if not hasattr(env, 'geosciapp_all_geosciapps'):
        env.geosciapp_all_geosciapps = []

    for node in doctree.traverse(geosciapplist):
        if not app.config['geosciapp_include_geosciapps']:
            node.replace_self([])
            continue

        content = []

        for geosciapp_info in env.geosciapp_all_geosciapps:
            para = nodes.paragraph(classes=['geosciapp-source'])
            if app.config['geosciapp_link_only']:
                description = _('<<original entry>>')
            else:
                description = (
                    _('(The <<original entry>> is located in %s, line %d.)') %
                    (geosciapp_info['source'], geosciapp_info['lineno'])
                )
            desc1 = description[:description.find('<<')]
            desc2 = description[description.find('>>')+2:]
            para += nodes.Text(desc1, desc1)

            # Create a reference
            newnode = nodes.reference('', '', internal=True)
            innernode = nodes.emphasis(_('original entry'), _('original entry'))
            try:
                newnode['refuri'] = app.builder.get_relative_uri(
                    fromdocname, geosciapp_info['docname'])
                newnode['refuri'] += '#' + geosciapp_info['target']['refid']
            except NoUri:
                # ignore if no URI can be determined, e.g. for LaTeX output
                pass
            newnode.append(innernode)
            para += newnode
            para += nodes.Text(desc2, desc2)

            # (Recursively) resolve references in the geosciapp content
            geosciapp_entry = geosciapp_info['geosciapp']
            env.resolve_references(geosciapp_entry, geosciapp_info['docname'],
                                   app.builder)

            # Insert into the geosciapplist
            content.append(geosciapp_entry)
            content.append(para)

        node.replace_self(content)


def purge_geosciapps(app, env, docname):
    if not hasattr(env, 'geosciapp_all_geosciapps'):
        return
    env.geosciapp_all_geosciapps = [geosciapp for geosciapp in env.geosciapp_all_geosciapps
                                if geosciapp['docname'] != docname]


def merge_info(app, env, docnames, other):
    if not hasattr(other, 'geosciapp_all_geosciapps'):
        return
    if not hasattr(env, 'geosciapp_all_geosciapps'):
        env.geosciapp_all_geosciapps = []
    env.geosciapp_all_geosciapps.extend(other.geosciapp_all_geosciapps)


def visit_geosciapp_node(self, node):
    self.visit_admonition(node)
    # self.visit_admonition(node, 'geosciapp')


def depart_geosciapp_node(self, node):
    self.depart_admonition(node)


def setup(app):
    app.add_event('geosciapp-defined')
    app.add_config_value('geosciapp_include_geosciapps', True, 'html')
    app.add_config_value('geosciapp_link_only', False, 'html')
    app.add_config_value('geosciapp_emit_warnings', False, 'html')

    app.add_node(geosciapplist)
    app.add_node(geosciapp_node,
                 html=(visit_geosciapp_node, depart_geosciapp_node),
                 latex=(visit_geosciapp_node, depart_geosciapp_node),
                 text=(visit_geosciapp_node, depart_geosciapp_node),
                 man=(visit_geosciapp_node, depart_geosciapp_node),
                 texinfo=(visit_geosciapp_node, depart_geosciapp_node))

    app.add_directive('geosciapp', Geosciapp)
    app.add_directive('geosciapplist', GeosciappList)
    app.connect('doctree-read', process_geosciapps)
    app.connect('doctree-resolved', process_geosciapp_nodes)
    app.connect('env-purge-doc', purge_geosciapps)
    app.connect('env-merge-info', merge_info)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
