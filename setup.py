import os
from setuptools import find_packages,setup
package_version = os.getenv('PACKAGE_VERSION', 'default_version')

setup (
    name='mypythonlib',
    packages=find_packages(include=['mypythonlib']),
    version=package_version,
    description='test python library',
    install_requires=[]
)
