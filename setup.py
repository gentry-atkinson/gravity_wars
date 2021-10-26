import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Defen the Zyrth!",
    version="1.0.0",
    author="Gentry Atkinson",
    author_email="SingleStarSW@gmail.com",
    description="Defender of Zyrth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    license='license.txt'
)
