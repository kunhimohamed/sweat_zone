from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sweat_zone/__init__.py
from sweat_zone import __version__ as version

setup(
	name="sweat_zone",
	version=version,
	description="Gym App",
	author="kunhimohamed6@gmail.com",
	author_email="kunhimohamed6@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
