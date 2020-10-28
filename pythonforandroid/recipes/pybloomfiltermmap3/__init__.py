from pythonforandroid.recipe import PythonRecipe


class PyBloomFilterMmap3Recipe(PythonRecipe):
    version = '0.5.3'
    url = 'https://pypi.python.org/packages/source/p/pybloomfiltermmap3/pybloomfiltermmap3-{version}.tar.gz'
    depends = ['setuptools', 'cffi']
    site_packages_name = 'pybloomfiltermmap3'
    call_hostpython_via_targetpython = False


recipe = PyBloomFilterMmap3Recipe()
