from setuptools import setup

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name='crispy-winner',
    version='1.0.1',
    packages=['crispywinner'],
    description="Mitigate discord phishing scams by spamming their webhooks",
    long_description=long_description,
    install_requires=[
        'requests'
    ],
    entry_points={
        "console_scripts": ["crispy-winner=crispywinner:run"]
    }
)
