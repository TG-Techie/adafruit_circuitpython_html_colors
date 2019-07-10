"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='adafruit-circuitpython-html-colors',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='html5 colors converted to displayio 24bit hex colors in CamelCaseNames and under_score_names.',
    long_description=long_description,
    long_description_content_type='text/x-rst',

    # The project's main homepage.
    url='https://github.com/adafruit/Adafruit_CircuitPython_html_colors',

    # Author details
    author='Adafruit Industries',
    author_email='circuitpython@adafruit.com',

    install_requires=[
        'Adafruit-Blinka'
    ],

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='adafruit blinka circuitpython micropython html_colors displayio color html '
             '24bit hex python circuitpyhton',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # TODO: IF LIBRARY FILES ARE A PACKAGE FOLDER,
    #       CHANGE `py_modules=['...']` TO `packages=['...']`
    py_modules=['adafruit_html_colors'],
)
