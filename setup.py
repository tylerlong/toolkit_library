from distutils.core import setup
import toolkit_library
from toolkit_library import inspector

def read_modules():
    result = ''
    package = inspector.PackageInspector(toolkit_library)
    for module in package.get_all_modules():
        exec('from toolkit_library import {0}'.format(module))
        result = '{0}{1}\n'.format(result, eval('{0}.__doc__'.format(module)))
    return result.rstrip()

readme = ''
with open('README_template', 'r') as file:
    readme = file.read()
readme = readme.replace('{{ modules }}', read_modules())
with open('README.rst', 'w') as file:
    file.write(readme)

    
setup(
    name = toolkit_library.__name__,
    version = toolkit_library.__version__,
    url = 'https://github.com/tylerlong/toolkit_library',
    license = 'BSD',
    author = toolkit_library.__author__,
    author_email = 'tyler4long@gmail.com',
    description = 'Toolkit Library, full of useful toolkits',
    long_description = readme,
    packages = ['toolkit_library', ],
    platforms = 'any',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
