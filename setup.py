"""
Python package file
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydatastructures", # Replace with your own username
    version="0.0.1",
    author="Matthieu BOUCHET",
    author_email="matthieu.bouchet@outlook.com",
    description="Basic library to implement data structures in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MatthieuBOUCHET/PyDataStructures",
    project_urls={
        "Bug Tracker": "https://github.com/MatthieuBOUCHET/PyDataStructures/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Education",
        "Natural Language :: French"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.0",
)