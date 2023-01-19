from setuptools import setup

setup(
    name='ASE-Homework-group22',
    version='v1.0',
    description='ASE Homework-Github repository',
    author='Nandini Mundra',
    author_email='nmundra@ncsu.edu',
    packages=['src', 'tst'],
        long_description="""\
            Creating github repository files.
            .gitignore
            CODE-OF-CONDUCT.md
            CONTRIBUTING.md
            LICENSE.md
            CITATION.md
            INSTALL.md
            README.md
            setup.py
            src/
              __init__.py
              Num.py
              Sym.py
              main.py
              Misc.py
              list_util.py
              consts.py
              str_util.py
            tst
              test_engine.py
        """,
        classifiers=[
            "License :: MIT License",
            "Programming Language :: Python",
            "Development Status :: Planning",
            "Intended Audience :: Developers",
            "Topic :: Automated Software Engineering (CSC510 - 021)",
        ],
        keywords='requirements license python gitignore',
        license='MIT',
        )
