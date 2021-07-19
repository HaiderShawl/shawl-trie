from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'A package that allows you to add, search, delete, autocomplete and display words in a trie.'

# Setting up
setup(
    name="shawl-trie",
    version=VERSION,
    author="Haider Shawl",
    author_email="<haidershawl@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pymongo'],
    keywords=['python','trie','shawl-trie'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)