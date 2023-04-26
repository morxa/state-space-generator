import os
import subprocess
from pathlib import Path

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext


__version__ = "0.0.8"
HERE = Path(__file__).resolve().parent


class BuildExt(build_ext):
    def build_extensions(self):
        self.extensions = [
            Extension('my_package.my_module', ['my_package/my_module.cpp'])
        ]
        super().build_extensions()  


setup(
    name="state_space_generator",
    version=__version__,
    license='GNU',
    author="Dominik Drexler, Jendrik Seipp",
    author_email="dominik.drexler@liu.se, jendrik.seipp@liu.se",
    url="https://github.com/drexlerd/state-space-generator",
    description="A tool for state space exploration of PDDL files",
    long_description="",
    packages=['state_space_generator'],
    package_dir={'state_space_generator': 'src/state_space_generator'},
    cmdclass={'build_ext': BuildExt},
    include_package_data=True,
    zip_safe=False,
)
