from setuptools import setup, find_packages

setup(
    name='couler',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'couler = couler:main',
        ]
    }
)