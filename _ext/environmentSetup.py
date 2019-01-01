from docutils.utils import get_source_line
import sphinx.environment

def checkDependencies():
    try:
        import numpy, scipy, matplotlib, sphinxcontrib.bibtex, sphinx_bootstrap_theme
        pass
    except (Exception, e):
        raise Exception("Requirements not installed, run: 'pip install -r requirements.txt' to install requirements")
    else:
        pass

def supress_nonlocal_image_warn():
    sphinx.environment.BuildEnvironment.warn_node = _supress_nonlocal_image_warn

def _supress_nonlocal_image_warn(self, msg, node, **kwargs):

    if not msg.startswith("nonlocal image URI found:"):
        self._warnfunc(msg, "%s:%s" % get_source_line(node))

def supress_citation_not_referenced():
    sphinx.environment.BuildEnvironment.warn_node = _supress_citation_not_referenced

def _supress_citation_not_referenced(self, msg, node, **kwargs):
    print(msg)
    if not (
        msg.lower().startswith("citation") and msg.lower().endswith("is not referenced.")
    ):
        self._warnfunc(msg, "%s:%s" % get_source_line(node))



if __name__ == "__main__":
    checkDependencies()
