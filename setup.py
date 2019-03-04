"""
Installation script
"""
from setuptools import setup

def get_requirements():
    """
    get the requirements
    """
    reqs = []
    with open("requirements.txt") as file:
        for line in file:
            reqs.append(line)
    return reqs

setup(name='hyperyaml',
      version='0.1.2',
      description='A library to build and run hyperparameter tuning schemes from yaml files',
      url='https://github.com/josmcg/HyperYAML',
      author='Josh McGrath',
      author_email='joshuawmcgrath@gmail.com',
      license='MIT',
      packages=['hyperyaml'],
      test_suite="nose.collector",
      install_requires=get_requirements(),
      zip_safe=False)
