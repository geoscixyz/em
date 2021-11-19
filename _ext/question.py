
"""
    Adapted from sphinx.ext.question

    https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/question.py

    Allow questions to be inserted into your documentation.  Inclusion of questions can
    be switched of by a configuration variable.  The questionlist directive collects
    all questions of your project and lists them along with a backlink to the
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


class question_node(nodes.Admonition, nodes.Element):
    pass


class questionlist(nodes.General, nodes.Element):
    pass


class Question(BaseAdmonition):
    """
    A question entry, displayed (if configured) in the form of an admonition.
    """

    node_class = question_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }

    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-question']

        (question,) = super(Question, self).run()
        if isinstance(question, nodes.system_message):
            return [question]

        question.insert(0, nodes.title(text=_('Question')))
        set_source_info(self, question)

        env = self.state.document.settings.env
        targetid = 'question'
        targetnode = nodes.target('', '', ids=[targetid])
        return [targetnode, question]


def process_questions(app, doctree):
    # collect all questions in the environment
    # this is not done in the directive itself because it some transformations
    # must have already been run, e.g. substitutions
    env = app.builder.env
    if not hasattr(env, 'question_all_questions'):
        env.question_all_questions = []
    for node in doctree.traverse(question_node):
        app.emit('question-defined', node)

        try:
            targetnode = node.parent[node.parent.index(node) - 1]
            if not isinstance(targetnode, nodes.target):
                raise IndexError
        except IndexError:
            targetnode = None
        newnode = node.deepcopy()
        del newnode['ids']
        env.question_all_questions.append({
            'docname': env.docname,
            'source': node.source or env.doc2path(env.docname),
            'lineno': node.line,
            'question': newnode,
            'target': targetnode,
        })



class QuestionList(Directive):
    """
    A list of all question entries.
    """

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        # Simply insert an empty questionlist node which will be replaced later
        # when process_question_nodes is called
        return [questionlist('')]


def process_question_nodes(app, doctree, fromdocname):
    if not app.config['question_include_questions']:
        for node in doctree.traverse(question_node):
            node.parent.remove(node)

    # Replace all questionlist nodes with a list of the collected questions.
    # Augment each question with a backlink to the original location.
    env = app.builder.env

    if not hasattr(env, 'question_all_questions'):
        env.question_all_questions = []

    for node in doctree.traverse(questionlist):
        if not app.config['question_include_questions']:
            node.replace_self([])
            continue

        content = []

        for question_info in env.question_all_questions:
            para = nodes.paragraph(classes=['question-source'])
            if app.config['question_link_only']:
                description = _('<<original entry>>')
            else:
                description = (
                    _('(The <<original entry>> is located in %s, line %d.)') %
                    (question_info['source'], question_info['lineno'])
                )
            desc1 = description[:description.find('<<')]
            desc2 = description[description.find('>>')+2:]
            para += nodes.Text(desc1, desc1)

            # Create a reference
            newnode = nodes.reference('', '', internal=True)
            innernode = nodes.emphasis(_('original entry'), _('original entry'))
            try:
                newnode['refuri'] = app.builder.get_relative_uri(
                    fromdocname, question_info['docname'])
                newnode['refuri'] += '#' + question_info['target']['refid']
            except NoUri:
                # ignore if no URI can be determined, e.g. for LaTeX output
                pass
            newnode.append(innernode)
            para += newnode
            para += nodes.Text(desc2, desc2)

            # (Recursively) resolve references in the question content
            question_entry = question_info['question']
            env.resolve_references(question_entry, question_info['docname'],
                                   app.builder)

            # Insert into the questionlist
            content.append(question_entry)
            content.append(para)

        node.replace_self(content)


def purge_questions(app, env, docname):
    if not hasattr(env, 'question_all_questions'):
        return
    env.question_all_questions = [question for question in env.question_all_questions
                                if question['docname'] != docname]


def merge_info(app, env, docnames, other):
    if not hasattr(other, 'question_all_questions'):
        return
    if not hasattr(env, 'question_all_questions'):
        env.question_all_questions = []
    env.question_all_questions.extend(other.question_all_questions)


def visit_question_node(self, node):
    self.visit_admonition(node)
    # self.visit_admonition(node, 'question')


def depart_question_node(self, node):
    self.depart_admonition(node)


def setup(app):
    app.add_event('question-defined')
    app.add_config_value('question_include_questions', True, 'html')
    app.add_config_value('question_link_only', False, 'html')
    app.add_config_value('question_emit_warnings', False, 'html')

    app.add_node(questionlist)
    app.add_node(question_node,
                 html=(visit_question_node, depart_question_node),
                 latex=(visit_question_node, depart_question_node),
                 text=(visit_question_node, depart_question_node),
                 man=(visit_question_node, depart_question_node),
                 texinfo=(visit_question_node, depart_question_node))

    app.add_directive('question', Question)
    app.add_directive('questionlist', QuestionList)
    app.connect('doctree-read', process_questions)
    app.connect('doctree-resolved', process_question_nodes)
    app.connect('env-purge-doc', purge_questions)
    app.connect('env-merge-info', merge_info)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
