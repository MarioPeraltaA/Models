from setuptools import find_packages, setup

setup(
    name='consumo',
    packages=find_packages(include=['consumo']),
    version='0.0.3',
    description='Proyecto 3 de IE0405 - Modelos Probabilísticos de Señales y Sistemas',
    author='Mario Roberto Peralta A.',
    license='MIT',
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'matplotlib',
        'requests',
        'datetime',
        'fitter',
    ],
)
