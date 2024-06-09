from setuptools import setup, find_packages

setup(
    name='Couler',
    version='0.0.1',
    install_requires=[
        'json',
        'argparse',
        'secrets'
    ],
    packages=find_packages(
        where='app'
    ),
    entry_points={
        'console_scripts': [
            'couler = app:hello_world',
        ]
    }
)