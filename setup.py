import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
VERSION = open(os.path.join(here, 'VERSION')).read()

requires = [

]

setup(
    name='Arithain',
    version=VERSION,
    description='Arithmetic training tool',
    long_description=README,
    author='Artem Kostiuk',
    author_email='postatum@gmail.com',
    url='https://github.com/postatum/arithain',
    license='MIT',
    install_requires=requires,
    tests_require=requires,
    classifiers=[
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ],
    packages=find_packages(),
    entry_points={
      'console_scripts': [
          'arithain = arithain.__main__:main'
      ]
    }
)