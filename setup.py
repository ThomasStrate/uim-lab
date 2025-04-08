# setup.py — UIM-Core install script

from setuptools import setup, find_packages

setup(
    name='uimcore',
    version='0.1.0',
    description='Core simulation engine for the Unified Information Model (UIM)',
    author='Thomas Strate',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7',
)