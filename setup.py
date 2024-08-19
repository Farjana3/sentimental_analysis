import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()

__version__ ="0.0.0"

REPO_NAME= "sentimental_analysis"
AUTHOR_USER_NAME= "Farjana3"
SRC_REPO= "happyAndSadFace"
AUTHOR_EMAIL= "farmail9999@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simple python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug tracker" : f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)