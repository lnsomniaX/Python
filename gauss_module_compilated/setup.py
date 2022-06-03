from setuptools import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize('gauss_cython.pyx'))