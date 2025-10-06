# setup.py
from setuptools import setup, find_packages

setup(
    name="pkgbuild_parser",
    version="0.1.0",
    author="KevinCrrl",
    description="Módulo sencillo para obtener datos básicos de un PKGBUILD de Arch Linux",
    url="https://github.com/KevinCrrl/pkgbuild_parser",
    packages=find_packages(),
    python_requires=">=3.6",
)
