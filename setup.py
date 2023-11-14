from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Income_ML_Project"
AUTHOR_USER_NAME = "abhishekjadhav3470"
SRC_REPO = "Models"
LIST_OF_REQUIREMENTS = []


setup(
    name="Models",
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Ml Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="abhishekjadhav3470@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)