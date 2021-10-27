from setuptools import setup

setup(
    name='crispy-winner',
    version='1.0.0',
    packages=['crispywinner'],
    install_requires=[
        'requests'
    ],
    entry_points={
        "console_scripts": ["crispy-winner=crispywinner:run"]
    }
)
