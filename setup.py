from setuptools import find_packages,setup

setup (
    name='mypythonlib',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.0',
    description='test python library',
    install_requires=[]
)