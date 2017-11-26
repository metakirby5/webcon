from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

# Get requirements from requirements.txt
with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().strip().split('\n')

setup(
    name='webcon',
    version='0.0.1',
    description='Control your computer from a web interface',
    long_description=long_description,
    url='https://github.com/metakirby5/webcon',
    author='Ethan Chan',
    author_email='metakirby5@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',

        'Programming Language :: Python :: 3',
    ],
    keywords='web controller config yaml',
    py_modules=['webcon'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'webcon=webcon:main',
        ],
    },
)
