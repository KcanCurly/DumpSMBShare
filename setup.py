from setuptools import setup, find_packages

setup(
    name="DumpSMBShare",
    version="1.0.0",
    author="KcanCurly",
    description="A script to dump files and folders remotely from a Windows SMB share.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/DumpSMBShare",
    packages=find_packages(),
    install_requires=[
        "impacket",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "DumpSMBShare=src.DumpSMBShare:main",  
        ],
    },
)