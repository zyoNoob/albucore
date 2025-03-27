from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    "numpy>=1.24.4",
    "typing-extensions>=4.9.0; python_version<'3.10'",
    "stringzilla>=3.10.4",
    "simsimd>=5.9.2",
    "opencv-python>=4.9.0.80",
]

setup(
    packages=find_packages(exclude=["tests", "benchmark"], include=['albucore*']),
    install_requires=INSTALL_REQUIRES,
)