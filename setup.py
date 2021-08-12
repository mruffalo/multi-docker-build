from pathlib import Path

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

here = Path(__file__).parent.absolute()

# Get the long description from the README file
with open(here / "README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="multi-docker-build",
    version="0.7.1",
    description="Automated building/tagging/pushing of multiple Docker images in succession",
    long_description=long_description,
    url="https://github.com/mruffalo/multi-docker-build",
    author="Matt Ruffalo",
    author_email="matt.ruffalo@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="docker automation",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "build_docker_images=multi_docker_build.build_docker_images:main",
        ],
    },
)
