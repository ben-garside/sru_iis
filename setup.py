"""
SRU IIS
Special Reconnaissance Unit
-----------
python SRU IIS
Link
`````
* Source
  https://github.com/abusaidm/
"""
from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="sru_iis",
    version=version,
    author="Mohamed Abusaid",
    author_email="m.abusaid<at>yahoo<dot>com",
    packages=find_packages(),
    include_package_data=True,
    url="http://github.com/abusaidm/sru_iis/packages/{}/".format(version),

    # license="LICENSE.txt",
    description="sru_iis",
    # long_description=open("README.txt").read() or just """ lots of text here too""",
    # Dependent packages (distributions)
    dependency_links=[
        "https://github.com/abusaidm/iis_shim/tarball/master#egg=iis_shim-0.1.0",
    ],
    install_requires=[
        "iis_shim>=0.1.0"
    ]
)