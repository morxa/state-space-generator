import os
import subprocess

from setuptools import setup
from setuptools.command.build_py import build_py


__version__ = "0.1.5"


class CustomBuild(build_py):
    def run(self):
        """ Builds the scorpion binaries. """
        curr_dir = os.getcwd()
        os.chdir(os.path.join(curr_dir, 'state_space_generator/scorpion'))
        subprocess.check_call(["python", "build.py"])
        os.chdir(curr_dir)
        super().run()


setup(
    name="state_space_generator",
    version=__version__,
    license='GNU',
    author="Dominik Drexler, Jendrik Seipp",
    author_email="dominik.drexler@liu.se, jendrik.seipp@liu.se",
    url="https://github.com/drexlerd/state-space-generator",
    description="A tool for state space exploration of PDDL files",
    long_description="",
    packages=["state_space_generator"],
    # package_data is copied after build, manifest is for source distribution.
    package_data={"state_space_generator":
        ["scorpion/fast-downward.py",
         "scorpion/README.md",
         "scorpion/LICENSE.md",
         "scorpion/builds/release/bin/*",
         "scorpion/driver/*"]
    },
    cmdclass={
        'build_py': CustomBuild},
    include_package_data=True,
    zip_safe=False,  # contains platform specific code
)
