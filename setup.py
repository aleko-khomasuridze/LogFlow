from pathlib import Path

from setuptools import find_packages, setup


BASE_DIR = Path(__file__).resolve().parent


setup(
    name="logify",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requirements.txt"],
    author="Aleko Khomasuridze",
    author_email="aleko.khomasurize@gmail.com",
    description="Simple but modular Logger Package for python",
    long_description=(BASE_DIR / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/aleko-khomasuridze/LogFlow",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)