from setuptools import find_packages, setup

setup(
    name='cadena',
    packages=find_packages(include=['cadena']),
    version='0.0.2',
    description='Proyecto 5 de IE0405 - Modelos Probabilísticos de Señales y Sistemas',
    author='Mario Roberto Peralta A.',
    license='MIT',
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'matplotlib',
    ],
)
