import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="keboola.component-davidesner",  # TESTING NAME
    version="0.0.1",
    author="Keboola KDS Team",
    author_email="data_ca@keboola.com",
    description="General library for Python applications running in Keboola Connection environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keboola/python-component",
    packages=setuptools.find_namespace_packages(include=['keboola.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 4 - Beta"
    ],
    python_requires='>=3.6'
)
