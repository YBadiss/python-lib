import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yass-pkg",
    version="0.0.2",
    author="Yacine Badiss",
    author_email="yacine.badiss@gmail.com",
    description="A small example package",
    scripts=['bin/yass'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YBadiss/python-lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
