from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sampah",  # your package name here
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,  # <-- This is important!
    install_requires=["flask"],
     entry_points={
        "console_scripts": [
            "sampah=sampah.cli:main"
        ]
    },
    author="Amirul Sadikin",
    author_email="ai.amirul.sadikin@gmail.com",
    description="Short description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/SAMPAH",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
