import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name ="sport_sessions_crawling",
    version = "0.0.1",
    author = "Guillaume Le Bihan",
    author_email = "rainrider37@gmail.com",
    description = ("A pet project whose purpose is, first, \
                   to gather my sport sessions data"),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['sport_sessions_crawling'],
    long_description=read('README.md'),
    classifiers=[
                "Development Status :: 3 - Alpha",
                "Topic :: Utilities",
                "License :: OSI Approved :: BSD License",

    ],
)
