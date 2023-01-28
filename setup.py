import setuptools 
import os

def requirements(file="requirements.txt"):
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return [i.strip() for i in r]
    else:
        return []


def readme(file="README.md"):
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return r.read()
    else:
        return ""

setuptools.setup(
    name='PyLeaves',
    version='1.0.0',
    author='MrMKN',
    long_description=readme(),
    license='GNU General Public License v3.0',
    description='Python package',                           
    package_data={
      "PyLeaves": ["py.typed"],
    },
    url="https://github.com/MrMKN/PyLeaves",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='~=3.7',
    py_modules=["pyleaves"],
)
