from setuptools import setup
setup(
    name='ArticleTools',
    version='1.0.0',
    description="Traitement des fichiers .bib afin de donner un tableau récapitulatif.",
    author='Lionel Trovalet & Charles Lignée',
    author_email='lionel.trovaletl@univ-reunion.fr & charles.lignee@ensam.eu',
    packages=['ArticleTools'],  # same as name
    install_requires=['bibtexparser==1.2.0',
                    'future==0.18.2',
                    'numpy==1.22.2',
                    'pandas==1.4.1',
                    'pyparsing==3.0.7',
                    'python-dateutil==2.8.2',
                    'pytz==2021.3',
                    'RISparser==0.4.4',
                    'six==1.16.0',]  # external packages as dependencies
)