import setuptools

setuptools.setup(
    name="nes",
    version="0.1.0",
    author="William, Bonnie, and Jeremy Magland",
    author_email="jeremy.magland@gmail.com",
    description="nes",
    url="https://github.com/magland/nes",
    packages=setuptools.find_packages(),
    include_package_data=True,
    scripts=[
        "bin/nes"
    ],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
