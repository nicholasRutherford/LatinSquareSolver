from setuptools import setup, find_packages

long_desc = "Solve Latin Squares using forward checking "
long_desc += "and arc consistency."

setup(
    name='LatinSquareSolver',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='Solve Latin Squares',
    long_description=long_desc,

    # The project's main homepage.
    url='https://github.com/nicholasRutherford/LatinSquareSolver',

    # Author details
    author='Nicholas Rutherford',
    author_email='nicholas.rutherford.pypi@cluemail.com',

    # Choose your license
    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Dev Status
        'Development Status :: 4 - Beta',

        # Target audience
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        # License
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Python Version
        'Programming Language :: Python :: 2.7',

        # Environment
        'Environment :: Console',
    ],

    # What does your project relate to?
    keywords='LatinSquare arc-consitency forward-checking',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['sphinx', 'sphinx-rtd-theme'],
        'test': ['nose'],
    },
)
