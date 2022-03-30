import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OpenWeatherClass",
    version="0.3.1",
    author="Brian Hudson",
    description="A Python implementation of OpenWeather's API",
    url="https://github.com/bearhudson/OpenWeatherClass",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "openweatherclass"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
