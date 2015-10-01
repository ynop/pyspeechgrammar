import setuptools

setuptools.setup(
    name="pyspeechgrammar",
    version="0.1.0",
    url="https://github.com/ynop/pyspeechgrammar",

    author="Buechi Matthias",
    author_email="m.buechi@outlook.com",

    description="PySpeechGrammar can be used to parse and convert speech grammar formats.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        "modgrammar"
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
