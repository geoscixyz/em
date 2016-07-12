def checkDependencies():
    try:
        import numpy, scipy, matplotlib, sphinxcontrib.bibtex, sphinx_bootstrap_theme
        pass
    except Exception, e:
        raise Exception('Requirements not installed, run: "pip install -r requirements.txt" to install requirements')
    else:
        pass

def supress_nonlocal_image_warn():
    import sphinx.environment
    sphinx.environment.BuildEnvironment.warn_node = _supress_nonlocal_image_warn

def _supress_nonlocal_image_warn(self, msg, node, **kwargs):
    from docutils.utils import get_source_line

    if not msg.startswith('nonlocal image URI found:'):
        self._warnfunc(msg, '%s:%s' % get_source_line(node))



if __name__ == '__main__':
    checkDependencies()
