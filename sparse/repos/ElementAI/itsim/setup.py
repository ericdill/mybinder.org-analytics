from setuptools import setup
from setuptools.command.install import install
from subprocess import check_call

with open("README.md", "r") as file_long_description:
    long_description = file_long_description.read()

sphinx_cmd_list = ["sphinx-apidoc itsim -METf -o sphinx/source/modules --implicit-namespaces",
                   "make -C sphinx html"]


class PostInstall(install):
    def run(self):
        for cmd in sphinx_cmd_list:
            check_call(cmd.split(" "))


setup(
    name='itsim',
    version='0.0.1',
    packages=['itsim'],
    data_files=[('.', ['LICENSE'])],
    scripts=["bin/itsim_serve_datastore.py"],
    install_requires=['greensim'],
    description='IT infrastructure and cyberattack simulation toolkit',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ElementAI/itsim",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
    cmdclass={"install": PostInstall}
)
