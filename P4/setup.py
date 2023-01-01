from setuptools import find_packages, setup

setup(
    name='proceso',
    packages=find_packages(include=['proceso']),
    version='0.0.3',
    description='Proyecto 4 de IE0405 - Modelos Probabilísticos de Señales y Sistemas',
    author='Mario R. Peralta A',
    license='MIT',
    install_requires=[
        'numpy',
        'scipy',
        'requests',
        'matplotlib',
        'pandas',
        'datetime',
    ],
)
