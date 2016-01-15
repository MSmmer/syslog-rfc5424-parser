from setuptools import setup, find_packages


setup(
    name="syslog_rfc5424_parser",
    version="0.1",
    author="James Brown",
    author_email="jbrown@easypost.com",
    url="https://github.com/easypost/syslog_rfc5424_parser",
    description="Parser for RFC5424-compatible Syslog messages",
    license="ISC",
    packages=find_packages(exclude=['tests']),
    test_suite="nose.collector",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: ISC License (ISCL)",
    ]
)