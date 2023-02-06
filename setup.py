# Kanged from https://github.com/PR0FESS0R-99/Telethroid
# My master https://github.com/PR0FESS0R-99

import re
import setuptools


# find repository version
with open("pyleaves/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

# read readme.md
with open("README.md", encoding="utf-8") as f:
    readme = f.read()
  
setuptools.setup(
    name="PyLeaves",
    version=version,
    author="MrMKN",
    long_description_content_type="text/markdown",
    long_description=readme,
    license='GNU General Public License v3.0',
    description='Python package for telegram bots and sub tool for pyrogram',                           
    package_data={
      "Telethroid": ["py.typed"],
    },
    url="https://github.com/MrMKN/PyLeaves",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    py_modules=["pyleaves"],
)






