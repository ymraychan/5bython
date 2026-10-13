from setuptools import setup
from Cython.Build import cythonize

modules = ["get_levels.py"]

if __name__ == "__main__":
    setup(
        ext_modules=cythonize(
            modules,
            compiler_directives={"language_level": "3",
                                "cdivision": True,
                                "overflowcheck": False,
                                "nonecheck": False} 
        )
    )