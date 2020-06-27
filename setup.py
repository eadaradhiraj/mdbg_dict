from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
      name="mdbg_dict",
      description="Unofficial MDBG command line interface",
      version="1.0",
      url="https://github.com/eadaradhiraj/mdbg_dict",
      install_requires=["beautifulsoup4","requests","colorama"],
      packages=find_packages(),
      scripts=["mdbg/mdbg_dict.py"]
     )