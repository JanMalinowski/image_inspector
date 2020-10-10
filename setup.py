# Majority of this scripte was copied from
# https://github.com/abhishekkrthakur/wtfml/blob/master/setup.py
from setuptools import setup, Extension
from setuptools import find_packages

import image_inspector


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="image_inspector",
        version=image_inspector.__version__,
        description="App for inspecting images",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Jan Malinowski",
        author_email="malinowwskijasiek1999@gmail.com",
        url="https://github.com/JanMalinowski/image_inspector",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
    )
