
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
from sphinx.locale import _
from sphinx.environment import NoUri
from sphinx.util.nodes import set_source_info
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition


class purpose_node(nodes.Admonition, nodes.Element):
    pass


class purposelist(nodes.General, nodes.Element):
    pass


class Purpose(BaseAdmonition):
    """
    A purpose entry, displayed (if configured) in the form of an admonition.
    """

    node_class = purpose_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }

    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-purpose']

        (purpose,) = super(Purpose, self).run()
        if isinstance(purpose, nodes.system_message):
            return [purpose]

        purpose.insert(0, nodes.title(text=_('Purpose')))
        set_source_info(self, purpose)

        env = self.state.document.settings.env
        targetid = 'purpose'
        targetnode = nodes.target('', '', ids=[targetid])
        return [targetnode, purpose]


def process_purposes(app, doctree):
    # collect all purposes in the environment
    # this is not done in the directive itself because it some transformations
    # must have already been run, e.g. substitutions
    env = app.builder.env
    if not hasattr(env, 'purpose_all_purposes'):
        env.purpose_all_purposes = []
    for node in doctree.traverse(purpose_node):
        app.emit('purpose-defined', node)

        try:
            targetnode = node.parent[node.parent.index(node) - 1]
            if not isinstance(targetnode, nodes.target):
                raise IndexError
        except IndexError:
            targetnode = None
        newnode = node.deepcopy()
        del newnode['ids']
        env.purpose_all_purposes.append({
            'docname': env.docname,
            'source': node.source or env.doc2path(env.docname),
            'lineno': node.line,
            'purpose': newnode,
            'target': targetnode,
        })



class PurposeList(Directive):
    """
    A list of all purpose entries.
    """

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        # Simply insert an empty purposelist node which will be replaced later
        # when process_purpose_nodes is called
        return [purposelist('')]


def process_purpose_nodes(app, doctree, fromdocname):
    if not app.config['purpose_include_purposes']:
        for node in doctree.traverse(purpose_node):
            node.parent.remove(node)

    # Replace all purposelist nodes with a list of the collected purposes.
    # Augment each purpose with a backlink to the original location.
    env = app.builder.env

    if not hasattr(env, 'purpose_all_purposes'):
        env.purpose_all_purposes = []

    for node in doctree.traverse(purposelist):
        if not app.config['purpose_include_purposes']:
            node.replace_self([])
            continue

        content = []

        for purpose_info in env.purpose_all_purposes:
            para = nodes.paragraph(classes=['purpose-source'])
            if app.config['purpose_link_only']:
                description = _('<<original entry>>')
            else:
                description = (
                    _('(The <<original entry>> is located in %s, line %d.)') %
                    (purpose_info['source'], purpose_info['lineno'])
                )
            desc1 = description[:description.find('<<')]
            desc2 = description[description.find('>>')+2:]
            para += nodes.Text(desc1, desc1)

            # Create a reference
            newnode = nodes.reference('', '', internal=True)
            innernode = nodes.emphasis(_('original entry'), _('original entry'))
            try:
                newnode['refuri'] = app.builder.get_relative_uri(
                    fromdocname, purpose_info['docname'])
                newnode['refuri'] += '#' + purpose_info['target']['refid']
            except NoUri:
                # ignore if no URI can be determined, e.g. for LaTeX output
                pass
            newnode.append(innernode)
            para += newnode
            para += nodes.Text(desc2, desc2)

            # (Recursively) resolve references in the purpose content
            purpose_entry = purpose_info['purpose']
            env.resolve_references(purpose_entry, purpose_info['docname'],
                                   app.builder)

            # Insert into the purposelist
            content.append(purpose_entry)
            content.append(para)

        node.replace_self(content)


def purge_purposes(app, env, docname):
    if not hasattr(env, 'purpose_all_purposes'):
        return
    env.purpose_all_purposes = [purpose for purpose in env.purpose_all_purposes
                                if purpose['docname'] != docname]


def merge_info(app, env, docnames, other):
    if not hasattr(other, 'purpose_all_purposes'):
        return
    if not hasattr(env, 'purpose_all_purposes'):
        env.purpose_all_purposes = []
    env.purpose_all_purposes.extend(other.purpose_all_purposes)


def visit_purpose_node(self, node):
    self.visit_admonition(node)
    # self.visit_admonition(node, 'purpose')


def depart_purpose_node(self, node):
    self.depart_admonition(node)


def setup(app):
    app.add_event('purpose-defined')
    app.add_config_value('purpose_include_purposes', True, 'html')
    app.add_config_value('purpose_link_only', False, 'html')
    app.add_config_value('purpose_emit_warnings', False, 'html')

    app.add_node(purposelist)
    app.add_node(purpose_node,
                 html=(visit_purpose_node, depart_purpose_node),
                 latex=(visit_purpose_node, depart_purpose_node),
                 text=(visit_purpose_node, depart_purpose_node),
                 man=(visit_purpose_node, depart_purpose_node),
                 texinfo=(visit_purpose_node, depart_purpose_node))

    app.add_directive('purpose', Purpose)
    app.add_directive('purposelist', PurposeList)
    app.connect('doctree-read', process_purposes)
    app.connect('doctree-resolved', process_purpose_nodes)
    app.connect('env-purge-doc', purge_purposes)
    app.connect('env-merge-info', merge_info)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
