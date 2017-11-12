from setuptools import setup

setup(
    name='rend',
    version='1.2',
    description='A rend parser lib',
    author='280canvas',
    author_email='hello@280canvas.com',
    packages=['rend', 'rend.ANTLR'],
    install_requires=['antlr4-python3-runtime', ],
)
