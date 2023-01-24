import setuptools  

setuptools.setup(
    name='PyLeaves',
    version='1.0.0',
    author='MrMKN',
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
