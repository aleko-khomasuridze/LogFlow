from setuptools import setup, find_packages

setup(
    name="package_publishing",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Aleko Khomasuridze",
    author_email="aleko.khomasurize@gmail.com",
    description="Simple but modular Logger Package for python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aleko-khomasuridze/LogFlow",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)