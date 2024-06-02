import setuptools

with open("README.md", "r", encoding="utf-8") as fd:
    long_description = fd.read()

setuptools.setup(
    name="logs_parser",
    version="1.0.1",
    author="RTzoneva",
    author_email="logpai@users.noreply.github.com",
    description="A tool to parse logs and extracting connections for a particular host.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(
        exclude=["tests", "input"]),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=["regex==2.2.1"],
    keywords=['log parsing', 'hosts', 'time range']
)
