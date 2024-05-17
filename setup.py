from setuptools import find_packages,setup
version = $(minor).$(patch).$(Rev:r)

setup (
    name='mypythonlib',
    packages=find_packages(include=['mypythonlib']),
    version=version,
    description='test python library',
    install_requires=[]
)
