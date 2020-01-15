from setuptools import setup

with open("requirements.txt") as f:
    install_requires = filter(lambda line: line != "", f.read().split("\n"))

setup(
    name="Fool-house",
    description="Yellow house",
    long_description="",
    keywords=["YELLOW", "FOOL", "HOUSE", "CORPSMAN", "SCHIZO", "COUNT"],
    author="Andreew Gregory",
    author_email='6squaress@gmail.com',
    url="https://github.com/1Gregory/fool-house",
    download_url="https://github.com/1Gregory/fool-house/archive/1.1.tar.gz",
    version="1.1",
    install_requires=install_requires,
    packages=["fool_house"],
    license="MIT",
)
