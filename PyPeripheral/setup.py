"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : setup.py
"""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

from setuptools import setup

setup(
    name='PyPeripheral',
    version='0.1.2',
    description='A RGB Controlling Library for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/gooday2die/PyPeripheral',
    author='Gooday2die',
    author_email='edina00@naver.com',
    license='MIT',
    packages=['PyPeripheral'],
    install_requires=['cuesdk', 'requests==2.21.0'],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Topic :: System :: Hardware',
    ],
)
