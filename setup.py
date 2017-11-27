from setuptools import setup
from os import path, walk
from itertools import chain

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open('README.rst') as f:
    long_description = f.read()


# Gather data files required
def package_files(directory):
    for (p, _, fs) in walk(directory):
        for f in fs:
            yield path.join('..', p, f)


setup(
    name='webcon',
    version='0.0.5',
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
    packages=['webcon'],
    install_requires=[
        'argcomplete',
        'bottle',
        'termcolor',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'webcon=webcon.webcon:main',
        ],
    },
    package_data={'webcon': list(chain(
        package_files('webcon/static'),
        package_files('webcon/views'),
    ))},
)
