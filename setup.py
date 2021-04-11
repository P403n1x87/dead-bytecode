from setuptools import find_packages, setup

setup(
    name="dead-bytecode",
    version="0.0.0",
    description="Backport of bytecode to Python 2",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/p403n1x87/dead-bytecode",
    author="Gabriele N. Tornetta",
    author_email="phoenix1987@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages(),
    python_requires=">=2.7, <3",
    setup_requires=["setuptools_scm==5.0.2"],
    use_scm_version=True,
    install_requires=["aenum>=2.0", "unittest2"],
    extras_require={
        "test": ["coverage", "pytest", "pytest-cov"],
    },
    project_urls={  # Optional
        "Bug Reports": "https://github.com/p403n1x87/dead-bytecode/issues",
        "Source": "https://github.com/p403n1x87/dead-bytecode/",
    },
)
