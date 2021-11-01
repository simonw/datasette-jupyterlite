from setuptools import setup
import os

VERSION = "0.1a0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-jupyterlite",
    description="JupyterLite as a Datasette plugin",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-jupyterlite",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-jupyterlite/issues",
        "CI": "https://github.com/simonw/datasette-jupyterlite/actions",
        "Changelog": "https://github.com/simonw/datasette-jupyterlite/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_jupyterlite"],
    entry_points={"datasette": ["jupyterlite = datasette_jupyterlite"]},
    install_requires=["datasette", "jupyterlite"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-jupyterlite[test]"],
    package_data={"datasette_jupyterlite": ["static/*"]},
    python_requires=">=3.7",
)
