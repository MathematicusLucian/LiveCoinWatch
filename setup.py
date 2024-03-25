from setuptools import setup, find_packages

setup(
    name="LiveCoinWatch",
    version="1.0.0",
    license="MIT",
    description="Interface in Python for the Live Coin Watch API",
    long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.md").read(),
    long_description_content_type="text/markdown",
    author="Luke Jones",
    url="https://github.com/MathematicusLucian/LiveCoinWatch",
    packages=find_packages(),
    install_requires=["requests"],
    keywords=["crypto", "crypto bot", "livecoinwatch"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)